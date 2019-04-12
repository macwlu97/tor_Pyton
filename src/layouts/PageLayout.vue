<template>
  <v-app light>
    <v-toolbar app class="white">
      <v-toolbar-title class="pr-4 text-lowercase orange--text">PYTON_DELIVER</v-toolbar-title>
      <v-form>
        <v-text-field solo flat color="orange" hide-details label="Search" width="100"/>
      </v-form>

      <v-spacer/>

      <v-toolbar-items>
        <v-menu v-model="chart" :close-on-content-click="false" :nudge-width="200" offset-x>
          <template v-slot:activator="{ on }">
            <v-btn flat v-on="on">
              <v-icon>shopping_cart</v-icon>
            </v-btn>
          </template>
          <v-card>
            <v-card-text>{{ items }}</v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>

              <v-btn flat @click="chart = false">Cancel</v-btn>
              <v-btn color="primary" flat @click="chart = false">Save</v-btn>
            </v-card-actions>
          </v-card>
        </v-menu>
      </v-toolbar-items>
    </v-toolbar>

    <v-content>
      <v-container fluid>
        <router-view @data="add_to_cart"></router-view>
      </v-container>
    </v-content>
    <v-footer></v-footer>
  </v-app>
</template>

<script>
export default {
  name: "PageLayout",
  data() {
    return {
      items: [],
      chart: false,
      providers_status: true
    };
  },
  mounted() {
    // let config = {
    //   headers: {
    //     Authorization: "Bearer " + this.validToken()
    //   }
    // };

    this.$http.get("http://localhost:5000/api/v1/status").then(response => {
      this.providers_status = !!response.data.status ? true : false;
    });

    // this.$http.get('https://api.allegro.pl/offers/listing?pharse=kappa').then(response => {
    //   console.log(response.data)
    // }).catch(error => {
    //   console.log(error.response.data)
    // })
  },
  methods: {
    add_to_cart(data) {
      this.items.push(data);
    },
    validToken() {
      const clientId = "d1814501b48143de85db0e7ece241ffd";
      const ClientSecret =
        "peC9cxZRv0M9li1LZQkKalcpLqNkQvDOZtzHjpODPiiBItpJruyppTPVMnRd1dqm";
      let config = {
        headers: {
          Authorization: `Basic base64(${clientId}:${ClientSecret})`
        }
      };

      this.$http
        .get(
          "https://allegro.pl/auth/oauth/token?grant_type=client_credentials",
          config
        )
        .then(response => {
          console.log(respopnse.data);
        });
    }
  }
};
</script>

<style scoped>
</style>