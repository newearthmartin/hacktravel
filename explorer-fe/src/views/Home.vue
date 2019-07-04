<template>
  <div class="hello">
    <H1>ORG.ID explorer</H1>
    <el-row>
      <el-col :span="20"><el-input placeholder="Enter your ORG.ID address" v-model="orgidIn"></el-input></el-col>
      <el-col :span="4"><el-button v-on:click="getOrgJson()" type="primary" plain>Explore</el-button></el-col>
    </el-row>
    <h2>DEBUG: {{ orgidIn }}</h2>
    <h2>ORG: {{ this.currentlySelectedOrg }}</h2>
  </div>
</template>

<script>
import { WtJsLibs } from '@windingtree/wt-js-libs';
import InMemoryAdapter from '@windingtree/off-chain-adapter-in-memory';
import axios from 'axios';

export default {
  name: 'Home',
  data () {
    return {
      orgidIn: '',
      libs: 'undefined',
      loadedOrg: {},
      shownOrg:{},
      currentlySelectedOrg: {},
    };
  },

  mounted() {
    this.libs = WtJsLibs.createInstance({
      onChainDataOptions: {
        provider: 'https://ropsten.infura.io/v3/7714245c4ea74010879bda16618931c9',
      },
      offChainDataOptions: {
        adapters: {
          // This is how you plug-in any off-chain data adapter you want.
          'in-memory': {
            options: {
              // some: options
            },
            create: (options) => {
              return new InMemoryAdapter(options);
            },
          },
        },
      },
      // This is how you configure trust clues
      /*
      trustClueOptions: {
        provider: 'http://ropsten.infura.io/v3/7714245c4ea74010879bda16618931c9', // or infura or any other ETH RPC node
        clues: {
          'curated-list': {
            options: {
              address: '0x...',
              provider: 'http://localhost:8545',
            },
            create: async (options) => {
              return new window.TrustClueCuratedList(options);
            },
          },
        }
      },*/
    });
  },

  methods: {
    getOrgJson() {
      console.log("Button clicked");
      console.log("Parameter is " + this.orgidIn)
      this.loadedOrg = this.libs.getOrganization(this.orgidIn);
      var myThis= this;
      this.loadedOrg.orgJsonUri.then(function(value){
        console.log("Calling from inside promise");
        console.log(value);
        myThis.shownOrg =  value;
        myThis.loadJsonFromUrl(value);
      });
      
      console.log("Call done");
    },

   async loadJsonFromUrl(url) {
      var httpResponse = await axios.get(url);

      console.log(JSON.stringify(httpResponse));
      this.currentlySelectedOrg = httpResponse.data;
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
