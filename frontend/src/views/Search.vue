<template>
  <div>
    <v-text-field
      class="mx-4"
      flat
      hide-details
      label="Search"
      prepend-inner-icon="mdi-magnify"
      solo-inverted
      v-model="keyword"
      @keydown.enter="search"
    ></v-text-field>
    <v-row dense class="mt-2">
      <v-col v-for="(item, i) in articles" :key="i" cols="12">
        <v-card>
          <v-card-text>
            <div style="display: flex">
              <div style="flex-grow: 1" class="mr-2">
                <b>{{ item.title }}</b>
                <div>
                  {{ item.desc }}
                </div>
              </div>
              <div style="display: flex">
                <RegisterDialog
                  v-bind:item="item"
                  @registered="registered"
                ></RegisterDialog>
              </div>
            </div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
const axios = require("axios");
import RegisterDialog from "@/components/RegisterDialog.vue";

export default {
  components: {
    RegisterDialog,
  },
  methods: {
    search() {
      const vm = this;
      axios.get(`/api/search/${vm.keyword}`).then(function (response) {
        vm.articles = response.data.list;
      });
    },
    registered() {
      console.log('registered')
      this.$router.push({ name: 'List' })
    },
  },
  data() {
    return {
      keyword: "",
      articles: [],
    };
  },
};
</script>
