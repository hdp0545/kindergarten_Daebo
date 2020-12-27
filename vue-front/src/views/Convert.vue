<template>
  <v-container
    style="min-height: 800px"
    class="mt-16">
    <v-row
      justify='center'>
      <div>
      <h1>
        Converter
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

    <v-row>
      <v-img :src="imageUrl"></v-img>
    </v-row>
    <v-row>
      <upload-box
        @select-file="selectFile"
        @submit-upload-data="uploadFile"
      ></upload-box>
    </v-row>
    <v-row
      justify="center">
      <h2>
        How to Use WALL·E Converter
      </h2>
    </v-row>
    <v-row
      justify="space-around"
      class="mt-16">
      <v-col
        v-for="howToCard in howToCards"
        :key="howToCard.step"
        cols="3">
        <v-card
          class="px-5"
          flat
          justify=center>
          <v-img
            :src="howToCard.src">
          </v-img>
          <v-card-text
            class="mt-5 px-0">
            {{howToCard.information}}
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import UploadBox from '../components/UploadBox.vue'
export default {
  name: "Convert",
  components: {
    UploadBox
  },
  data () {
    return {
      imageUrl: '',
      howToCards: [
        {
          step: 1,
          src: require("../img/page_converter/step1.png"),
          information: "1. 고화질로 변환하고 \n인식하고자 하는 이미지 업로드"
        },
        {
          step: 2,
          src: require("../img/page_converter/step2.png"),
          information: "2. 화질 변환 과정 진행\n(약 1분 정도 소요)"
        },
        {
          step: 3,
          src: require("../img/page_converter/step3.png"),
          information: "3. 고화질 이미지 확인 및\n다운로드 가능"
        },
        {
          step: 4,
          src: require("../img/page_converter/step4.png"),
          information: "4. 차량번호판을 인식한\n텍스트 화면 출력"
        },
      ],
    }
  },
  methods: {
    selectFile(selectedFile) {
      this.imageUrl = URL.createObjectURL(selectedFile)
    },
    uploadFile(selectedFile, onUploadProgress) {
      this.$emit('submit-upload-data', selectedFile, onUploadProgress)
    }
  }
}
</script>

<style>

</style>