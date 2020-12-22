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


    <img class="img-video" src='../img/icon-video.png' alt="비디오 로고" height="100"/>
    
    <v-img
      :src="imageUrl"
      max-height="450"
      max-width="600"
    ></v-img>
      <!-- <input type="file"  /> -->
    <v-form>
      <v-file-input
        :rules="rules"
        accept="image/png, image/jpeg, image/bmp"
        placeholder="인식할 사진을 넣어주세요"
        prepend-icon="mdi-camera"
        label="Picture"
        v-model="selectedFile"
        @change="selectFile"
      ></v-file-input>
      <v-btn
        color="primary"
        class="mr-4"
        @click="fileUpload">
        전송
      </v-btn>
    </v-form>
    

  </v-container>
</template>

<script>
import UploadService from "../services/UploadFilesService";

export default {
  name: "upload-box",
  data() {
    return {
      selectedFile: [],
      imageUrl: "",
      progress: 0,
      currentFile: undefined,
      
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
      if (!this.currentFile) {
        this.message = "Please select a file!";
        return;
      }
      this.message = ""
      UploadService.upload(this.currentFile, (event) => {
        this.progress = Math.round((100 * event.loaded) / event.total);
      })
        .then((response) => {
          this.message = response.data.message;
          return UploadService.getFiles();
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

</style>