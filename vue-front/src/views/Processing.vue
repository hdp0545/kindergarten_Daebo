<template>
  <v-container
    style="min-height: 600px; max-height:600px;"
    class="mt-16 my-main">
    <v-row
      justify='center'>
      <div>
      <h1 class="bold">
        Processing
      </h1>
      </div>
    </v-row>
    <v-row
      justify='center'>
      <hr
        class="mt-1"
        width="110px"
        size="1pt"
        color="black"
        text-align="center">
    </v-row>
    <v-row
      justify="space-around"
      class=" mt-4 pt-10">
      <v-col
        v-for="howToCard in howToCards"
        :key="howToCard.step"
        cols="3">
        <v-card
          class="mx-2"
          flat
          justify=center>
          <v-card-text
            class="mt-n2 px-0">
            <pre><center>{{howToCard.information}}</center></pre>
          </v-card-text>
          <v-img
            :src="howToCard.src">
          </v-img>
        </v-card>
      </v-col>
    </v-row>

  </v-container>
</template>

<script>
export default {
  name: 'Processing',
  data () {
    return {
      imageUrl: '',
      howToCards: [
        {
          step: 1,
          src: require("../img/page_converter/work_step1.png"),
          information: "[Upload] Drag&Drop"
        },
        {
          step: 2,
          src: require("../img/page_converter/work_step2.png"),
          information: "[Detection] YOLO"
        },
        {
          step: 3,
          src: require("../img/page_converter/work_step3.png"),
          information: "[Recognition] OCR"
        },
        {
          step: 4,
          src: require("../img/page_converter/work_step4.png"),
          information: "[Show] Output"
        },
      ],
    }
  },
}
</script>

<style>

</style>