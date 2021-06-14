<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="290">
      <template v-slot:activator="{ on, attrs }">
        <v-btn depressed v-bind="attrs" v-on="on" style="height: 100%">
          등록하기
        </v-btn>
      </template>
      <v-card>
        <v-card-title class="text-h5"> 등록하시겠습니까? </v-card-title>
        <v-card-text>{{ item.title }}</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" text @click="$emit('register', item)">
            YES
          </v-btn>
          <v-btn color="green darken-1" text @click="dialog = false">
            NO
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
export default {
  props: ["item"],
  data() {
    return {
      dialog: false,
    };
  },
};
</script>
