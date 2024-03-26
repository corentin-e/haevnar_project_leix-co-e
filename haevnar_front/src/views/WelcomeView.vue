<script setup lang="ts">
  import WelcomeImg from '@/assets/images/welcome-image.png'
  import { RouterLink } from 'vue-router'

  import LogoShipHaevnarWhite from '@/assets/logos/logo_ship_haevnar_white.png'

  import { useThemeStore } from '@/stores/app-store'

  defineProps({
    darkModeActive: Boolean,
  })

  const theme = useThemeStore()

  theme.theme
</script>

<template>
  <div class="w-full justify-center flex flex-col pt-5">
    <!-- Banneer - Components -->
    <div class="overflow-hidden img-frame-custom">
      <div class="relative text-haev_white z-20 w-full h-full p-24 text-custom">
        <div class="flex items-start h-full">
          <div class="w-4/5">
            <p class="text-first-custom text-custom">
              Bienvenue sur le site de l'Alliance d'Hævnär,
            </p>
            <p class="pt-2">
              Un réseau interstellaire de corporations unifiées et de citoyens visionnaires dans l'univers de Star Citizen.
            </p>
            <p class="pt-2">
              Une alliance dynamique et diversifié de corporations spécialisées, s'étendant des activités d'exploration et de mercenariat, à la logistique et au sport compétitif.
            </p>
            <p  class="pt-2">
              Nous sommes une communauté soudée de pionniers, d'explorateurs, de commerçants, et de guerriers, œuvrant ensemble pour forger un avenir meilleur dans les vastes étendues de l'espace.
            </p>
            <p  class="pt-2">
              Chez nous, vous trouverez une place pour vous et les votres, que vous soyez un vétéran de l'espace ou un nouveau venu dans l'univers de Star Citizen.
            </p>
          </div>
          <img :src="LogoShipHaevnarWhite" alt="welcome image" class="w-1/5">
        </div>
      </div>
      <img :src="WelcomeImg" alt="welcome image" class="w-full img-size-custom">
    </div>
    <!-- Button - Banneer - Components -->
    <div class="bg-haev_orange p-5 flex justify-center">
      <RouterLink to="/registration">
        <button type="button" class="rounded-full border border-haev_dark bg-transparent text-haev_dark px-5 py-2 hover:bg-haev_dark hover:text-haev_orange transition-all duration-300">Rejoindre l'Alliance</button>
    </RouterLink>
    </div>
      <!-- News - Components -->
    <span class="title-news-custom w-full text-center">
      Journal de l'Alliance
    </span>
    <div class="flex flex-col px-10">
      <span class="title-sub-new-custom">
        Vie de l'alliance
      </span>
    </div>
  </div>
</template>

<style>
.img-frame-custom {
  width: 100%;
  margin: 0 auto;
  overflow: hidden;
  position: relative;
  height: 600px;
}
.img-size-custom {
  top: -300px;
  position: absolute;
}

.text-first-custom::first-letter {
  font-family: "Slackside One", cursive;
  font-size: 64px;
}

.text-custom {
  font-size: 22px;
}

.title-news-custom::first-letter {
  font-family: "Slackside One", cursive;
  font-size: 94px;
}

.title-news-custom {
  font-size: 40px;
}

.title-sub-new-custom {
  font-family: "Slackside One", cursive;
  font-size: 33px;
  color: var(--haev_orange)
}

</style>
