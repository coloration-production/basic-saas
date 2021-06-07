<script setup lang="ts">
import { defineProps } from 'vue-demi'

const props = defineProps({
  title: {
    type: String,
    default: '',
  },
})
</script>
<template>
  <div v-bind="$attrs">
    <div class="flex justify-between items-center">
      <h2 class="text-xl md:text-3xl font-bold">{{ props.title }}</h2>
      <div>
        <slot></slot>
      </div>
    </div>
  </div>
</template>
