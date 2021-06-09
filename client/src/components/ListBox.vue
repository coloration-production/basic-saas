<script lang="ts">
import { ref } from 'vue'
import {
  Listbox,
  ListboxButton,
  ListboxOptions,
  ListboxOption,
} from '@headlessui/vue'

export default {
  components: {
    Listbox,
    ListboxButton,
    ListboxOptions,
    ListboxOption,
  },

  setup() {
    const people = [
      { name: 'Wade Cooper' },
      { name: 'Arlene Mccoy' },
      { name: 'Devon Webb' },
      { name: 'Tom Cook' },
      { name: 'Tanya Fox' },
      { name: 'Hellen Schmidt' },
    ]
    const selectedPerson = ref(people[0])

    return {
      people,
      selectedPerson,
    }
  },
}
</script>

<template>
  <div>
    <Listbox v-model="selectedPerson">
      <div class="relative mt-1">
        <ListboxButton class="list-box-button">
          <span class="block truncate">{{ selectedPerson.name }}</span>
          <span class="absolute inset-y-0 right-0 flex items-center pr-2 pointer-events-none">
            <heroicons-outline-selector class="w-5 h-5 text-gray-400 font-thin" aria-hidden="true" />
          </span>
        </ListboxButton>

        <transition
          leave-active-class="transition duration-100 ease-in"
          leave-from-class="opacity-100"
          leave-to-class="opacity-0"
        >
          <ListboxOptions class="list-box-options">
            <ListboxOption
              v-for="person in people"
              v-slot="{ active, selected }"
              :key="person.name"
              :value="person"
              as="template"
            >
              <li
                :class="[
                  active ? 'text-indigo-900 bg-indigo-100' : 'text-gray-900',
                  'cursor-default select-none relative py-2 pl-10 pr-4 focus:outline-none',
                ]"
              >
                <span
                  :class="[
                    selected ? 'font-medium' : 'font-normal',
                    'block truncate',
                  ]"
                >{{ person.name }}</span>
                <span
                  v-if="selected"
                  class="absolute inset-y-0 left-0 flex items-center pl-3 text-indigo-600"
                >
                  <akar-icons-check class="w-4 h-4" aria-hidden="hidden" />
                </span>
              </li>
            </ListboxOption>
          </ListboxOptions>
        </transition>
      </div>
    </Listbox>
  </div>
</template>
<style lang="postcss" scoped>
.list-box-button {
  @apply
    relative
    w-full py-2 pl-3 pr-10
    text-left sm:text-sm cursor-default leading-5
    rounded-sm border
    focus:outline-none focus:border-indigo-500;
}

.list-box-options {
  @apply
    absolute
    w-full py-1 mt-1 overflow-auto max-h-60
    sm:text-sm
    bg-white rounded-sm shadow-lg ring-1 ring-black ring-opacity-5
    focus:outline-none;
}
</style>
