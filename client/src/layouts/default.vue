<script setup lang="ts">
import { useNaiveThemeOverrides } from '~/logic'
const { themeOverrides } = useNaiveThemeOverrides()
</script>
<template>
  <NConfigProvider :theme-overrides="themeOverrides">
    <NMessageProvider>
      <main class="text-gray-700 dark:text-gray-200">
        <Sidebar />
        <div>
          <Header />
          <div class="px-4 sm:px-6 lg:px-8 py-8 w-full max-w-9xl mx-auto">
            <router-view></router-view>
          </div>
        </div>
        <div class="mt-5 mx-auto text-center opacity-25 text-sm">[Home Layout]</div>
      </main>
    </NMessageProvider>
  </NConfigProvider>
</template>
