<script lang="ts">
import { defineComponent, ref } from 'vue'

export default defineComponent({
  props: {
    name: {
      type: String,
      default: '',
    },
  },
  setup() {
    const err = ref<string>('')

    return {
      err,
    }
  },
})
</script>
<template>
  <label v-bind="$attrs">
    <span v-if="name" class="block text-sm font-medium mb-1">{{ name }}</span>
    <slot></slot>
    <span v-if="err">{{ err }}</span>
  </label>
</template>
