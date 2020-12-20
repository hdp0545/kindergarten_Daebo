<template>
  <div>
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
    <label class="selectbtn btn btn-default">
      <!-- <input type="file"  /> -->
      <input type="text" value="선택된 파일이 없습니다." id="fileName" class="file_input_textbox" readonly="readonly">
      <input type="button" value="파일 선택" class="file_input_button font-weight-bold"/>
      <input type="file" ref="file" @change="selectFile" class="file_input_hidden" onchange="javascript:document.getElementById('fileName').value = this.value.split('\\')[this.value.split('\\').length-1]">
    </label>
    <!-- :disabled="!selectedFiles" -->
  </div>
</template>

<script>
export default {
  name: "Convert",
  data() {
    return {
      selectedFiles: undefined,
      currentFile: undefined,
      progress: 0,
      message: "",
      fileInfos: [],
    }
  }
}
</script>

<style>

</style>