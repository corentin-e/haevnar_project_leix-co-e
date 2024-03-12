<script setup lang="ts">

import LogoHaevLight from '../../../../assets/logos/logo_haevnar_white_orange.png'
import LogoHaevDark from '../../../../assets/logos/logo_haevnar_balck_orange.png'

defineProps({
    darkMode: Boolean,
})

</script>

<template>
    <div class="button-container mt-3 mb-3 flex justify-center items-center cursor-pointer w-full h-56 relative">
        <div class="button-band border-2 border-haev_orange h-0"></div>
        <button 
            type="button" 
            name="Lancer l'application" 
            class="flex items-center justify-items-center z-50 absolute rounded-full button-custom border py-8 px-8"
            :class="darkMode ? 'bg-haev_dark border-haev_white' : 'bg-haev_white border-haev_dark'" 
            @click="$emit('load', $event)"
        >
            <img 
                :src="darkMode ? LogoHaevLight : LogoHaevDark" 
                alt="logo Haevnär"
            >
        </button>
    </div>
</template>

<style scoped>
    .button-container {
        height: 22%;
        transition: all .5s ease;
    }
    .button-band {
        width: 0px;
        transition: all .5s ease;
    }
    .button-custom {
        width: 160px;
        height: 160px;
        transition: all .5s ease;
        box-shadow: 0px 1px 30px 9px rgba(0, 0, 0, 0.4);
    }

    .button-container:hover {
        height: 30%;
    }
    .button-container:hover > .button-band {
        width: 60%;
    }

    .button-container:hover > .button-custom {
        width: 250px;
        height: 250px;
        box-shadow: 0px 1px 18px 9px rgba(247, 124, 4, 0.8);
    }

    .button-container:hover > .button-custom {
        width: 300px;
        height: 300px;
    }

    @media screen and (max-width: 986px) {
        .button-container:hover {
            height: 45%;
        }
    }

</style>