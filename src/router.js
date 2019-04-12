import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import PageLayout from './layouts/PageLayout.vue';
import Products from './views/Products.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'layout',
      component: PageLayout,
      children: [
        {
          path: '/home',
          name: 'home',
          alias: '',
          component: Home,
        },
        {
          path: '/products',
          name: 'products',
          component: Products
        }
      ],
    },
    {
      path: '/about',
      name: 'about',
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue'),
    },
  ],
});
