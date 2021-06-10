<script lang="ts">
import { defineComponent, ref } from 'vue'
import { userApi } from '~/api'
import { UserDto } from '~/types'
import { useStatusOptions } from '~/logic'
import { filterNameByOptions } from '~/util'

export default defineComponent({
  setup() {
    const users = ref<UserDto[]>([])
    const { defaultOptions } = useStatusOptions()

    function fetchList() {
      userApi.list().then(res => users.value = res)
    }

    fetchList()

    return {
      users,
      statusFilter: filterNameByOptions(defaultOptions),

    }
  },
})
</script>
<template>
  <div>
    <PageHead title="User" class="mb-8">
      <router-link to="/permission/users/0">
        <Button>Add User</Button>
      </router-link>
    </PageHead>
    <ContentBox>
      <header class="px-5 py-4 flex justify-between items-center">
        <h2 class="font-semibold">
          All Users
          <span class="font-medium text-blue-gray-400">{{ users.length }}</span>
        </h2>
        <div class="pagination text-blue-gray-300 text-sm">
          <ul class="flex">
            <li v-for="i in 5" :key="i" class="px-0.5" >
              {{ i }}
            </li>
          </ul>
        </div>
      </header>
      <div class="p-3 border-t border-gray-100">
        <table class="w-full table-auto">
          <thead class="text-xs font-semibold uppercase text-gray-500 bg-gray-50">
            <tr>
              <th class="p-2 whitespace-nowrap font-semibold text-left">id</th>
              <th class="p-2 whitespace-nowrap font-semibold text-left">name</th>
              <th class="p-2 whitespace-nowrap font-semibold text-left">role</th>
              <th class="p-2 whitespace-nowrap font-semibold text-left">status</th>
              <th class="p-2 whitespace-nowrap font-semibold text-left">operation</th>
            </tr>
          </thead>
          <tbody class="text-sm divide-y divide-gray-100">
            <tr v-for="u in users" :key="u.id">
              <td class="p-2 whitespace-nowrap font-semibold text-left">{{ u.id }}</td>
              <td class="p-2 whitespace-nowrap font-semibold text-left">{{ u.name }}</td>
              <td class="p-2 whitespace-nowrap font-semibold text-left">{{ u.role.alias }} {{ u.role.name }}</td>
              <td class="p-2 whitespace-nowrap font-semibold text-left">{{ statusFilter(u.status) }}</td>
              <td class="p-2 whitespace-nowrap font-semibold text-left">
                <router-link :to="`/permission/users/${u.id}`">Edit</router-link>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </ContentBox>
  </div>
</template>
