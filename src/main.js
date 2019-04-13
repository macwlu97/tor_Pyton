import Vue from 'vue';
import axios from 'axios';
import App from './App.vue';
import router from './router';
import store from './store';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';
import VueSocketIO from 'vue-socket.io';

Vue.prototype.$http = axios;
Vue.use(Vuetify);
Vue.prototype.$status = false;
Vue.use(new VueSocketIO({
    debug: true,
    connection: 'http://localhost:5000',
}));
Vue.config.productionTip = false;

new Vue({
  sockets: {
        connect: function () {
        },
        deliver_success: function (data) {
            alert('twoje zamowienie jest w drodze');
        },
        status_success(data) {
            Vue.prototype.$status = true;
        },
  },
  router,
  store,
  render: h => h(App),
}).$mount('#app');
