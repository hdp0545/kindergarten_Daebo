<template>
  <v-container
    style="min-height: 600px"
    class="my-main">
    <about></about>
    <convert
      @submit-upload-data="uploadFile"></convert>
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
    }
  }
}
</script>
