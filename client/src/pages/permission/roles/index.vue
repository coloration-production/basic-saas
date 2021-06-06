<script lang="ts">
import { defineComponent, ref } from 'vue'
import { roleApi } from '~/api'
import { RoleDto } from '~/types'

export default defineComponent({
  setup() {
    const roles = ref<RoleDto[]>([])

    function fetchList() {
      roleApi.roles().then(res => roles.value = res)
    }

    fetchList()

    return {
      roles,
    }
  },
})
</script>
<template>
  <div>
    roles
    <div v-for="r in roles" :key="r.id">{{ r }}</div>
  </div>
</template>
<route lang="yaml">
meta:
  layout: home
</route>
