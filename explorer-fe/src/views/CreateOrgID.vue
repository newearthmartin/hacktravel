<template>
  <div class="test">
    <SearchComponent></SearchComponent>
    <p><strong>org.id:</strong> {{ orgId }}</p>
    <p><strong>json URL:</strong> &nbsp;<a :href="jsonUrl" target="_blank">{{jsonUrl}}</a></p>
    <p class="json"><strong>json:</strong> </p>
    <pre class="code">{{ orgJson }}</pre>
  </div>
</template>

<script>
import OrganizationFactory from '@windingtree/wt-contracts/build/contracts/OrganizationFactory.json';
import helper from '@/helper.js';
import axios from 'axios';
import Eth from 'ethjs';
import SearchComponent from '@/components/SearchComponent.vue';

export default {
  name: 'Explore',
  components: {
    SearchComponent
  },
  data() {
    return {
      orgId: null,
      libs: null,
      jsonUrl: null,
      orgJson: null,
    };
  },
  mounted() {
    this.libs = helper.getLibs();
    this.orgId = this.$route.params.orgId;
    this.getOrgJson();
    this.callCreateOrg();
  },
  methods: {
    callCreateOrg() {
      // check if metamask is installed
      if (!window.ethereum || !window.web3) {
        throw new Error('Metamask not found. Is it installed as an extension?');
      }

      // create ethjs object
      window.ethereum.enable();
      let eth = new Eth(window.web3.currentProvider);

      // grab the user's first account in metamask
      var accounts = eth.accounts()
      .then( (accounts) => {
        let userAddress = accounts[0];
        const organizationFactoryAddress = '0x78D1548E03660093B51159De0E615ea8F6B9eaF9';
        const orgJsonUri = 'https://github.com/newearthmartin/hacktravel/blob/master/files/airline_safe.json';  // this will be given by the user

        // create contract object for organization factory
        var contract = eth.contract(
            OrganizationFactory.abi,
            undefined,
            {"from": userAddress, "gas": 3000000}
        ).at(organizationFactoryAddress);

        // create ORG ID by calling
        // organization factory create method
        var result = contract["create"](orgJsonUri)
        .then( (txid) => {
            console.log("txid: ", txid);
        })
        .catch( (error) => {
            console.log("error: ", error);
        });

      })
      .catch( (error) => {
        console.log("error: ", error);
      });

    },

    getOrgJson() {
      console.log("Parameter is " + this.orgId);
      this.loadedOrg = this.libs.getOrganization(this.orgId);
      var myThis = this;
      this.loadedOrg.orgJsonUri.then(function (value) {
        console.log("Calling from inside promise");
        console.log(value);
        myThis.jsonUrl = value;
        myThis.loadJsonFromUrl(value);
      }).catch(err => {
          this.orgJson = err;
      });
      console.log("Call done");
    },
    async loadJsonFromUrl(url) {
      var httpResponse = await axios.get(url);
      console.log(JSON.stringify(httpResponse));
      this.orgJson = httpResponse.data;
    }
  }
};
</script>

<style scoped>
.code {
  font-family: 'Lucida Console', Monaco, monospace;
  font-size: smaller;
  text-align: left;
  padding: 5px;
  border: 1px solid #c4c7b2;
}
</style>
