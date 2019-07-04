const web3 = require('web3-eth-accounts');
const web3utils = require('web3-utils');
const wtContracts = require('@windingtree/wt-contracts');
const LifDepositAbi = require('@windingtree/trust-clue-lif-deposit/build/contracts/LifDeposit.json');
const truffleContract = require('truffle-contract');

const keyFile = require('./keys.json');
const provider = utils.getInfuraNodeAddress('ropsten', keyFile.infura_projectid);
const accounts = web3.Accounts(provider);

(async () => {
  // decoding
  const actualSigner = accounts.recover(receivedThis.claim, receivedThis.signature);
  const decodedClaim = JSON.parse(web3utils.hexToUtf8(receivedThis.claim));
  console.log({
    signedBy: actualSigner,
    subject: decodedClaim.subject,
    guarantor: decodedClaim.guarantor,
    expiresAt: new Date(decodedClaim.expiresAt * 1000),
  });

  const OrgContract = truffleContract(wtContracts.OrganizationContract);
  OrgContract.setProvider(provider);
  const Organization = await OrgContract.at(decodedClaim.subject);
  console.log(`Is ${actualSigner} an associated key of ${decodedClaim.subject}?`, await Organization.hasAssociatedKey(actualSigner) );
  const LifDepositContract = truffleContract(LifDepositAbi);
  LifDepositContract.setProvider(provider);
  const lifDeposit = await LifDepositContract.at('0x39af806825B81342D51980E2AD96B7A75Ab31CDa');
  console.log(`How much LIF had the ${actualSigner} deposited?`, (await lifDeposit.getDepositValue(actualSigner)).toString());
  console.log(`How much LIF had the ${decodedClaim.subject} deposited?`, (await lifDeposit.getDepositValue(decodedClaim.subject)).toString());
  process.exit(0);
})();
