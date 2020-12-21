<template>
  <div>
    <v-container>
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
    uploadFile(selectedFile) {
      this.$emit('submit-upload-data', selectedFile)
    }
  }
}
</script>

<style>

</style>