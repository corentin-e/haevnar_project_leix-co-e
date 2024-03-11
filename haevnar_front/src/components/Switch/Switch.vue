<script setup lang="ts">
import { ref } from 'vue'
    const darkMode = ref(true) 
    const onClickSwitch = () => {
        darkMode.value = !darkMode.value
    }
</script>

<template>
    <button 
        class="outline-none border-none" 
        @click="onClickSwitch"
    >
        <div 
            class="flex bg-haev_orange rounded-full w-12 h-5"
        >
            <div class="flex justify-end transition-all duration-500"
                :class="darkMode ? 'w-custom-dark' : 'w-custom-ligth' "
            >
                <div class="bg-haev_white rounded-full w-5 h-5 z-50 absolute">
                </div>
            </div>
        </div>
    </button>

</template>

<style>
    .w-custom-dark {
        width: 20px;
    }
    .w-custom-ligth {
        width: 70px;
    }
</style>