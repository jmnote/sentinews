<template>
  <div>
    <v-row dense class="mt-2">
      <v-col v-for="(item, i) in articles" :key="i" cols="12">
        <v-card>
          <v-card-text>
            <div>
              <b>{{ item.title }}</b>
            </div>
            {{ item.desc }}
          </v-card-text>
          <v-layout justify-center>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="green darken-1" text>
                자세히 보기
              </v-btn>
            </v-card-actions>
          </v-layout>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
const axios = require("axios");
export default {
  data() {
    return {
      articles: [],
    };
  },
  mounted() {
    const vm = this;
    axios.get("/api/articles").then(function (response) {
      vm.articles = response.data;
    });
  },
};
</script>
