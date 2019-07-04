const ethjswallet = require('ethereumjs-wallet');
const web3 = require('web3-eth-accounts');
const HDWalletProvider = require('truffle-hdwallet-provider');

function getInfuraNodeAddress(networkName, projectid) {
  return `https://${networkName}.infura.io/v3/${projectid}`;
}

function getWeb3Account(provider, keyFile) {
  const accounts = new web3.Accounts(provider, null, {});
  if (keyFile.mnemonic) {
    const hdWalletProvider = new HDWalletProvider(keyFile.mnemonic, provider);
    const wallet = ethjswallet.fromPrivateKey(hdWalletProvider.wallets[hdWalletProvider.addresses[0]].getPrivateKey());
    const password = 'temp-password';
    const keystore = wallet.toV3(password);
    return accounts.decrypt(keystore, password);
  } else if (keyFile.wallet && keyFile.password) {
    return accounts.decrypt(keyFile.wallet, keyFile.password);
  }
}

function getWalletProvider(keyFile, networkName) {
  const provider = getInfuraNodeAddress(networkName, keyFile.infura_projectid);
  if (keyFile.mnemonic) {
    const hdWalletProvider = new HDWalletProvider(keyFile.mnemonic, provider);
    console.info(`Running truffle with default account ${hdWalletProvider.addresses[0]}`);
    return hdWalletProvider;
  } else if (keyFile.wallet && keyFile.password) {
    const accounts = new web3.Accounts(provider, null, {});
    const account = accounts.decrypt(keyFile.wallet, keyFile.password);
    console.info(`Running truffle with default account ${account.address}`);
    return new HDWalletProvider(account.privateKey, provider)
  }
  throw new Error('Either mnemonic or wallet & password are missing in the keys.json');
}

module.exports = {
  getWeb3Account: getWeb3Account,
  getWalletProvider: getWalletProvider,
  getInfuraNodeAddress: getInfuraNodeAddress,
}