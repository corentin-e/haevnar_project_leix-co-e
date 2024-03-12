<script setup lang="ts">
import { ref } from 'vue'

import WelcomeLoader from './components/loading/loading_specific/welcome/WelcomeLoader.vue'

const darkModeActive = ref(true)

const onSwitchScreenMode = () => {
    darkModeActive.value = !darkModeActive.value
}

const loadApplication = () => {
  const loader = document.getElementById('loader')
  loader.classList.add("hidden-loader")
}
</script>

<header>
  
</header>

<template>
  <WelcomeLoader 
    id="loader" 
    class="loader w-full"
    :dark-mode-active="darkModeActive"
    @screenMode="onSwitchScreenMode"
    @load="loadApplication"
  />
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
</style>./components/loading/loading_specific/welcome/WelcomeLoader.vue
