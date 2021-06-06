<script lang="ts">
import { useToggle } from '@vueuse/core'
import { defineComponent, onBeforeUnmount, watch } from 'vue'

export default defineComponent({
  props: {
    visiable: {
      type: Boolean,
      default: true,
    },
    items: {
      type: Array,
      default: () => ([]),
    },
  },
  setup(props) {
    const barWidth = 256
    const [pinned, toggle] = useToggle(true)
    watch(pinned, () => {
      document.documentElement.style.setProperty('--sidebar-offset-width', `${pinned.value ? barWidth : 0}px`);
    }, { immediate: true })
    onBeforeUnmount(() => {
      document.documentElement.style.setProperty('--sidebar-offset-width', '0px');
    })
    return {
      barWidth, toggle, pinned,
    }
  },
})

</script>
<template>
  <div>
    <div
      class="fixed left-0 top-0 bottom-0 z-40 bg-gray-800 p-4 transition-transform duration-200 ease-in-out"
      :style="{ width: `${barWidth}px` }"
    >
      <div class="flex flex-col h-full">
        <div class="flex justify-between items-center pr-1 mb-10">
          <button
            class="lg:hidden text-gray-500 hover:text-gray-400 hidden-outline"
            aria-controls="sidebar"
            aria-expanded="true"
          >
            <akar-icons-arrow-left />
          </button>
          <router-link to="/">
            <IconDashboard class="flex-shrink-0 h-8 w-8" active />
          </router-link>
        </div>

        <div class="flex-1">
          <h3 class="text-xs uppercase text-gray-500 font-semibold mb-3">Pages</h3>
          <ul>
            <li class="px-3 py-2 rounded-sm mb-0.5 last:mb-0 bg-gray-900">
              <router-link
                to="/"
                class="block text-gray-200 hover:text-white transition duration-150"
              >
                <div class="flex flex-grow items-center">
                  <IconDashboard class="flex-shrink-0 h-6 w-6 mr-3" active />
                  <span class="text-sm font-medium flex-1">Dashboard</span>
                </div>
              </router-link>
            </li>
            <li class="px-3 py-2 rounded-sm mb-0.5 last:mb-0">
              <router-link
                to="/"
                class="block text-gray-200 hover:text-white transition duration-150"
              >
                <div class="flex flex-grow items-center">
                  <IconCustomers class="flex-shrink-0 h-6 w-6 mr-3" />
                  <span class="text-sm font-medium flex-1">Customers</span>
                  <span
                    class="inline-flex items-center justify-center h-5 text-xs font-medium text-white bg-indigo-500 px-2 rounded-sm"
                  >4</span>
                </div>
              </router-link>
            </li>
            <li class="px-3 py-2 rounded-sm mb-0.5 last:mb-0 bg-gray-900">
              <router-link
                to="/"
                class="block text-gray-200 hover:text-white transition duration-150"
              >
                <div class="flex flex-grow items-center">
                  <svg class="flex-shrink-0 h-6 w-6 mr-3" viewBox="0 0 24 24">
                    <path
                      class="fill-current false text-indigo-500"
                      d="M18.974 8H22a2 2 0 012 2v6h-2v5a1 1 0 01-1 1h-2a1 1 0 01-1-1v-5h-2v-6a2 2 0 012-2h.974zM20 7a2 2 0 11-.001-3.999A2 2 0 0120 7zM2.974 8H6a2 2 0 012 2v6H6v5a1 1 0 01-1 1H3a1 1 0 01-1-1v-5H0v-6a2 2 0 012-2h.974zM4 7a2 2 0 11-.001-3.999A2 2 0 014 7z"
                    />
                    <path
                      class="fill-current false text-indigo-300"
                      d="M12 6a3 3 0 110-6 3 3 0 010 6zm2 18h-4a1 1 0 01-1-1v-6H6v-6a3 3 0 013-3h6a3 3 0 013 3v6h-3v6a1 1 0 01-1 1z"
                    />
                  </svg>
                  <span class="text-sm font-medium flex-1">權限管理</span>
                  <akar-icons-chevron-down class="text-sm mr-1" />
                </div>
              </router-link>
              <ul class="pl-9 mt-1">
                <li class="mb-1 block hover:text-indigo-400 text-gray-200">
                  <router-link to="/" class="text-sm">角色管理</router-link>
                </li>
                <li class="mb-1 block hover:text-indigo-400 text-gray-200">
                  <router-link to="/" class="text-sm">用戶管理</router-link>
                </li>
              </ul>
            </li>
          </ul>
        </div>

        <div class="flex justify-end">
          <carbon-pin-filled v-if="pinned" @click="toggle" />
          <carbon-pin v-else @click="toggle" />
        </div>
      </div>
    </div>
    <!-- shadow  -->
    <div
      class="fixed inset-0 bg-gray-900 bg-opacity-30 z-40 lg:hidden lg:z-auto transition-opacity duration-200 opacity-0 pointer-events-none"
    />
  </div>
</template>
