<template>
  <div id="app">
    <v-app>
      <v-main>
        <v-toolbar color="cyan" dark flat>
          <v-app-bar-nav-icon></v-app-bar-nav-icon>

          <v-toolbar-title>감성뉴스</v-toolbar-title>

          <v-spacer></v-spacer>

          <v-btn icon>
            <v-icon>mdi-magnify</v-icon>
          </v-btn>

          <v-btn icon>
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
          <template v-slot:extension>
            <v-tabs v-model="tab" centered grow>
              <v-tabs-slider></v-tabs-slider>
              <v-tab v-for="item in items" :to="item.to" :key="item.icon">
                <v-icon>mdi-{{ item.icon }}</v-icon>&nbsp;{{ item.text }}
              </v-tab>
            </v-tabs>
          </template>
        </v-toolbar>
        <v-container>
          <router-view />
        </v-container>
      </v-main>
    </v-app>
  </div>
</template>


<script>
//import Search from './Search';
//import List from './List';

export default {
  data() {
    return {
      tab: null,
      items: [
        {
          icon: "magnify",
          to: "/",
          text: "검색",
        },
        {
          icon: "format-list-bulleted",
          to: "/list",
          text: "목록",
        },
        {
          icon: "star",
          to: "/star",
          text: "책갈피",
        },
      ],
    };
  },
};
</script>