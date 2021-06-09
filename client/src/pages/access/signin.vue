<script lang="ts">
import { computed, defineComponent, ref } from 'vue'
import { useRouter } from 'vue-router'
import { accessApi } from '~/api'
import { useUser } from '~/logic'
import { SigninPayload, SigninDto } from '~/types'
export default defineComponent({
  setup() {
    const router = useRouter()
    const { setUser } = useUser()
    const param = ref<SigninPayload>({
      name: 'David',
      pwd: '123456',
    })

    const disabled = computed(() => {
      return param.value.name === '' || param.value.pwd === ''
    })

    function signin(e: Event) {
      e.preventDefault()

      if (disabled.value) return

      accessApi.signin(param.value)
        .then((dto: SigninDto) => {
          setUser(dto)
          router.push('/dashboard')
        })
    }

    return {
      signin,
      param,
      disabled,
    }
  },
})
</script>
<template>
  <div class="flex relative">
    <div
      class="md:w-1/2"
      style="min-height: 100vh"
    >
      <div class="px-4 py-8 w-max-96 mx-auto h-full flex flex-col justify-center">
        <h1 class="text-3xl text-gray-800 font-bold mb-6">
          Welcome back! ✨
        </h1>

        <form @submit="signin">
          <div class="mb-4">
            <label for="name" class="block text-sm font-medium mb-1">
              Username
            </label>
            <input id="name" v-model="param.name" type="text" class="w-full outline-none form-input">
          </div>
          <div class="mb-8">
            <label for="pwd" class="block text-sm font-medium mb-1">
              Password
            </label>
            <input id="pwd" v-model="param.pwd" type="password" class="w-full outline-none form-input">
          </div>
          <div>
            <button type="submit" class="w-full btn" style="outline: none;">Sign In</button>
          </div>
          <div class="divider mt-8 mb-5"></div>
          <div class="text-sm mb-6">
            Don’t you have an account?

            <router-link to="/access/signup" class="link">
              Sign Up
            </router-link>
          </div>
          <div>
            <div class="alert warning">
              <akar-icons-check class="align-middle" />
              <span class="text-sm">
                To support you during the pandemic super pro features are free until March 31st.
              </span>
            </div>
          </div>
        </form>
      </div>
    </div>
    <div class="md:w-1/2 hidden md:block absolute top-0 right-0 bottom-0 bg-gray-300">
      cover
    </div>
  </div>
</template>
<route lang="yaml">
meta:
  layout: empty
</route>
