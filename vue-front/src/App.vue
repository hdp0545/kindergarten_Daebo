<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <a href="/">
        <div class="d-flex align-center">
          <v-img
            alt="Vuetify Logo"
            class="shrink mr-2"
            contain
            src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
            transition="scale-transition"
            width="40"
          />

          <v-img
            alt="Vuetify Name"
            class="shrink mt-1 hidden-sm-and-down"
            contain
            min-width="100"
            src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
            width="100"
          />
        </div>
      </a>

      <v-spacer></v-spacer>
      <v-tabs
        dark
        optional
        right
        >
        <v-tab
          to="/about"
          text
        >
          <span class="mr-2">About Us</span>
        </v-tab>
        <v-tab
          to="/convert"
          text
        >
          <span class="mr-2">Convert</span>
        </v-tab>
        <v-tab
          to="/contact"
          text
        >
          <span class="mr-2">Contact Us</span>
        </v-tab>
      </v-tabs>
    </v-app-bar>

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
    }
  }
};
</script>
