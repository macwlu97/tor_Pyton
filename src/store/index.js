import Vue from 'vue';
import Vuex from 'vuex';
import AppStore from './stores/app_store';

Vue.use(Vuex);

const store = new Vuex.Store({
  modules: {
    AppStore,
  },
});

export default store;
