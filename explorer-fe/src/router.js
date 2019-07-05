import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import Explore from './views/Explore.vue'
import CreateOrgID from './views/CreateOrgID.vue'

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/explore/:orgId',
      name: 'explore',
      component: Explore
    },
    {
      path: '/createOrgID',
      name: 'createOrgID',
      component: CreateOrgID
    },
  ],
});
