<template>
  <section>
    <v-container grid-list-xl>
      <v-layout row wrap>
        <v-flex d-flex xs12 md3 v-for="item in items" :key="item.id">
          <v-card hover  >
            <v-card-media>
              <v-img v-if="item.images[0]" :src="item.images[0].url" height="200px" />
              <v-img v-else src="https://www.pcgamesn.com/wp-content/uploads/2018/10/gabe_newell_meme-580x334.jpg" height="200px" />
            </v-card-media>
            <v-card-actions class="py-2">
              <v-btn v-if="providers_status" small color="success" class="elevation-0 text-capitalize" @click="add_product(item)">
                <v-icon small class="pr-1">add_shopping_cart</v-icon>Dostępne już za godzine!
              </v-btn>
            </v-card-actions>
            <v-card-title class="py-1">
              <h5 class="title">{{ item.sellingMode.price.amount}} {{ item.sellingMode.price.currency}}</h5>
            </v-card-title>
            <v-card-text class="py-0">
              <p class="mb-0">{{ item.name.substring(0,20) }}</p>
            
            </v-card-text>
            
            <v-card-actions class="pt-0">
                <v-btn flat class="mx-0" block small :to="{name: 'Product', params: {id: item.id, item: item}}">View</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </section>
</template>

<script>
export default {
  name: "home",
  props: { 
    providers_status: {
    type: String
  },
  items: {
    type: Array
  }
  },
  methods: {
    add_product(item) {
      this.$emit('data', item);

    }
  }
};
</script>

