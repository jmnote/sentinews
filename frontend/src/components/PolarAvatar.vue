<template>
  <v-avatar :color="color" size="36">
    <span class="white--text text-h5">{{ number }}</span>
  </v-avatar>
</template>

<script>
export default {
  props: ["polarity"],
  computed: {
    number: function () {
      return Math.round(100 * this.polarity);
    },
    color: function () {
        let r, g, b;
        const intensity = Math.abs(this.polarity);
        if( this.polarity > 0 ) {
            r = 60;
            g = Math.min(200,100+intensity*400);
            b = 60;
        }
        else if( this.polarity == 0 ) {
            r = g = b = 60;
        }
        else {
            r = Math.min(200,100+intensity*400);
            g = 60;
            b = 60;
        }
        return "rgb("+r+","+g+","+b+")";
    },
  },
};
</script>

