<template>
  <div>
    <v-text-field
      class="mx-4"
      flat
      hide-details
      label="Search"
      prepend-inner-icon="mdi-magnify"
      solo-inverted
    ></v-text-field>
    <v-row dense class="mt-2">
      <v-col v-for="(item, i) in articles" :key="i" cols="12">
        <v-card>
          <v-card-text>
            <div>
              <b>{{ item.title }}</b>
            </div>
            {{ item.content }}
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      articles: [
        {
          title: "Hello 1----------------------------------",
          content:
            "This pattern can be used when you need a toolbar, a responsive drawer and content to be displayed following the Material ",
        },
        {
          title: "Hello 2",
          content:
            "This pattern can be used when you need a toolbar, a responsive drawer and content to be displayed following the Material ",
        },
        {
          title: "Hello",
          content:
            "This pattern can be used when you need a toolbar, a responsive drawer and content to be displayed following the Material ",
        },
        {
          title: "Hello 1",
          content:
            "This pattern can be used when you need a toolbar, a responsive drawer and content to be displayed following the Material ",
        },
        {
          title: "Hello 2",
          content:
            "This pattern can be used when you need a toolbar, a responsive drawer and content to be displayed following the Material ",
        },
        {
          title: "Hello",
          content:
            "This pattern can be used when you need a toolbar, a responsive drawer and content to be displayed following the Material ",
        },
        {
          title: "Hello 1",
          content:
            "This pattern can be used when you need a toolbar, a responsive drawer and content to be displayed following the Material ",
        },
        {
          title: "Hello 2",
          content:
            "This pattern can be used when you need a toolbar, a responsive drawer and content to be displayed following the Material ",
        },
        {
          title: "Hello",
          content:
            "This pattern can be used when you need a toolbar, a responsive drawer and content to be displayed following the Material ",
        },
        {
          title: "Hello 1",
          content:
            "This pattern can be used when you need a toolbar, a responsive drawer and content to be displayed following the Material ",
        },
        {
          title: "Hello 2",
          content:
            "This pattern can be used when you need a toolbar, a responsive drawer and content to be displayed following the Material ",
        },
        {
          title: "Hello",
          content:
            "This pattern can be used when you need a toolbar, a responsive drawer and content to be displayed following the Material ",
        },
      ],
    };
  },
};
</script>
