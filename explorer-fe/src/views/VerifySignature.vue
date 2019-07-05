<template>
    <div class="verifySignature">
        <el-row>
            <el-col :span="20"><el-input placeholder="orgIdAddress" v-model="orgId"></el-input></el-col>
            <el-col :span="20"><el-input placeholder="message" v-model="message"></el-input></el-col>
            <el-col :span="20"><el-input placeholder="signature" v-model="signature"></el-input></el-col>
            <el-col :span="4"><el-button v-on:click="verifySiganture()" type="primary" plain>Verify Signature</el-button></el-col>
        </el-row>
        <div v-if="signaturesMatch === true">
            <br/>
            The Signer of the supplied message matches the Org ID
        </div>
        <div v-if="signaturesMatch === false">
            <br/>
            The Signer of the supplied message does not match the Org ID
        </div>
    </div>
</template>

<script>
  import helper from '@/helper.js';
  import { Accounts }  from 'web3-eth-accounts';
  import { hexToUtf8 } from 'web3-utils';
  import wtContracts  from '@windingtree/wt-contracts';
  import LifDepositAbi  from '@windingtree/trust-clue-lif-deposit/build/contracts/LifDeposit.json';
  import truffleContract from 'truffle-contract';

  export default {
    name: 'VerifySignature',
    data() {
      return {
        orgId: this.$route.query.orgId,
        message: null,
        signature: null,
        signaturesMatch: null,
      };
    },
    methods: {
      async verifySiganture() {

        const accounts = Accounts('https://ropsten.infura.io/v3/7714245c4ea74010879bda16618931c9');

        let signature = this.signature;
        let r = signature.slice(0,66);
        let s = '0x' + signature.slice(66,130);
        let v = '0x' + signature.slice(130,132);

        let signer = accounts.recover({
          messageHash: this.message,
          v: v,
          r: r,
          s: s
        })

        console.log('signer is ' + signer);

        this.signaturesMatch = signer === this.orgId;

      }
    }
  };
</script>

<style scoped>
</style>
