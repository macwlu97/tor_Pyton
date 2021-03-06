import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import PageLayout from './layouts/PageLayout.vue';
import Products from './views/Products.vue';
import Product from './views/Product.vue';
import Tracking from './views/Tracking.vue';

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
          name: 'Home',
          alias: '',
          component: Home,
        },
        {
          path: '/products',
          name: 'Products',
          component: Products
        },
        {
          props: true,
          path: '/product/:id',
          name: 'Product',
          component: Product
        },
      ],
    },
    {
      path: '/tracking',
      name: 'tracking',
      component: Tracking,
    },
  ],
});
