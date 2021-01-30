<template>
  <v-container
    style="min-height: 600px"
    class="my-main">
    <!-- about page -->
    <about></about>
    <!-- converter page -->
    <convert
      @submit-upload-data="uploadFile"
      @start-ocr="startOcr"></convert>
    <!-- contact page -->
    <contact></contact>
  </v-container>
</template>

<script>
import About from './About.vue'
import Contact from './Contact.vue'
import Convert from './Convert.vue'

export default {
  name: 'Home',
  components: {
    About,
    Contact,
    Convert
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
