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
  import { utf8ToHex } from 'web3-utils';
  import wtContracts  from '@windingtree/wt-contracts';
  import LifDepositAbi  from '@windingtree/trust-clue-lif-deposit/build/contracts/LifDeposit.json';
  import truffleContract from 'truffle-contract';

  import ethjswallet from 'ethereumjs-wallet';
  import HDWalletProvider from 'truffle-hdwallet-provider';

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

        // let hash = accounts.hashMessage('message claim text');
        // console.log('hash is ' + hash);
        // const hdWalletProvider = new HDWalletProvider('eagle next flag someone catalog base sun warfare wasp foot shed obscure luggage man explain', 'https://ropsten.infura.io/v3/7714245c4ea74010879bda16618931c9');
        // const wallet = ethjswallet.fromPrivateKey(hdWalletProvider.wallets[hdWalletProvider.addresses[0]].getPrivateKey());
        // const password = 'temp-password';
        // const keystore = wallet.toV3(password);
        // let account = accounts.decrypt(keystore, password);
        // let sig = account.sign(hash);
        // console.log('sig is ' + sig.signature);

        let signer = accounts.recover(this.message, this.signature);
        console.log('signer is ' + signer);
        this.signaturesMatch = signer.toLowerCase() === this.orgId.toLowerCase();

      }
    }
  };
</script>

<style scoped>
</style>
