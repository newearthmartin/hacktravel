<template>
  <div class="test">
    <SearchComponent></SearchComponent>
     <el-row>
      <el-col :span="16">
        <div>
          <p><strong>org.id:</strong> {{ orgId }}</p>
          <p><strong>owner:</strong> {{ owner }}</p>
          <p><strong>json URL:</strong> &nbsp;<a :href="jsonUrl" target="_blank">{{jsonUrl}}</a></p>
          <p class="json"><strong>json:</strong> </p>
          <pre class="code">{{ orgJson }}</pre>
        </div>
      </el-col>
      <el-col :span="8">
        <div>
          <p><strong>LIF balance:</strong> {{ lifBalance }}</p>
          <p><strong>Can we trust this website(using wt-hackathon trust service):</strong> {{ trustWebsite }}</p>
        </div>
      </el-col>
    </el-row>

  </div>
</template>

<script>
import helper from '@/helper.js';
import axios from 'axios';
import SearchComponent from '@/components/SearchComponent.vue';
import LifTokenTest from '@windingtree/lif-token/build/contracts/LifTokenTest.json';
import TruffleContract from 'truffle-contract';

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
      lifBalance: null,
      trustWebsite: null,
      owner: null,
    };
  },
  mounted() {
    this.libs = helper.getLibs();
    this.orgId = this.$route.params.orgId;
    this.getOrgJson();
  },
  beforeRouteUpdate(to, from, next) {
    console.log("Calling beforeRouteUpdate");
    this.orgId = to.params.orgId;
    this.getOrgJson();
    next();
  },
  methods: {
    async getOrgJson() {
      console.log("Parameter is " + this.orgId);
      this.loadedOrg = this.libs.getOrganization(this.orgId);
      var myThis = this;
      this.loadedOrg.orgJsonUri.then(function (value) {
        console.log("Calling from inside promise");
        
        myThis.jsonUrl = value;
        myThis.loadJsonFromUrl(value);
        myThis.loadLifBalance(myThis.orgId);
        myThis.getWebsiteTrustClue(myThis.orgId);
      }).catch(err => {
          this.orgJson = err;
      });
      this.owner = await this.loadedOrg.owner;
      console.log("Call done");
    },
    async loadJsonFromUrl(url) {
      var httpResponse = await axios.get(url);
      console.log(JSON.stringify(httpResponse));
      this.orgJson = httpResponse.data;
    },
    async loadLifBalance(url) {
      console.log("loading lif balance: " + JSON.stringify(url));
      var liftokentest = await this.getLifTokenTestContract();
      var balance = await liftokentest.balanceOf(url);
      this.lifBalance = balance.toString();
    },
    async getLifTokenTestContract() {
     let contract = TruffleContract(LifTokenTest);
     contract.setProvider(helper.getProvider());
     return contract.at('0xB6e225194a1C892770c43D4B529841C99b3DA1d7')
    },
    async getWebsiteTrustClue(orgId) {
      var httpResponse = await axios.get('http://caramon.kunveni.net:5010'+ '/clue/dns?organization='+orgId);
      this.trustWebsite = httpResponse.data.trusted;
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
