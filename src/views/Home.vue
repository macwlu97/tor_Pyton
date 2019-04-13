<template>
  <section>
    <v-container grid-list-xl>
      <v-layout row wrap>
        <v-flex d-flex xs12 md3 v-for="item in items" :key="item.id">
          <v-card hover :to="{name: 'Product', params: {id: item.id, item: item}}" >
            <v-card-media>
              <v-img v-if="item.images[0]" :src="item.images[0].url" height="200px" />
            </v-card-media>
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
    type: Boolean
  },
  items: {
    type: Object
  }
  },
  methods: {
    add_product(item_id) {
      this.$emit('data', item_id);

    }
  }
};
</script>

