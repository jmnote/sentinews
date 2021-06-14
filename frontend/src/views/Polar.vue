<template>
  <div>
    <v-row justify="center" class="mt-2">
      <v-expansion-panels focusable>
        <v-expansion-panel v-for="(item, i) in articles" :key="i">
          <v-expansion-panel-header>
            <div>
            <div><b>{{ item.title }}</b></div>
            <div><small>{{ item.desc }}</small></div>
            </div>
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <div style='white-space: pre;white-space: break-spaces;'>
              {{ item.content.replace(/\n\s*\n/g, '\n') }}
            </div>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-row>
  </div>
</template>

<script>
const axios = require("axios");
export default {
  data() {
    return {
      articles: [],
      shows: [],
    };
  },
  mounted() {
    const vm = this;
    axios.get("/api/polars").then(function (response) {
      vm.articles = response.data;
      vm.articles.forEach((e) => (e.show = false));
      console.log(vm.articles);
    });
  },
};
</script>
