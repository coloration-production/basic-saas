<script lang="ts">
import { defineComponent, ref, computed, watch, ComponentOptions } from 'vue'
import { useRouter } from 'vue-router'
import { widgetApi } from '~/api'
import { useStatusOptions } from '~/logic'
import { WidgetDto } from '~/types'
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

    const model = ref<Partial<WidgetDto>>({
      name: '',
      url: '',
      status: 1,
      type: 1,
    })

    const info = ref<any>({
      src: '',
    })

    const id = computed(() => Number(props.id) || 0)
    const title = computed(() => id.value === 0 ? 'Create Widget' : `Edit Widget #${id.value}`)
    const permissionOptions = ref<ComponentOptions>([])
    const rules = {
      name: [
        {
          required: true,
          message: 'require name',
          trigger: ['input', 'blur'],
        },
      ],
    }

    watch(id, () => {
      if (id.value === 0) return

      widgetApi.get(id.value)
        .then((res) => {
          const { name, status, url, type, info: infomation } = res
          model.value = { name, status, url, type }
          info.value = infomation
        })
    }, { immediate: true })

    function handleSubmit(e: Event) {
      e.preventDefault()

      // form.value.validate((errors) => {

      // })
      const params = Object.assign({}, model.value)
      delete params.info
      const widgetPromise = id.value === 0
        ? widgetApi.create(params)
        : widgetApi.modify(id.value, params)

      widgetPromise.then(() => {
        // console.log(title.value + 'success !')
        router.replace('/monitor/widgets')
      })
    }

    function playCamera() {
      //
    }

    return {
      formRef,
      model,
      title,
      rules,
      info,
      handleSubmit,
      defaultStatusOptions: mapOptions(defaultOptions),
      permissionOptions,
      playCamera,
    }
  },
})
</script>
<template>
  <div>
    <PageHead :title="title" class="mb-8">
      <router-link to="/monitor/widgets">
        <NButton type="primary">Back</NButton>
      </router-link>
    </PageHead>
    <ContentBox class="p-6 flex md:flex-row flex-col">
      <div class="lg:w-1/3 md:w-1/2">
        <NForm ref="form" :model="model" :rules="rules">
          <NFormItemRow path="name" label="Name">
            <NInput v-model:value="model.name" @keydown.enter.prevent />
          </NFormItemRow>
          <NFormItemRow path="url" label="URL">
            <NInput v-model:value="model.url" @keydown.enter.prevent />
          </NFormItemRow>
          <NFormItemRow path="tyoe" label="Type">
            <NSelect v-model:value="model.type" :options="[{ label: 'website', value: 1 }, { label: 'camera', value: 2 }]" />
          </NFormItemRow>
          <NFormItemRow path="status" label="Status">
            <NSelect v-model:value="model.status" :options="defaultStatusOptions" />
          </NFormItemRow>
        </NForm>

        <div class="flex justify-end">
          <NButton type="primary" @click="handleSubmit">Submit</NButton>
        </div>

        <div class="border-t border-gray-200 my-4 md:hidden"></div>
      </div>

      <div class="flex-1 md:pl-4">
        <div class="pb-1">Preview</div>

        <div class="border min-h-86 border-gray-200 rounded-sm overflow-hidden flex items-stretch">
          <iframe
            v-if="model.type === 1"
            class="flex-1 min-h-86"
            frameborder="no"
            border="0"
            :src="model.url"
          />
          <CameraPlayer v-else :url="info?.src" />
        </div>
      </div>
    </ContentBox>
  </div>
</template>
