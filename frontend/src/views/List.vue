<template>
  <div>
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
      articles: [],
    };
  },
  mounted() {
    //axios.
  }
};
</script>
