<script setup lang="ts">

    import WelcomeLoaderButton from '../../../button/buttons_specific/WelcomeLoaderButton.vue'
    import SwitchScreenMode from '../../../switch/switch_specific/SwitchScreenMode.vue'

    const emit = defineEmits(['inFocus', 'screenMode', 'load'])

    defineProps({
        darkModeActive: Boolean,
    })

</script>

<template>
    <div 
        class="h-screen absolute text-white flex flex-col justify-center items-center transition-all duration-500 z-50"
        :class="darkModeActive ? 'bg-haev_dark' : 'bg-haev_white'"
    >
        <div class="top-0 right-0 absolute mt-9 mr-5">
            <SwitchScreenMode
                :dark-mode="darkModeActive"
                @screenMode="emit('screenMode')"
            />
        </div>
        <span class="text-7xl text-center text-nowrap text-haev_orange">Haevnär</span>
        <WelcomeLoaderButton
            :dark-mode="darkModeActive"
            @load="$emit('load', $event)"
        />
        <span 
            class="text-xl text-nowrap transition-all duration-500"
            :class="darkModeActive ? 'text-haev_white' : 'text-haev_dark'"
        >Lancer le chargement de l'application</span>
    </div>
</template>../../../button/buttons_specific/WelcomeLoaderButton.vue