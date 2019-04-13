<template>
  <div>
    <v-container grid-list-md>
      <v-layout row wrap>
        <v-flex md3 hidden-xs>
          <v-card>  
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
          </v-card>
        </v-flex>
        <v-flex xs12 md9>
          <v-layout row wrap>
            <v-flex xs12 v-for="i in 40" :key="i">
              <v-card hover class="py-2" :to="{name: 'Product', params: {id: i}}" > 
                <v-layout row wrap>
                  <v-flex xs12 md3>
                    <v-card-media>
                      <div class="product-image"/>
                    </v-card-media>
                  </v-flex>
                  <v-flex xs12 md9>
                    <v-card-text class="pt-2 pb-0">
                      <p class="mb-0">Excepteur sit irure occaecat tempor eu exercitation nisi sint id fugiat. Ipsum cupidatat Lorem cupidatat aliquip. Excepteur tempor nisi quis incididunt sunt quis nisi mollit deserunt.</p>
                    </v-card-text>
                    <v-card-title class="py-0">
                      <h5 class="title">170zł</h5>
                    </v-card-title>
                    <v-card-actions class="py-1">
                      <v-btn small color="error">
                        <v-icon>add_shopping_cart</v-icon>Get this product in: 30 min!
                      </v-btn>
                    </v-card-actions>
                  </v-flex>
                </v-layout>
              </v-card>
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "Products"
};
</script>

<style scoped>
</style>