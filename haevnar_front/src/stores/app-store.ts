import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useThemeStore = defineStore('theme', () => {
  const theme = ref('dark')
  function onChangeThemeMode() {
    console.log('theme')
    theme.value = theme.value == 'dark' ? 'light' : 'dark'
    console.log('theme', theme.value)
  }
  return { theme, onChangeThemeMode }
})
