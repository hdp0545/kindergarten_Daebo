<template>
  <v-container
    style="min-height: 800px">
  <v-row
      justify='center'>
      <div>
      <h1>
        Contact Us
      </h1>
      </div>
    </v-row>  
    <v-row
      justify='center'>
      <hr
        class="mt-1"
        width="110px"
        size="1pt"
        color="black"
        text-align="center">
    </v-row>
    
    <v-row
      justify="space-between"
      v-for="(images, index) in member_images"
      :key="index"
      :src="images.src"
      >
      <v-card   
        tile
        flat
        elevation="2"
        class="mt-16"
      >
        <v-container>
          <v-row
            class="mb-5 px-5">
           
            <v-img
              contain
              
            ></v-img>
          </v-row>
          <v-row
            class="px-5">
            <v-img
              contain
              src="../img/page_contact/icon_mail.png"
            ></v-img>
            <v-img
              contain
              src="../img/page_contact/icon_github.png"
            ></v-img>
            <v-img
              contain
              src="../img/page_contact/icon_instagram.png"
            ></v-img>
          </v-row>
        </v-container>
        
      </v-card>
    </v-row>
    
  </v-container>
</template>

<script>
export default {
  name: "Contact",
  data () {
    return {
      member_images: [
        {
          src:"../img/page_contact/member_SeungHyeonYang.png"
        },
        {
          src:'../img/page_contact/member_BeonChyulKim.png'
        },
        {
          src:'../img/page_contact/member_DuPyoHong.png'
        },
        {
          src: '../img/page_contact/member_KiSungBae.png'
        }
      ],
    }
  },
  computed: {
    member_image_path() {
      
      return this.member_image[0]
    }
  }
}
</script>

<style>
</style>