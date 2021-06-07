<script lang="ts">
import { defineComponent, ref, computed, watch } from 'vue'
import { useRouter } from 'vue-router'
import { roleApi } from '~/api'
import { RoleDto } from '~/types'

export default defineComponent({
  props: {
    id: {
      type: String,
      default: '0',
    },
  },
  setup(props) {
    const router = useRouter()
    const role = ref<RoleDto>({
      name: '',
      alias: '',
      status: 1,
    } as RoleDto)

    const rid = computed(() => Number(props.id) || 0)
    const title = computed(() => rid.value === 0 ? 'Create Role' : `Edit Role #${rid.value}`)

    watch(rid, () => {
      if (rid.value === 0) return

      roleApi.getRole(rid.value)
        .then(res => {
          role.value = res
        })
    }, { immediate: true })

    function handleSubmit(e: Event) {
      e.preventDefault()

      const rolePromise = rid.value === 0
        ? roleApi.createRole(role.value)
        : roleApi.modifyRole(rid.value, role.value)

      rolePromise.then(() => {
        // console.log(title.value + 'success !')
        router.replace('/permission/roles')
      })
    }

    return {
      role,
      rid,
      title,
      handleSubmit,
    }
  },
})
</script>
<template>
  <div>
    <PageHead :title="title" class="mb-8">
      <router-link class="btn" to="/permission/roles">Back</router-link>
    </PageHead>
    <ContentBox class="p-6">
      <form :onsubmit="handleSubmit">
        <div class="lg:w-1/3 md:w-1/2 w-full">
          <div class="mb-8">
            <label for="name" class="block text-sm font-medium mb-1">Name</label>
            <input id="name" v-model="role.name" type="text" class="w-full outline-none form-input" />
          </div>
          <div class="mb-8">
            <label for="alias" class="block text-sm font-medium mb-1">Alias</label>
            <input
              id="alias"
              v-model="role.alias"
              type="text"
              class="w-full outline-none form-input"
            />
          </div>
          <div class="mb-8">
            <label for="status" class="block text-sm font-medium mb-1">status</label>
            <input
              id="status"
              v-model="role.status"
              type="number"
              class="w-full outline-none form-input"
            />
          </div>
          <div class="flex justify-end">
            <button type="submit" class="btn">Submit</button>
          </div>
        </div>
      </form>
    </ContentBox>
  </div>
</template>
<route lang="yaml">
meta:
  layout: home
</route>
  