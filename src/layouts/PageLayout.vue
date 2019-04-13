<template>
  <v-app light>
    <v-toolbar flat app class="white elevation-1">
      <v-toolbar-title class="pr-5 text-lowercase allegro_orange__text">PYTON_DELIVER</v-toolbar-title>
      <v-form @submit="search()" onSubmit="return false;" class="elevation-1" flat>
        <v-text-field v-model="searchValue" solo flat color="orange" hide-details label="Search"/>
      </v-form>

      <v-spacer/>
      <v-toolbar-items>
        <v-menu v-model="chart" :close-on-content-click="false" :nudge-width="200" offset-x>
          <template v-slot:activator="{ on }">
            <v-btn flat v-on="on">
              <v-badge v-if="chartItems.length > 0" color="allegro_orange" right>
                <template v-slot:badge>
                  <span>{{ chartItems.length }}</span>
                </template>
                <v-icon>shopping_cart</v-icon>
              </v-badge>
               <v-icon v-else>shopping_cart</v-icon>
            </v-btn>
          </template>
          <v-card v-for="item in chartItems" :key="item.id">
            <v-layout row wrap>
              <v-flex xs12 md3>
                <v-card-media class="pa-2">
                  <v-img v-if="item.images[0]" :src="item.images[0].url" height="70px"/>
                  <v-img
                    v-else
                    src="https://www.pcgamesn.com/wp-content/uploads/2018/10/gabe_newell_meme-580x334.jpg"
                    height="70px"
                  />
                </v-card-media>
              </v-flex>
              <v-flex xs12 md7>
                <v-card-text>
                  <p>{{item.name}}</p>
                </v-card-text>
              </v-flex>
              <v-flex xs12 md2>
                <v-btn flat icon @click="removeFromChart(item)">
                  <v-icon>remove</v-icon>
                </v-btn>
              </v-flex>
            </v-layout>
          </v-card>
          <v-divider/>
          <v-card>
            <v-card-actions>
              <v-spacer />

              <v-btn flat @click="chart = false">Cancel</v-btn>
              <v-btn dark class="allegro_orange" flat @click="send_deliver_to_bus()">Buy Now</v-btn>
               <v-spacer />


            </v-card-actions>
          </v-card>
        </v-menu>
      </v-toolbar-items>
    </v-toolbar>

    <v-content>
      <v-container fluid>
        <router-view :categories="categories" :items="items" :providers_status="this.$status" @data="add_to_cart"></router-view>
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
      categories: {},
      items: {},
      searchValue: ""
    };
  },
  mounted() {
    this.$socket.emit("status");
    this.$store.dispatch("search", "czerwony").then(response => {
      this.items = response.data.items.regular;
      this.categories = response.data;
    });
  },
  methods: {
    add_to_cart(data) {
      this.chartItems.push(data);
    },
    send_deliver_to_bus() {
      this.$socket.emit("deliver");
    },
    removeFromChart(data) {
      this.chartItems.pop(data);
    },
    search() {
      this.$store.dispatch("search", this.searchValue).then(response => {
        this.items = response.data.items.regular;
        this.categories = response.data;
        this.$router.push("/products");
      });
    }
  }
};
</script>

<style lang="scss">
.allegro_orange {
  background: #ff5a00;
  &__text {
    color: #ff5a00;
  }
}
</style>