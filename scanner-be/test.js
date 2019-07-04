const web3 = require('web3-eth-accounts');
const web3utils = require('web3-utils');
const wtContracts = require('@windingtree/wt-contracts');
const LifDepositAbi = require('@windingtree/trust-clue-lif-deposit/build/contracts/LifDeposit.json');
const truffleContract = require('truffle-contract');
const utils = require('./utils');

const keyFile = require('./keys.json');
const provider = utils.getInfuraNodeAddress('ropsten', keyFile.infura_projectid);
const accounts = web3.Accounts(provider);

