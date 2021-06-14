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
                  @register="register"
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
    register(item) {
      //const vm = this;
      axios
        .post("/api/register", item)
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          // handle error
          console.log(error);
        });
    },
  },
  data() {
    return {
      keyword: "",
      articles: [
        {
          title: "hello",
          desc: "바른미래당, 경남도당 공동위원장에 안성오 임명",
          url: "url1",
        },
        {
          title: "hello",
          desc: "바른미래당, 경남도당 공동위원장에 안성오 임명",
          url: "url2",
        },
        {
          title: "hello",
          desc: "바른미래당, 경남도당 공동위원장에 안성오 임명",
          url: "url3",
        },
        {
          title: "hello",
          desc: "바른미래당, 경남도당 공동위원장에 안성오 임명",
          url: "url4",
        },
      ],
    };
  },
};
</script>
