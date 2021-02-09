<template>
  <v-container
    style="min-height: 600px"
    class="my-main">
    <!-- about page -->
    <about></about>
    <v-spacer
      class="spacer"></v-spacer>
    <!-- converter page -->
    <convert
      @submit-upload-data="uploadFile"
      @start-ocr="startOcr"></convert>
    <!-- contact page -->
    <v-spacer
      class="spacer"></v-spacer>
    <contact></contact>
    <after-recognition></after-recognition>
  </v-container>
</template>

<script>
import About from './About.vue'
import Contact from './Contact.vue'
import Convert from './Convert.vue'
import AfterRecognition from './AfterRecognition.vue'

export default {
  name: 'Home',
  components: {
    About,
    Contact,
    Convert,
    AfterRecognition
  },
  methods: {
    uploadFile(selectedFile, onUploadProgress) {
      this.$emit('submit-upload-data', selectedFile, onUploadProgress)
    },
    startOcr() {
      this.$emit('start-ocr')
    }
  }
}
</script>

<style scoped>
.spacer {
  height: 150px;
}
</style>
