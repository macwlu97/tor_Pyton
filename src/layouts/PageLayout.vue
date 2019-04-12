<template>
  <v-app light>
    <v-toolbar app class="white">
      <v-toolbar-title class="pr-4 text-lowercase orange--text">PYTON_DELIVER</v-toolbar-title>
       <v-text-field solo flat color="orange" hide-details label="Search" width="100"/>
       <v-spacer />
         
        <v-toolbar-items>
            <v-btn flat><v-icon>shopping_cart</v-icon></v-btn>
        </v-toolbar-items>
    </v-toolbar>

    <v-content>
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-content>
    <v-footer></v-footer>
  </v-app>
</template>

<script>
export default {
  name: "PageLayout"
};
</script>

<style scoped>
</style>