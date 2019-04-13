<template>
  <div>
    <v-container grid-list-md>
      <v-layout row wrap>
        <v-flex md3 hidden-xs>
          <v-card>
            <h4 class="pt-2 ml-2 font-weight-regular">Kategorie:</h4>
            <v-list dense>
              <v-list-tile v-for="item in categories.categories.subcategories" :key="item">
                <v-list-tile-content>{{item.name}}</v-list-tile-content>
              </v-list-tile>
            </v-list>
          </v-card>
        </v-flex>
        <v-flex xs12 md9>
          <v-layout row wrap>
            <v-flex class="mb-2" xs12 v-for="item in items" :key="item.id">
              <v-card hover>
                <v-layout row wrap>
                  <v-flex xs12 md3>
                    <v-responsive>
                      <v-img :src="item.images[0].url" height="200px"/>
                    </v-responsive>
                  </v-flex>
                  <v-flex xs12 md9>
                    <v-card-actions class="py-1">
                      <v-btn
                        v-if="providers_status"
                        small
                        color="success"
                        class="text-capitalize elevation-0"
                        @click="add_product(item)"
                      >
                        <v-icon small class="pr-1">add_shopping_cart</v-icon>U ciebie już za godzine!
                      </v-btn>
                    </v-card-actions>
                    <v-card-title class="py-1">
                      <h5
                        class="title"
                      >{{ item.sellingMode.price.amount}} {{ item.sellingMode.price.currency}}</h5>
                    </v-card-title>
                    <v-card-text class="py-0">
                      <p>{{ item.name }}</p>
                    </v-card-text>
                    <v-card-actions>
                      <v-btn
                        flat
                        small
                        :to="{name: 'Product', params: {id: item.id, item: item}}"
                      >View</v-btn>
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
  name: "Products",
  props: {
    providers_status: {
      type: String
    },
    items: {
      type: Array
    },
    categories: {
      type: Object
    }
  },
  methods: {
    add_product(item) {
      this.$emit("data", item);
    }
  },
};
</script>

<style scoped>
</style>