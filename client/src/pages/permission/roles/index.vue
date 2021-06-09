<script lang="ts">
import { defineComponent, ref } from 'vue'
import { permissionApi, roleApi } from '~/api'
import { useStatusOptions } from '~/logic'
import { PermissionDto, RoleDto } from '~/types'
import { filterNameByOptions } from '~/util'

export default defineComponent({
  setup() {
    const roles = ref<RoleDto[]>([])
    const permissions = ref<PermissionDto[]>([])
    const { defaultOptions } = useStatusOptions()

    function fetchList() {
      roleApi.list().then(res => roles.value = res)
      permissionApi.list().then(res => permissions.value = res)
    }

    function permissionFilter(id: PermissionDto['id']) {
      return filterNameByOptions(permissions.value, 'name', 'id')(id)
    }

    fetchList()

    return {
      roles,
      statusFilter: filterNameByOptions(defaultOptions),
      permissionFilter,
    }
  },
})
</script>
<template>
  <div>
    <PageHead title="Role" class="mb-8">
      <router-link to="/permission/roles/0">
        <NButton type="primary">Create Role</NButton>
      </router-link>
    </PageHead>

    <ContentBox>
      <header class="px-5 py-4 flex justify-between items-center">
        <h2 class="font-semibold">
          All Roles
          <span class="font-medium text-blue-gray-400">{{ roles.length }}</span>
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
              <th class="p-2 whitespace-nowrap font-semibold text-left">status</th>
              <th class="p-2 whitespace-nowrap font-semibold text-left">permissions</th>
              <th class="p-2 whitespace-nowrap font-semibold text-left">operation</th>
            </tr>
          </thead>
          <tbody class="text-sm divide-y divide-gray-100">
            <tr v-for="r in roles" :key="r.id">
              <td class="p-2 whitespace-nowrap font-semibold text-left">{{ r.id }}</td>
              <td class="p-2 whitespace-nowrap font-semibold text-left">{{ r.alias }} {{ r.name }}</td>
              <td class="p-2 whitespace-nowrap font-semibold text-left">{{ statusFilter(r.status) }}</td>
              <td class="p-2 whitespace-nowrap font-semibold text-left">
                <span v-for="p in r.permissions" :key="p">{{ permissionFilter(p) }}</span>
              </td>
              <td class="p-2 whitespace-nowrap font-semibold text-left">
                <router-link :to="`/permission/roles/${r.id}`">Edit</router-link>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </ContentBox>
  </div>
</template>
