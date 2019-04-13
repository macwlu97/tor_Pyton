<template>
  <div>
    <v-container grid-list-md>
      <v-card class="white">
        <v-layout row wrap>
          <v-flex xs12 md7>
            <div class="product-image"/>
          </v-flex>
          <v-flex xs12 md5>
            <v-card flat>
              <v-card-title>Product Name</v-card-title>
              <v-card-text class="py-0">1600zł</v-card-text>
              <v-card-actions>
                <v-btn v-if="providers_status" small color="error" @click="add_product(this.$route.params.id)">
                  <v-icon>add_shopping_cart</v-icon>Get this product in: 30 min!
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-card>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "Product",
  props: {
    providers_status: {
      type: Boolean
    }
  },
  methods: {
    add_product(item_id) {
      this.$emit("data", item_id);
    }
  }
};
</script>

<style scoped>
</style>