<template>
  <v-container
    style="min-height: 600px"
    class="my-main">
    <!-- about page -->
    <about></about>
    <v-spacer
      class="spacer"></v-spacer>
    <!-- converter page -->
    <convert></convert>
    <!-- contact page -->
    <v-spacer
      class="spacer"></v-spacer>
    <contact></contact>
    <processing></processing>
  </v-container>
</template>

<script>
import About from './About.vue'
import Contact from './Contact.vue'
import Convert from './Convert.vue'
import Processing from './Processing.vue'

export default {
  name: 'Home',
  components: {
    About,
    Contact,
    Convert,
    Processing,
  },
  methods: {
  }
}
</script>

<style scoped>
.spacer {
  height: 150px;
}
</style>
