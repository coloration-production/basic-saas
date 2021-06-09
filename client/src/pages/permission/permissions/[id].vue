<script lang="ts">
import { defineComponent, ref, computed, watch, ComponentOptions } from 'vue'
import { useRouter } from 'vue-router'
import { permissionApi } from '~/api'
import { useStatusOptions } from '~/logic'
import { PermissionDto } from '~/types'
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

    const permission = ref<Partial<PermissionDto>>({
      name: '',
      alias: '',
      status: 1,
    })

    const rid = computed(() => Number(props.id) || 0)
    const title = computed(() => rid.value === 0 ? 'Create Permission' : `Edit Permission #${rid.value}`)
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

    watch(rid, () => {
      if (rid.value === 0) return

      permissionApi.get(rid.value)
        .then((res) => {
          const { name, status, alias } = res
          permission.value = { name, status, alias }
        })

      permissionApi.list().then(res => permissionOptions.value = mapOptions(res))
    }, { immediate: true })

    function handleSubmit(e: Event) {
      e.preventDefault()

      // form.value.validate((errors) => {

      // })

      const permissionPromise = rid.value === 0
        ? permissionApi.create(permission.value)
        : permissionApi.modify(rid.value, permission.value)

      permissionPromise.then(() => {
        // console.log(title.value + 'success !')
        router.replace('/permission/permissions')
      })
    }

    return {
      formRef,
      model: permission,
      rid,
      title,
      rules,
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
      <router-link class="btn" to="/permission/permissions">Back</router-link>
    </PageHead>
    <ContentBox class="p-6">
      <div class="lg:w-1/3 md:w-1/2">
        <NForm ref="form" :model="model" :rules="rules">
          <NFormItemRow path="name" label="Name">
            <NInput v-model:value="model.name" @keydown.enter.prevent />
          </NFormItemRow>
          <NFormItemRow path="alias" label="Alias">
            <NInput v-model:value="model.alias" @keydown.enter.prevent />
          </NFormItemRow>
          <NFormItemRow path="status" label="Parent">
            <NSelect v-model:value="model.status" :options="defaultStatusOptions" />
          </NFormItemRow>
        </NForm>

        <div class="flex justify-end">
          <NButton type="primary" @click="handleSubmit">Submit</NButton>
        </div>
      </div>
    </ContentBox>
  </div>
</template>
