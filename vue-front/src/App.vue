<template>
  <v-app>
    <v-img
      alt="Background Image"
      src='@/img/background.png'
      height='800px'
      gradient="to top, rgba(0,0,0,.4), rgba(0,0,0,.9)"
      background-position
      >
      <v-layout column align-center justify-center class="mt-n7 white--text" fill-height>
        <h1 class="white--text font-weight-bold display-2 mb-1 text-center">Kindergarten_AI</h1>
        <hr
          width="150px"
          class="my-4">
				<div class="subheading mb-4 text-center">인공지능을 이용한 차량 번호판 화질 개선 및 인식 프로젝트</div>
      </v-layout>
    </v-img>
    <v-app-bar
      v-scroll="onScroll"
      color="white"
      light
      flat
      :fixed="fixed"
      :class="bosang"
    > 
      <v-container
        class="mx-auto"
        style="min-width: 1000px">
        <v-row
          justify="space-between">
          <v-col>
            <a href="/">
              <div class="d-flex-inline mb-n20 align-start">
                <v-img
                  alt="Wall-E Logo"
                  class="shrink mr-2 mt-2"
                  contain
                  src="./img/page_main/logo_horizontal.png"
                  transition="scale-transition"
                  width="250px"
                />
              </div>
            </a>
          </v-col>
          <v-col
            class="mt-3">
            <v-tabs
              lights
              optional
              right
              >
              <v-tab
                to="/"
                text
              >
                <span class="mr-2">Home</span>
              </v-tab>
              <v-tab
                to="/about"
                text
              >
                <span class="mr-2">About Program</span>
              </v-tab>
              <v-tab
                to="/convert"
                text
              >
                <span class="mr-2">Converter</span>
              </v-tab>
              <v-tab
                to="/contact"
                text
              >
                <span class="mr-2">Contact</span>
              </v-tab>
            </v-tabs>
          </v-col>
        </v-row>
      </v-container>
    </v-app-bar>

    <div
      :v-if="fixed"
      class="height-64px"></div>
    <v-main>
      <router-view
        @submit-upload-data="uploadFile"
      ></router-view>
    </v-main>
    <footer-vue/>
  </v-app>
</template>

<script>
import footerVue from '@/components/Footer.vue'
import axios from 'axios'

// const SERVER_URL = 'http://34.64.197.76/api'
const SERVER_URL = 'http://127.0.0.1:8000'
export default {
  name: 'App',

  components: {
    footerVue,
  },

  data: () => ({
    file: undefined,
    fixed: false,
    offsetTop: 0,
    bosang: ""
  }),
  methods: {
    uploadFile(file, onUploadProgress) {
      let formData = new FormData();
      formData.append("file", file)

      console.log(formData, onUploadProgress)
      axios.post(`${SERVER_URL}/img/`, formData,
        {headers: {
          'Content-Type': "multipart/form-data"}
        }
      ).then(response => {
        console.log(response)
      }).catch(err => {
        console.log(err)
      })
    },
    onScroll () {
      if (window.scrollY >= 800) {
        this.bosang = "pb-16"
        this.fixed = true
        
        
      } else if (window.scrollY <= 800) {
        this.bosang = ""
        this.fixed = false
      }
    },
  }
};
</script>
<style scoped>
.my-main {
  max-width: 900px;
}

</style>


