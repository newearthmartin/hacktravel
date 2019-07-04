import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import ExplorerDetails from './views/ExplorerDetails.vue'

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/explorer/:orgId',
      name: 'explorerDetails',
      component: ExplorerDetails
    },
    {
      path: '/',
      name: 'home',
      component: Home,
    }
  ],
});
