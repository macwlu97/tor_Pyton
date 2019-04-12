<template>
  <section>
    <v-container grid-list-xl>
      <v-layout row wrap>
        <v-flex xs12 md3 v-for="i in 40" :key="i">
          <v-card hover>
            <v-card-media>
              <div class="product-image"/>
            </v-card-media>
            <v-card-actions class="py-1">
              <v-btn small color="error" @click="add_product(i)">
                <v-icon>add_shopping_cart</v-icon>Get this product in: 30 min!
              </v-btn>
            </v-card-actions>
            <v-card-title class="py-1">
              <h5 class="title">170zł</h5>
            </v-card-title>
            <v-card-text class="py-0">
              <p>Excepteur sit irure occaecat tempor eu exercitation nisi sint id fugiat. Ipsum cupidatat Lorem cupidatat aliquip. Excepteur tempor nisi quis incididunt sunt quis nisi mollit deserunt.</p>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </section>
</template>

<script>
export default {
  props: {
    items: Object
  },
  name: "home",
  methods: {
    add_product(item_id) {
      this.$emit('data', item_id);

    }
  }
};
</script>

<style lang="scss">
.product-image {
  margin: 10px auto;

  display: block;
  width: 100%;
  height: 200px;
  background: #131313;
}
</style>
