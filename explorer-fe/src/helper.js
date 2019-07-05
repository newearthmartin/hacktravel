import { WtJsLibs } from '@windingtree/wt-js-libs';
import InMemoryAdapter from '@windingtree/off-chain-adapter-in-memory';

export default {
    getLibs() {
       return WtJsLibs.createInstance({
            onChainDataOptions: {
              provider: this.getProvider(),
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

    getProvider(){
      return 'https://ropsten.infura.io/v3/7714245c4ea74010879bda16618931c9';
    },

    getWeb3(){

    }
}
