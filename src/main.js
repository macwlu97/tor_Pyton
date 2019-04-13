import Vue from 'vue';
import axios from 'axios';
import Vuetify from 'vuetify';
import App from './App.vue';
import router from './router';
import store from './store';
import 'vuetify/dist/vuetify.min.css';
import VueSocketIO from 'vue-socket.io';
import VueSweetalert2 from 'vue-sweetalert2';

Vue.use(VueSweetalert2);
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
    connect() {
    },
    deliver_success(data) {
      this.$swal({
        title: 'Przyjęto do realizacji',
        text: 'Twoja paczka jest w drodze!',
        type: 'success',
        footer: "<a href='/tracking'>Śledź przesyłkę</a>"
      });
    },
    status_success(data) {
      Vue.prototype.$status = true;
    },
  },
  router,
  store,
  render: h => h(App),
}).$mount('#app');
