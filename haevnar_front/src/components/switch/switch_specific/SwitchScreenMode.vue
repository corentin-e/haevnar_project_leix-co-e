<script setup lang="ts">

defineProps({
    darkMode: Boolean,
})

const emit = defineEmits(['inFocus', 'screenMode'])

const onClickSwitch = () => {
    emit('screenMode')
}
</script>

<template>
    <button 
        class="flex outline-none border-none" 
        @click="onClickSwitch"
    >
        <i 
            class='bx bx-moon bx-sm transition-all duration-500 mr-2'
            :class="darkMode ? 'text-haev_white' : 'text-haev_dark'"
        />
        <div 
            class="flex bg-haev_orange rounded-full w-12 h-5"
        >
            <div class="flex justify-end transition-all duration-500"
                :class="darkMode ? 'w-custom-dark' : 'w-custom-ligth' "
            >
                <div 
                    class=" rounded-full w-5 h-5 z-50 absolute transition-all duration-500"
                    :class="darkMode ? 'bg-haev_white' : 'bg-haev_dark'"
                >
                </div>
            </div>
        </div>
        <i 
            class='bx bx-sun bx-sm transition-all duration-500 ml-2'
            :class="darkMode ? 'text-haev_white' : 'text-haev_dark'"
        />
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