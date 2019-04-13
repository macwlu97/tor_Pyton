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
            <v-flex xs12 v-for="item in items" :key="item.id">
              <v-card hover>
                <v-layout row wrap>
                  <v-flex xs12 md3>
                     <v-card-media>
                  <v-img v-if="item.images[0]" :src="item.images[0].url" height="200px" />
                </v-card-media>
                    </v-flex>
                    <v-flex xs12 md9>
                      <v-card-actions class="py-1">
                  <v-btn v-if="providers_status" small color="error" @click="add_product(item.id)">
                    <v-icon>add_shopping_cart</v-icon>Get this product in: 30 min!
                  </v-btn>
                </v-card-actions>
                <v-card-title class="py-1">
                  <h5 class="title">{{ item.sellingMode.price.amount}} {{ item.sellingMode.price.currency}}</h5>
                </v-card-title>
                <v-card-text class="py-0">
                  <p>{{ item.name }}</p>
                </v-card-text>
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
  name: "Products",
  props: { 
    providers_status: {
    type: String
  },
  items: {
    type: Array
  }
  },
    methods: {
    add_product(item_id) {
      this.$emit('data', item_id);

    }
  }
};
</script>

<style scoped>
</style>