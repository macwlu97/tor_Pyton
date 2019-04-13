import Vue from 'vue';
import axios from 'axios';
import App from './App.vue';
import router from './router';
import store from './store';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';
import VueSocketIO from 'vue-socket.io'

Vue.prototype.$http = axios;
Vue.use(Vuetify);

Vue.use(new VueSocketIO({
    debug: true,
    connection: 'http://localhost:5000',
}))

Vue.config.productionTip = false;

new Vue({
  sockets: {
        connect: function () {
            // console.log('socket connected')
        },
        deliver_success: function (data) {
            alert('twoje zamowienie jest w drodze')
        },
  },
    methods: {
      makeDeliver(data) {
          // $socket is socket.io-client instance
          this.$socket.emit('emit_method', data)
      }
  },
  router,
  store,
  render: h => h(App),
}).$mount('#app');
