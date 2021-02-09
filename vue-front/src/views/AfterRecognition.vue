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
          class="imgbox">hihi</v-img>
      </v-col>
      <v-col
        cols="4"
        class="pr-2 py-2">
        <v-img
          class="imgbox mb-2">hihi</v-img>
        <v-img
          class="imgbox">hihi</v-img>
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