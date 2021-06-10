<script setup lang="ts">
import { useNaiveThemeOverrides } from '~/logic'
const { themeOverrides } = useNaiveThemeOverrides()
</script>
<template>
  <NConfigProvider :theme-overrides="themeOverrides">
    <main class="text-gray-700 dark:text-gray-200">
      <router-view />
    </main>
  </NConfigProvider>
</template>
