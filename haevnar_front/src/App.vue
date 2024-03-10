<script setup lang="ts">
import WelcomeLoader from './components/WelcomeLoader/WelcomeLoaderPage.vue'

function loadApplication () {
  const loader = document.getElementById('loader')
  loader.classList.add("hidden-loader")
}
</script>

<template>
  <WelcomeLoader id="loader" class="loader w-full" @load="loadApplication"/>
</template>

<style scoped>

.loader {
  transition: all .8s;
}
  .hidden-loader {
    width: 0%;
    overflow: hidden;
    opacity: 0;
  }
</style>
