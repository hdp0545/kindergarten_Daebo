<template>
  <div>
    <v-container
      style="min-height: 800px">
      <v-img :src="imageUrl"></v-img>
    </v-container>
    <upload-box
      @select-file="selectFile"
      @submit-upload-data="uploadFile"
    ></upload-box>
  </div>
</template>

<script>
import UploadBox from '../components/UploadBox.vue'
export default {
  name: "Convert",
  components: {
    UploadBox
  },
  data() {
    return {
      imageUrl: '',
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