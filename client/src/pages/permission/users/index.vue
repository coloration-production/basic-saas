<script lang="ts">
import { defineComponent, ref } from 'vue'
import { userApi } from '~/api'
import { UserDto } from '~/types'

export default defineComponent({
  setup() {
    const users = ref<UserDto[]>([])

    function fetchList() {
      userApi.users().then(res => users.value = res)
    }

    fetchList()

    return {
      users,
    }
  },
})
</script>
<template>
  <div>
    users
    <div v-for="u in users" :key="u.id">
      {{ u }}
    </div>
  </div>
</template>
<route lang="yaml">
meta:
  layout: home
</route>
