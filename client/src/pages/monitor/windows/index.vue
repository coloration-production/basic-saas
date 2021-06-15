<script lang="ts">
import { defineComponent, ref } from 'vue'
import { windowApi } from '~/api'
import { WindowDto } from '~/types'

export default defineComponent({
  setup() {
    const windows = ref<WindowDto[]>([])

    function fetchList() {
      windowApi.list().then(res => windows.value = res)
    }

    fetchList()

    return {
      windows,
    }
  },
})
</script>
<template>
  <div>
    <PageHead title="Window" class="mb-8">
      <router-link to="/monitor/windows/0">
        <NButton type="primary">Add Window</NButton>
      </router-link>
    </PageHead>
    <ContentBox>
      <header class="px-5 py-4 flex justify-between items-center">
        <h2 class="font-semibold">
          All Windows
          <span class="font-medium text-blue-gray-400">{{ windows.length }}</span>
        </h2>
        <div class="pagination text-blue-gray-300 text-sm">
          <ul class="flex">
            <li v-for="i in 5" :key="i" class="px-0.5">{{ i }}</li>
          </ul>
        </div>
      </header>
      <div class="p-3 border-t border-gray-100">
        <table class="w-full table-auto">
          <thead class="text-xs font-semibold uppercase text-gray-500 bg-gray-50">
            <tr>
              <th class="p-2 whitespace-nowrap font-semibold text-left">id</th>
              <th class="p-2 whitespace-nowrap font-semibold text-left">name</th>
              <th class="p-2 whitespace-nowrap font-semibold text-left">operation</th>
            </tr>
          </thead>
          <tbody class="text-sm divide-y divide-gray-100">
            <tr v-for="item in windows" :key="item.id">
              <td class="p-2 whitespace-nowrap font-semibold text-left">{{ item.id }}</td>
              <td class="p-2 whitespace-nowrap font-semibold text-left">{{ item.name }}</td>
              <td class="p-2 whitespace-nowrap font-semibold text-left">
                <router-link :to="`/monitor/windows/${item.id}`">Edit</router-link>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </ContentBox>
  </div>
</template>
