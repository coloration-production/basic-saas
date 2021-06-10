<script lang="ts">
import { defineComponent, ref, computed, watch, ComponentOptions } from 'vue'
import { useRouter } from 'vue-router'
import { permissionApi, roleApi } from '~/api'
import { useStatusOptions } from '~/logic'
import { RoleDto } from '~/types'
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

    const role = ref<Partial<RoleDto>>({
      name: '',
      alias: '',
      status: 1,
      permissions: [],
    })

    const rid = computed(() => Number(props.id) || 0)
    const title = computed(() => rid.value === 0 ? 'Create Role' : `Edit Role #${rid.value}`)
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

      roleApi.get(rid.value)
        .then((res) => {
          const { name, status, alias } = res
          role.value = { name, status, alias }
        })

      permissionApi.list().then(res => permissionOptions.value = mapOptions(res, 'alias', 'id'))
    }, { immediate: true })

    function handleSubmit(e: Event) {
      e.preventDefault()

      // form.value.validate((errors) => {

      // })

      const rolePromise = rid.value === 0
        ? roleApi.create(role.value)
        : roleApi.modify(rid.value, role.value)

      rolePromise.then(() => {
        // console.log(title.value + 'success !')
        router.replace('/permission/roles')
      })
    }

    return {
      formRef,
      model: role,
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
      <router-link to="/permission/roles">
        <NButton type="primary">Back</NButton>
      </router-link>
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
          <NFormItemRow path="permissions" label="Permissions">
            <NSelect v-model:value="model.permissions" :options="permissionOptions" multiple />
          </NFormItemRow>
          <NFormItemRow path="status" label="Status">
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
