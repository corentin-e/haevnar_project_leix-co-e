<script setup lang="ts">
import { ref, computed, watch } from 'vue'

import { useThemeStore } from '@/stores/app-store'

import WelcomeLoader from '@/components/loading/loading_specific/welcome/WelcomeLoader.vue'
import HeaderPage from '@/components/HeaderPage.vue'

const theme = useThemeStore()

theme.theme

const loaderActive = ref(true)

const themeMode = computed(() => {
  return theme.theme
})


watch(themeMode, (newTheme) => {
  if(newTheme == 'dark') {
    document.documentElement.style.setProperty('--bg_app', 'var(--haev_bg_mode_dark)');
    document.documentElement.style.setProperty('--text_app', 'var(--haev_text_mode_dark)');
  } else {
    document.documentElement.style.setProperty('--bg_app', 'var(--haev_bg_mode_light)');
    document.documentElement.style.setProperty('--text_app', 'var(--haev_text_mode_light)');
  }
})


const loadApplication = () => {
  loaderActive.value = false
}

</script>

<header>
  
</header>

<template >
  <div
    class="w-100 h-screen transition-all duration-500 theme-mode"
  >
    <WelcomeLoader
      v-if="loaderActive"
      id="loader" 
      class="loader w-full"
      @load="loadApplication"/>
    <HeaderPage/>
    <router-view></router-view>
  </div>
  
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
