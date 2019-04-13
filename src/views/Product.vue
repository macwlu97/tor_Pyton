<template>
  <div>
    <v-container grid-list-md>
      <v-card class="white">
        <v-layout row wrap>
          <v-flex xs12 md7>
            <v-img v-if="it.images[0]" :src="it.images[0].url" height="200px" />
          </v-flex>
          <v-flex xs12 md5>
            <v-card flat>
              <v-card-title>{{ it.name}}</v-card-title>
              <v-card-text class="py-0">{{ it.sellingMode.price.amount}} {{ it.sellingMode.price.currency}}</v-card-text>
              <v-card-actions>
                <v-btn v-if="providers_status" small color="error" @click="add_product(it.id)">
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
    },
  },
  data(){
    return {
      it: {} ,
    };
  },
  mounted(){
    if(this.$route.params.item) {
      localStorage.setItem('item', JSON.stringify(this.$route.params.item));
    }
    this.it = JSON.parse(localStorage.getItem('item'));
    
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