<template>
  <n-form :model="model" ref="form" :rules="rules">
    <n-form-item-row path="age" label="年龄">
      <n-input v-model:value="model.age" @keydown.enter.prevent />
    </n-form-item-row>
  </n-form>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'

export default defineComponent({
  setup() {
    const formRef = ref(null)
    const modelRef = ref({
      age: null,
    })

    return {
      formRef,
      model: modelRef,
      rules: {
        age: [
          {
            required: true,
            message: '需要年龄2',
            trigger: ['input', 'blur'],
          },
        ],
      },
    }
  },
})
</script>