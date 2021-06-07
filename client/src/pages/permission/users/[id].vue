<script lang="ts">
import { defineComponent, ref, computed, watch } from 'vue'
import { useRouter } from 'vue-router'
import { userApi } from '~/api'
import { UserDto } from '~/types'

export default defineComponent({
  props: {
    id: {
      type: String,
      default: '0',
    },
  },
  setup(props) {
    const router = useRouter()
    const user = ref<Partial<UserDto>>({
      name: '',
      role_id: 1,
      status: 1,
    })

    const uid = computed(() => Number(props.id) || 0)
    const title = computed(() => uid.value === 0 ? 'Create User' : `Edit User #${uid.value}`)

    watch(uid, () => {
      if (uid.value === 0) return

      userApi.getUser(uid.value)
        .then((res) => {
          const { name, role_id, status } = res

          user.value = {
            name, role_id, status,
          }
        })
    }, { immediate: true })

    function handleSubmit(e: Event) {
      e.preventDefault()

      const userPromise = uid.value === 0
        ? userApi.createUser(user.value)
        : userApi.modifyUser(uid.value, user.value)

      userPromise.then(() => {
        // console.log(title.value + 'success !')
        router.replace('/permission/users')
      })
    }

    return {
      user,
      uid,
      title,
      handleSubmit,
    }
  },
})
</script>
<template>
  <div>
    <PageHead :title="title" class="mb-8">
      <router-link class="btn" to="/permission/users">Back</router-link>
    </PageHead>
    <ContentBox class="p-6">
      <form :onsubmit="handleSubmit">
        <div class="lg:w-1/3 md:w-1/2 w-full">
          <div class="mb-8">
            <label for="name" class="block text-sm font-medium mb-1">Name</label>
            <input id="name" v-model="user.name" type="text" class="w-full outline-none form-input" />
          </div>
          <div class="mb-8">
            <label for="role" class="block text-sm font-medium mb-1">Role</label>
            <input
              id="role"
              v-model="user.role_id"
              type="number"
              class="w-full outline-none form-input"
            />
          </div>
          <div class="mb-8">
            <label for="status" class="block text-sm font-medium mb-1">status</label>
            <input
              id="status"
              v-model="user.status"
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
