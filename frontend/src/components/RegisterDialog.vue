<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="290">
      <template v-slot:activator="{ on, attrs }">
        <v-btn depressed v-bind="attrs" v-on="on" style="height: 100%">
          등록하기
        </v-btn>
      </template>
      <v-card v-if="registering">
        <v-card-title class="text-h5">등록중입니다...</v-card-title>
        <v-card-text>
          <div class="text-center">
            <v-progress-circular
              indeterminate
              color="primary"
            ></v-progress-circular>
          </div>
        </v-card-text>
      </v-card>
      <v-card v-else>
        <v-card-title class="text-h5">등록하시겠습니까? </v-card-title>
        <v-card-text>{{ item.title }}</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" text @click="register(item)">
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
const axios = require("axios");
export default {
  props: ["item"],
  methods: {
    register(item) {
      console.log(item);
      this.registering = true;
      const vm = this;
      axios
        .post("/api/register", item)
        .then(function () {
          vm.dialog = false
          vm.registering = false
          vm.$emit('registered')
        })
        .catch(function (error) {
          vm.registering = false
          console.log(error);
        });
    },
  },
  data() {
    return {
      dialog: false,
      registering: false,
    };
  },
};
</script>
