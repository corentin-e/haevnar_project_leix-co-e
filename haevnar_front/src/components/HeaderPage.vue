<script setup lang="ts">
    import { RouterLink, useRouter } from 'vue-router'
    import { computed } from 'vue'
    import { useThemeStore } from '@/stores/app-store'

    import SwitchScreenMode from '@/components/switch/switch_specific/SwitchScreenMode.vue';

    import LogoTitleHaevnarBlack from '../assets/logos/logo_haevnär_black_title.png'
    import LogoTitleHaevnarWhite from '../assets/logos/logo_haevnär_white_title.png'

    const theme = useThemeStore()

    theme.theme

    const getRouteName = computed(() => router.currentRoute.value.name)

    const router = useRouter()

    const emit = defineEmits(['inFocus', 'screenMode'])
</script>

<template>
    <div 
        class="flex items-center justify-between px-5 text_mode"
    >
        <RouterLink to="/">
            <img 
                :src="theme.theme == 'dark' ? LogoTitleHaevnarWhite : LogoTitleHaevnarBlack"
                width="230"
                alt="logo title Haevnär"
            >
        </RouterLink>

        <div class="flex">
            <RouterLink to="/">
                <div 
                    class="px-12 py-4 "
                    :class="getRouteName === 'home' ? 'text-haev_orange border-b border-b-haev_orange' : 'nav-link-custom'"
                >
                    Bienvenue !
                </div>
            </RouterLink>
            <RouterLink to="/alliances">
                <div 
                    class="px-12 py-4 "
                    :class="getRouteName === 'alliances' ? 'text-haev_orange border-b border-b-haev_orange' : 'nav-link-custom'"
                >
                    Alliances
                </div>
            </RouterLink>
            <RouterLink to="/events">
                <div 
                    class="px-12 py-4 "
                    :class="getRouteName === 'events' ? 'text-haev_orange border-b border-b-haev_orange' : 'nav-link-custom'"
                >
                    Evénements
                </div>
            </RouterLink>
            <RouterLink to="/registration">
                <div 
                    class="px-12 py-4 "
                    :class="getRouteName === 'registration' ? 'text-haev_orange border-b border-b-haev_orange' : 'nav-link-custom'"
                >
                    Inscription
                </div>
            </RouterLink>
        </div>

        <SwitchScreenMode
            @screenMode="emit('screenMode')"
        />
    </div>
</template>

<style>
    .nav-link-custom {
        color: var(--text_app);
        border-bottom: 1px solid var(--text_app);
        transition: all 0.5s;
    }
    .nav-link-custom:hover {
        color: #F77C04;
        border-bottom: 1px solid #F77C04;
    }
</style>