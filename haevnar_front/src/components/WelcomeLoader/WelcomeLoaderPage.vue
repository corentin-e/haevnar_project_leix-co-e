<script setup lang="ts">
    import WelcomeLoaderButton from './WelcomeLoaderButton.vue'
</script>

<template>
    <div class="bg-haev_dark h-screen absolute text-white flex flex-col justify-center items-center">
        <span class="text-7xl text-center text-nowrap text-haev_orange">Haevnär</span>
        <WelcomeLoaderButton @load="$emit('load', $event)"/>
        <span class="text-xl text-nowra text-haev_white">Lancer le chargement de l'application</span>
    </div>
</template>