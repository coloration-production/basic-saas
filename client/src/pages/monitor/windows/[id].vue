<script lang="ts">
import { defineComponent, ref, computed, watch, ComponentOptions } from 'vue'
import { useRouter } from 'vue-router'
import { windowApi } from '~/api'
import { useStatusOptions } from '~/logic'
import { WindowDto } from '~/types'
import { mapOptions } from '~/util'
export default defineComponent({
  props: {
    id: {
      type: String,
      default: '0',
    },
  },
  setup(props) {
    const router = useRouter()
    const formRef = ref(null)

    const { defaultOptions } = useStatusOptions()

    const window = ref<Partial<WindowDto>>({
      name: '',
      status: 1,
      layout: '',
      widgets: [],
    })

    const size = ref<number[]>([2, 2])

    const rid = computed(() => Number(props.id) || 0)
    const title = computed(() => rid.value === 0 ? 'Create Window' : `Edit Window #${rid.value}`)
    const permissionOptions = ref<ComponentOptions>([])
    const fullscreenSign = ref(false)
    const rules = {
      name: [
        {
          required: true,
          message: 'require name',
          trigger: ['input', 'blur'],
        },
      ],
    }

    watch(rid, () => {
      if (rid.value === 0) return

      windowApi.get(rid.value)
        .then((res) => {
          const { name, status, widgets } = res
          window.value = { name, status, widgets }
        })
    }, { immediate: true })

    function handleSubmit(e: Event) {
      e.preventDefault()

      // form.value.validate((errors) => {

      // })

      const windowPromise = rid.value === 0
        ? windowApi.create(window.value)
        : windowApi.modify(rid.value, window.value)

      windowPromise.then(() => {
        // console.log(title.value + 'success !')
        router.replace('/monitor/windows')
      })
    }

    function setFullscreen() {
      fullscreenSign.value = true
    }

    return {
      formRef,
      model: window,
      rid,
      title,
      rules,
      size,
      fullscreenSign,
      setFullscreen,
      handleSubmit,
      defaultStatusOptions: mapOptions(defaultOptions),
      permissionOptions,
    }
  },
})
</script>
<template>
  <div>
    <PageHead :title="title" class="mb-8">
      <router-link to="/monitor/windows">
        <NButton type="primary">Back</NButton>
      </router-link>
    </PageHead>
    <ContentBox class="p-6 flex md:flex-row flex-col">
      <div class="lg:w-1/3 md:w-1/2">
        <NForm ref="form" :model="model" :rules="rules">
          <NFormItemRow path="name" label="Name">
            <NInput v-model:value="model.name" @keydown.enter.prevent />
          </NFormItemRow>
          <NFormItemRow path="status" label="Status">
            <NSelect v-model:value="model.status" :options="defaultStatusOptions" />
          </NFormItemRow>

          <NFormItemRow path="size" label="Size">
            <NInput type="number" v-model:value="size[0]" />
            <span class="mx-6">*</span>
            <NInput type="number" v-model:value="size[1]" />
          </NFormItemRow>
        </NForm>
        <div class="flex justify-end">
          <NButton type="primary" @click="handleSubmit">Submit</NButton>
        </div>
      </div>
      <div class="flex-1 md:pl-6">
        <div class="pb-1 flex justify-between items-center">
          <span>Preview</span>
          <fluent:arrow-expand-24-regular @click="setFullscreen" />
        </div>
        <div
          :class="{ 'full-screen': fullscreenSign }"
          class="border-t border-l h-120 border-gray-200 rounded-sm overflow-hidden clearfix"
        >
          <div
            v-for="i in size[0] * size[1]"
            :key="i"
            class="relative float-left border-gray-200 border-r border-b"
            :style="{ width: 100 / size[0] + '%', height: 100 / size[1] + '%' }"
          >
            <div
              v-if="i > model.widgets?.length"
              class="absolute inset-0 flex justify-center items-center hover:bg-gray-200 group"
            >
              <akar-icons-circle-plus class="text-2xl text-gray-300 group-hover:text-gray-500" />
            </div>
            <div class="absolute inset-0" v-else>
              <div v-if="model.widgets[i-1].type === 1" class="absolute inset-0">
                <iframe :src="model.widgets[i-1].url" class="h-full w-full" />
              </div>
              <div v-else>
                <CameraPlayer :url="model.widgets[i-1].info?.src" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </ContentBox>
  </div>
</template>
<style scoped lang="postcss">
.full-screen {
  @apply fixed inset-0 z-50;
  height: 100vh;
}
</style>