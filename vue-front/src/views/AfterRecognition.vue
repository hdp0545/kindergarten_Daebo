<template>
  <v-container
    style="min-height: 672px"
    class="mt-16 my-main">
    
    <v-row
      class="mx-0 outline">
      <v-col
        cols="8"
        class="px-2 py-2">
        <v-img
          class="imgbox"
          :src="yoloResult.detectPath">hihi</v-img>
      </v-col>
      <v-col
        cols="4"
        class="pr-2 py-2">
        <v-img
          class="imgbox mb-2"
          :src="yoloResult.platePath">hihi</v-img>
        <v-text>
          <h2>"{{ this.ocrText }}"</h2>
        </v-text>
      </v-col>
    </v-row>
    <v-row></v-row>
  
  </v-container>
</template>

<script>
export default {
  name: "AfterRecognition",
  data () {
    return {
    }
  },
  props: {
    yoloResult: {
      type: Object
    },
    ocrText: {
      type: String
    }
  }
}
</script>

<style>
.outline {
  background-color: rgb(245, 247, 249);
}
.imgbox {
  background-color: rgb(232, 235, 240);
}
.col {
  padding: 0;
}
</style>