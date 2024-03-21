<script setup lang="ts">
    import { useThemeStore } from '@/stores/app-store'

    import WelcomeLoaderButton from '../../../button/buttons_specific/WelcomeLoaderButton.vue'
    import SwitchScreenMode from '../../../switch/switch_specific/SwitchScreenMode.vue'


    const theme = useThemeStore()

    theme.theme

    const emit = defineEmits(['inFocus', 'screenMode', 'load'])

</script>

<template>
    <div 
        class="h-screen absolute text-white flex flex-col justify-center items-center transition-all duration-500 z-50 theme-mode"
    >
        <div class="top-0 right-0 absolute mt-9 mr-5">
            <SwitchScreenMode/>
        </div>
        <span class="text-7xl text-center text-nowrap text-haev_orange">Haevnär</span>
        <WelcomeLoaderButton
            @load="$emit('load', $event)"
        />
        <span 
            class="text-xl text-nowrap"
        >Lancer le chargement de l'application</span>
    </div>
</template>