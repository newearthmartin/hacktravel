<template>
  <div class="test">
    <SearchComponent></SearchComponent>
<<<<<<< HEAD
    <p><strong>org.id:</strong> {{ orgId }}</p>
    <p><strong>json URL:</strong>&nbsp;<a :href="jsonUrl" target="_blank">{{jsonUrl}}</a></p>
    <p><strong>json:</strong></p>
    <pre class="code">{{ orgJson }}</pre>
=======
     <el-row>
      <el-col :span="16">
        <div>
          <p><strong>org.id:</strong> {{ orgId }}</p>
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

>>>>>>> new_master
  </div>
</template>

<script>
import helper from '@/helper.js';
import axios from 'axios';
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
<<<<<<< HEAD
=======
      lifBalance: null,
      trustWebsite: null,
>>>>>>> new_master
    };
  },
  mounted() {
    this.libs = helper.getLibs();
    this.orgId = this.$route.params.orgId;
    this.getOrgJson();
  },
  methods: {
    getOrgJson() {
      console.log("Parameter is " + this.orgId);
      this.loadedOrg = this.libs.getOrganization(this.orgId);
      var myThis = this;
      this.loadedOrg.orgJsonUri.then(function (value) {
        console.log("Calling from inside promise");
        console.log(value);
        myThis.jsonUrl = value;
        myThis.loadJsonFromUrl(value);
<<<<<<< HEAD
=======
        myThis.loadLifBalance(myThis.orgId);
        myThis.getWebsiteTrustClue(myThis.orgId);
>>>>>>> new_master
      }).catch(err => {
          this.orgJson = err;
      });
      console.log("Call done");
    },
    async loadJsonFromUrl(url) {
      var httpResponse = await axios.get(url);
      console.log(JSON.stringify(httpResponse));
      this.orgJson = httpResponse.data;
<<<<<<< HEAD
=======
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
>>>>>>> new_master
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
