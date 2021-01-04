<template>
  <v-container>
    <div v-if="currentFile" class="progress">
      <div
        class="progress-bar progress-bar-info progress-bar-striped"
        role="progressbar"
        :aria-valuenow="progress"
        aria-valuemin="0"
        aria-valuemax="100"
        :style="{ width: progress + '%' }"
      >
        {{ progress }}%
      </div>
    </div>
    <div
      class="uploadBox">
      <div class="py-auto">Choose File <br> OR <br> Drag & Drop Files Here</div>    
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
      
      message: "",
      fileInfos: [],
      rules: [
        value => !value || value.size < 2000000 || 'Picture size should be less than 2 MB!',
      ],
    }
  },
  methods: {
    selectFile() {
      this.$emit('select-file', this.selectedFile)
    },
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
        })
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
  padding-top: 11%;
  }




</style>