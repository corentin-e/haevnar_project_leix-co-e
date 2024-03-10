<script setup lang="ts">
import LogoHaev from '../../assets/logos/logo_haevnär_white.png'
</script>

<template>
    <div class="button-container mt-3 mb-3 flex justify-center items-center cursor-pointer w-full h-56 relative">
        <div class="button-band border-2 border-haev_orange h-0"></div>
        <button type="button" name="Lancer l'application" class="flex items-center justify-content-center Z-50 absolute rounded-full button-custom bg-haev_dark border border-haev_white py-8 px-8" @click="$emit('load', $event)">
            <img :src="LogoHaev" alt="logo Haevnär">
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
        width: 200px;
        height: 200px;
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