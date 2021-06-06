<script setup lang="ts">
import { defineProps } from 'vue'

const props = defineProps({
  active: {
    type: Boolean,
    default: false,
  },
})
</script>
<template>
  <svg v-bind="$attrs" viewBox="0 0 24 24">
    <path
      class="fill-current"
      :class="props.active ? 'text-indigo-300' : 'text-gray-400'"
      d="M7 0l6 7H8v10H6V7H1z"
    />
    <path
      class="fill-current"
      :class="props.active ? 'text-indigo-500' : 'text-gray-600'"
      d="M18 7v10h5l-6 7-6-7h5V7z"
    />
  </svg>
</template>
<style>
</style>
