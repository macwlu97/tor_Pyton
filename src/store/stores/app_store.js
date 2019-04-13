import axios from 'axios';

const API_ENDPOINT = 'http://localhost:5000/api/v1';
const API_ALLEGRO = 'https://api.allegro.pl.allegrosandbox.pl';

const access_token = 'bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NTUxNjIxMTIsInVzZXJfbmFtZSI6IjQ0MTU4NDAyIiwianRpIjoiOTBkYmVlZGMtNzUyZS00ZGYwLTgxZTItZGExMjYyN2M1M2M3IiwiY2xpZW50X2lkIjoiY2U2YjI5ZDdlZjE0NDMxOThiY2UwZDkyZWJlZTQ5MzEiLCJzY29wZSI6WyJhbGxlZ3JvX2FwaSJdfQ.R2Hfu2WJvDjSOblCm0uMYcEMWcx00wMwhX3MPuhLqMAIyRV5bDSaYpL9NBdk52wwFDR4FGWcCsEUACLNqSKDsCJ1FBiTmfspv-zlyOAklChz1nQ8Arkb0VNpv-n5s1in2AdTDtN8z3xJ1g-3gcLKHGF1xrv9NUvS5lFfIWbGJzwmt4HZcglsNgqJLIQjw85ShtBfl9ig7diaga56Ix0cdeR1u3fqoqNPDV2Np6V-s_iUbpsdUDG1uu-gYYbtk_SrPrJJ8QZtPI6qhfbhU9O81wBt7eh4PJCS9QS9qf5X3u9qOKQK75mCZH9GieUYdqEAYZTLMs1yP26RdT777Gn_Gw';
const refresh_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NjI4OTQ5MTIsInVzZXJfbmFtZSI6IjQ0MTU4NDAyIiwianRpIjoiYWYyOGIwOWEtNTJlNi00N2I2LTg2NTAtYmEyODA5MmIzZDAwIiwiY2xpZW50X2lkIjoiY2U2YjI5ZDdlZjE0NDMxOThiY2UwZDkyZWJlZTQ5MzEiLCJzY29wZSI6WyJhbGxlZ3JvX2FwaSJdLCJhdGkiOiI5MGRiZWVkYy03NTJlLTRkZjAtODFlMi1kYTEyNjI3YzUzYzcifQ.AuNhHFWZw4L8qDvVK7rqzpnpSgg2Le51sh5Y8RUB9MbOBDTryzPYCPUA066UZ2f8ttCprLzxUo5Mm4Bdj1IMc81iFL4fTX6ovaGb-oegh8uQL69YGYX8_p4JAcJQ8ebEg9n_9IUpMYeu3lN0q40n4W2By1-ml3NCgElMP3DK0cHfIHQ3njs2qOfP1dq3cuff8HY9gfbaOM4qjcum6kdD26CZ4RLId2sj10ee6VTiVcb9z_qeYmzoCdNdbkcTwLl6vc8eK5EA8XNKFO7BkEUjM5mDHwk6A1A0twfszHsAoIWbih-0WhV-YCVrSnBBPXCaeUpTMepi5ePrRc_n8gaRwg';

const AppStore = {
  state: {
    one: {},
    many: {},
    status: '',
    error: '',
  },
  mutations: {
    one_success(state, data) {
      state.one = data;
    },
    many_success(state, data) {
      state.many = data;
    },
    error(state) {
      state.error = 'Error';
    },
    status(state) {
      state.status = true;
    },
  },
  actions: {
    status({ commit }) {
      return new Promise((resolve, reject) => {
        axios.get(`${API_ENDPOINT}/status`)
          .then((response) => {
            commit('status');
            resolve(response);
          })
          .catch((err) => {
            commit('error');
            reject(err);
          });
      });
    },
    getProducts({ commit }) {
      return new Promise((resolve, reject) => {
        axios.defaults.headers.common.Authorization = access_token;
        axios.defaults.headers.common.Accept = 'application/vnd.allegro.public.v1+json';
        axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
        axios.get(`${API_ALLEGRO}/offers/listing?phrase=czerwona+sukienka`)
          .then((response) => {
            commit('many', response.data);
            resolve(response);
          })
          .catch((err) => {
            commit('error');
            reject(err);
          });
      });
    },
  },

};

export default AppStore;
