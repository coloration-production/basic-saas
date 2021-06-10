<script lang="ts">
import { useToggle } from '@vueuse/core'
import { defineComponent, onBeforeUnmount, PropType, watch, ref } from 'vue'
import { useRoute } from 'vue-router'
import IconDashboard from '~/components/IconDashboard.vue'
import IconTeam from '~/components/IconTeam.vue'
import { SidebarItem } from '~/types/views'

export default defineComponent({
  props: {
    visiable: {
      type: Boolean,
      default: true,
    },
    items: {
      type: Array as PropType<SidebarItem[]>,
      default: () => ([
        { name: 'Dashboard', icon: IconDashboard, value: '/dashboard' },
        {
          name: 'Permission',
          icon: IconTeam,
          value: '/permission',
          children: [
            { name: 'Permission', value: '/permission/permissions' },
            { name: 'Roles', value: '/permission/roles' },
            { name: 'Users', value: '/permission/users' },
          ],
        },
        {
          name: 'Monitor',
          value: '/monitor',
          icon: IconDashboard,
          children: [
            { name: 'Cameras', value: '/monitor/cameras' },
            { name: 'Screens', value: '/monitor/screens' },
          ],
        },
        { name: 'Settings', value: '/settings', icon: IconDashboard, tips: 6 },
      ]),
    },
  },
  setup() {
    const barWidth = 256
    const [pinned, toggle] = useToggle(true)
    const route = useRoute()
    const expandKeys = ref<string[]>([])

    function toggleExpandKey(key: SidebarItem['value']) {
      const idx = expandKeys.value.indexOf(key)
      if (idx < 0) expandKeys.value.push(key)
      else expandKeys.value.splice(idx, 1)
    }

    watch(pinned, () => {
      document.documentElement.style.setProperty('--sidebar-offset-width', `${pinned.value ? barWidth : 0}px`)
    }, { immediate: true })

    onBeforeUnmount(() => {
      document.documentElement.style.setProperty('--sidebar-offset-width', '0px')
    })

    return {
      barWidth, toggle, pinned, route, expandKeys, toggleExpandKey,
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
            <li
              v-for="item in items"
              :key="item.name"
              class="px-3 py-2 rounded-sm mb-0.5 last:mb-0 text-gray-200 hover:text-white hover:bg-gray-900 transition"
              :class="route.path.startsWith(item.value) ? 'bg-gray-900' : ''"
            >
              <router-link
                :to="item.children ? '' : item.value"
                @click="item.children && toggleExpandKey(item.value)"
              >
                <div class="flex flex-grow items-center">
                  <component
                    :is="item.icon"
                    class="flex-shrink-0 h-6 w-6 mr-3"
                    :active="route.path.startsWith(item.value)"
                  />
                  <span class="text-sm font-medium flex-1">{{ item.name }}</span>
                  <akar-icons-chevron-up
                    v-if="item.children && expandKeys.includes(item.value)"
                    class="text-sm mr-1"
                  />
                  <akar-icons-chevron-down
                    v-if="item.children && !expandKeys.includes(item.value)"
                    class="text-sm mr-1"
                  />
                  <span
                    v-if="item.tips && item.tips > 0"
                    class="inline-flex items-center justify-center h-5 text-xs font-medium text-white bg-indigo-500 px-2 rounded-sm"
                  >{{ item.tips }}</span>
                </div>
              </router-link>
              <ul v-if="item.children && expandKeys.includes(item.value)" class="pl-9 mt-1">
                <li
                  v-for="sub in item.children"
                  :key="sub.value"
                  class="py-1 block hover:text-indigo-400 text-gray-200 transition"
                  :class="route.path.startsWith(sub.value) ? 'text-indigo-400' : 'text-gray-200'"
                >
                  <router-link :to="sub.value" class="block text-sm">{{ sub.name }}</router-link>
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
      class="fixed inset-0 bg-gray-900 z-30 lg:hidden lg:z-auto transition-opacity duration-200 opacity-0 pointer-events-none"
    >
      <p>wswwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww</p>
      <p>wswwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww</p>
      <p>wswwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww</p>
      <p>wswwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww</p>
      <p>wswwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww</p>
      <p>wswwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww</p>
      <p>wswwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww</p>
      <p>wswwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww</p>
    </div>
  </div>
</template>
