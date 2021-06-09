<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  props: {
    modelValue: {
      type: [String, Number],
      default: '',
    },
  },
  emits: ['update:modelValue'],
  setup(_props, context) {
    return {
      handleInput(event: Event) {
        const target = event.target as HTMLInputElement
        context.emit('update:modelValue', target.value)
      },
    }
  },
})
</script>
<template>
  <input :value="modelValue" v-bind="$attrs" class="input-box" @input="handleInput" />
</template>
<style lang="postcss" scoped>
.input-box {
  @apply
    w-full py-2 px-3
    text-sm leading-5 sm:text-sm
    border rounded-sm border-blue-gray-200 shadow-sm
    focus:border-indigo-500 focus:outline-none;
}
</style>
