<script lang="ts">
import { defineComponent, ref } from 'vue'
import { permissionApi } from '~/api'
import { PermissionDto } from '~/types'

export default defineComponent({
  setup() {
    const permissions = ref<PermissionDto[]>([])

    function fetchList() {
      permissionApi.list().then(res => permissions.value = res)
    }

    fetchList()

    return {
      permissions,
    }
  },
})
</script>
<template>
  <div>
    <PageHead title="Permission" class="mb-8">
      <router-link to="/permission/permissions/0">
        <NButton type="primary">Add Permission</NButton>
      </router-link>
    </PageHead>
    <ContentBox>
      <header class="px-5 py-4 flex justify-between items-center">
        <h2 class="font-semibold">
          All Permission
          <span class="font-medium text-blue-gray-400">{{ permissions.length }}</span>
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
            <tr v-for="p in permissions" :key="p.id">
              <td class="p-2 whitespace-nowrap font-semibold text-left">{{ p.id }}</td>
              <td class="p-2 whitespace-nowrap font-semibold text-left">{{ p.alias }} {{ p.name }}</td>
              <td class="p-2 whitespace-nowrap font-semibold text-left">
                <router-link :to="`/permission/permissions/${p.id}`">Edit</router-link>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </ContentBox>
  </div>
</template>
