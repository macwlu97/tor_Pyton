<template>
  <v-app light>
    <v-toolbar app class="white">
      <v-toolbar-title class="pr-4 text-lowercase orange--text">
        PYTON_DELIVER
        </v-toolbar-title>
      <v-form @submit="search()" onSubmit="return false;">
        <v-text-field v-model="searchValue" solo flat color="orange" hide-details label="Search" width="100"/>
      </v-form>

      <v-spacer/>

      <v-toolbar-items>
        <v-menu v-model="chart" :close-on-content-click="false" :nudge-width="200" offset-x>
          <template v-slot:activator="{ on }">
            <v-btn flat v-on="on">
              <v-icon>shopping_cart</v-icon>
            </v-btn>
          </template>
          <v-card v-for="i in chartItems" :key="i">
            <v-flex xs12 md3>
            </v-flex>
            <v-flex xs12 md9>
                <v-card-text>
                  <p>Eiusmod velit deserunt magna do laboris dolore eu mollit.</p>
                </v-card-text>
                <v-card-actions>
                  <v-btn flat @click="removeFromChart(i)"><v-icon>remove</v-icon></v-btn>
                </v-card-actions>
            </v-flex>
          </v-card>
          <v-divider />
          <v-card> 
            <v-card-actions>
              <v-spacer></v-spacer>

              <v-btn flat @click="chart = false">Cancel</v-btn>
              <v-btn color="primary" flat @click="send_deliver_to_bus()">Buy Now</v-btn>
            </v-card-actions>
          </v-card>
        </v-menu>
      </v-toolbar-items>
    </v-toolbar>

    <v-content>
      <v-container fluid>
        <router-view :items="items" :providers_status="providers_status" @data="add_to_cart"></router-view>
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
      chartItems: [],
      chart: false,
      providers_status: false,
      items: {},
      searchValue: '',
    };
  },
  mounted() {
    this.$store.dispatch('status').then(response => {
      console.log(response)
      this.providers_status = response.data.status;
    })
    this.$store.dispatch('search', "czerwony").then(response => {
      this.items = response.data.items.regular;
    })
  },
  methods: {
    add_to_cart(data) {
      this.chartItems.push(data);
    },
    send_deliver_to_bus() {
      this.$http
        .post("http://localhost:5000/api/v1/deliver", { id: 1 })
        .then(response => {
          alert(response.data);
        });
    },
    removeFromChart(data) {
      this.chartItems.pop(data);
    },
    search() {
      this.$store.dispatch('search', this.searchValue).then(response => {
      this.items = response.data.items.regular;
      this.$router.push("/products");
    })
      
    },
  }
};
</script>

<style scoped>
</style>