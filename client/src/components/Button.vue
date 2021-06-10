<template>
  <button class="button" v-bind="$attrs">
    <slot></slot>
  </button>
</template>
<style lang="postcss" scoped>
.button {
  @apply
    inline-block px-3 py-2
    rounded-sm
    text-center text-white cursor-pointer
    disabled:cursor-default disabled:bg-gray-600 disabled:opacity-50
    foucs:outline-none;

  background-color: var(--primary-color);
}
</style>
