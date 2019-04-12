<template>
  <v-app light>
    <v-toolbar app class="white">
      <v-toolbar-title class="pr-4 text-lowercase orange--text">PYTON_DELIVER</v-toolbar-title>
      <v-text-field solo flat color="orange" hide-details label="Search" width="100"/>
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
      chart: false
    };
  },
  mounted() {
    ajax
  },
  methods: {
    add_to_cart(data) {
      this.items.push(data);
    }
  }
};
</script>

<style scoped>
</style>