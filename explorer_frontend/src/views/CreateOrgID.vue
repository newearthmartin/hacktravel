<template>
    <div class="createOrgId">
        <h1>Create an ORG.ID</h1>
        <h3>This service lets you create an ORG.ID.</h3>
        <h3>Please enter below the URI of your organization JSON.</h3>
        <h4>Note that you need to have the Metamask browser extension installed, and an ethereum account with some fund$ in it.</h4>
        <el-row>
            <el-col :span="20"><el-input placeholder="Enter ORG JSON URI" v-model="orgJsonUri"></el-input></el-col>
            <el-col :span="4"><el-button v-on:click="callCreateOrg()" type="primary" plain>Create ORG.ID!</el-button></el-col>
        </el-row>
    </div>
</template>

<script>
  import Eth from 'ethjs';
  import OrganizationFactory from '@windingtree/wt-contracts/build/contracts/OrganizationFactory.json';

  export default {
    name: 'createOrgId',
    data() {
      return {
        orgJsonUri: null,
      };
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
          //const orgJsonUri = 'https://github.com/newearthmartin/hacktravel/blob/master/files/airline_safe.json';  // this will be given by the user

          // create contract object for organization factory
          var contract = eth.contract(
              OrganizationFactory.abi,
              undefined,
              {"from": userAddress, "gas": 3000000}
          ).at(organizationFactoryAddress);

          // create ORG ID by calling
          // organization factory create method
          var result = contract["create"](this.orgJsonUri)
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
    }
  };
</script>

<style scoped>
</style>
