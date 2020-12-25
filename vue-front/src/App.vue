<template>
  <v-app
    >
    <v-img
      alt="Background Image"
      src='@/img/background.png'
      height='800px'>
    </v-img>
    <v-app-bar
      v-scroll="onScroll"
      class="fixed"
      color="white"
      light
      flat
      :fixed="fixed"
    >
      <a href="/">
        <div class="d-flex align-start">
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


      <v-spacer></v-spacer>
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
    </v-app-bar>

    <v-main
      :class="bosang">
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
        this.bosang = "mt-16"
        this.fixed = true
        
        
      } else if (window.scrollY <= 700) {
        this.bosang = ""
        this.fixed = false
      }
    },
  }
};
</script>
<style scoped>

</style>


