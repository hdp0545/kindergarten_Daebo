<template>
  <v-container>
    <div
      class="uploadBox"  @drop.prevent="addFile" @dragover.prevent>
      <div v-if="selectedFile" class="progress">
        <v-progress-linear
          color="light-blue"
          height="10"
          :value="progress"
          striped
        > {{ progress }}% </v-progress-linear>
      </div>
      <div class="my-auto upload-word">Choose File <br> OR <br> Drag & Drop Files Here</div>
    </div>
  </v-container>
</template>

<script>
import UploadService from "../services/UploadFilesService";

export default {
  name: "upload-box",
  data() {
    return {
      selectedFile: undefined,
      imageUrl: "",
      progress: 0,

      during_OCR: false,
      
      message: "",
      fileInfos: [],
      rules: [
        value => !value || value.size < 2000000 || 'Picture size should be less than 2 MB!',
      ],
    }
  },
  methods: {
    fileUpload() {
      if (!this.selectedFile) {
        this.message = "Please select a file!";
        return;
      }
      this.message = ""
      UploadService.upload(this.selectedFile, (event) => {
        this.progress = Math.round((100 * event.loaded) / event.total);
      })
        .then((response) => {
          this.message = response.data.message;
          console.log(this.message)
          this.$emit('start-ocr')
          this.progress = 0
          this.during_OCR = true
          this.selectedFile = undefined
        }).catch((err) => {
          console.log(err)
          this.progress = 0;
          this.message = "Could not upload the file!";
          this.selectedFile = undefined;
          console.log(this.message)
        });
    },
    addFile(e) {
      this.selectedFile = e.dataTransfer.files[0]
      console.log(this.selectedFile)
      this.fileUpload()
    }

    // upload() {
    //   console.log("start")
    //   this.progress = 0;
    //   this.uploadData.name = this.selectedFiles.item(0).name
    //   this.$emit('submit-upload-data', this.uploadData)
    //   this.currentFile = this.selectedFiles.item(0);
    //   this.$emit('upload-file', this.currentFile)
    //   UploadService.upload(this.currentFile, event => {
    //     this.progress = Math.round((100 * event.loaded) / event.total);
    //   })
    //     .then(response => {
    //       this.message = response.data.message;
    //       // return UploadService.getFiles();
    //     })
    //     // .then(files => {
    //     //   this.fileInfos = files.data;
    //     // })
    //     // .catch(() => {
    //     //   this.progress = 0;
    //     //   this.message = "Could not upload the file!";
    //     //   this.currentFile = undefined;
    //     // });
    //   this.selectedFiles = undefined;
    // }
  },
}

</script>

<style>
.uploadBox {
  background-color:rgb(132, 151, 176);
  width: 100%;
  height: 280px;
  border: dashed rgb(68, 114, 196);
  line-height: 1.5rem;
  margin: auto;
  text-align: center;
  align-content: center;
  color: white;
  display: block;
  position: relative;
}
.upload-word {
  position: relative;
  top: 90px;
}
.progress {
  position: absolute;
  width: 100%;
} 




</style>