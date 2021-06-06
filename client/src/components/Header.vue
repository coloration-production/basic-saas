<script setup lang="ts">
import { useToggle } from '@vueuse/core'
import { computed, watch } from 'vue-demi'
import { useRouter } from 'vue-router'
import { accessApi } from '~/api'
import { useUser } from '~/logic'

const router = useRouter()
const [dropVisible, dropToggle] = useToggle(false)
const { userInfo, clearUser, noUser } = useUser()
const user = computed(() => userInfo.value.user || {})

watch(userInfo, () => {
  noUser() && router.replace('/access/signin')
}, { immediate: true })

function signout() {
  accessApi.signout().then(clearUser)
}
</script>
<template>
  <header class="sticky top-0 bg-white border-b border-gray-200 z-30">
    <div class="px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16 -mb-px">
        <div class="flex">
          <button
            class="text-gray-500 hover:text-gray-600 lg:hidden hidden-outline"
            aria-controls="sidebar"
            aria-expanded="false"
          >
            <bx-bx-menu class="text-2xl" />
          </button>
        </div>
        <div class="flex items-center">
          <div>
            <button
              class="w-8 h-8 flex items-center justify-center bg-gray-100 hover:bg-gray-200 transition duration-150 rounded-full ml-3 false"
              aria-controls="search-modal"
              style="outline: none;"
            >
              <eva-search-fill />
            </button>
            <div
              class="fixed inset-0 bg-gray-900 bg-opacity-30 z-50 transition-opacity exit-done"
              aria-hidden="true"
              style="display: none;"
            ></div>
          </div>
          <hr class="w-px h-6 bg-gray-200 mx-3" />
          <div class="relative inline-flex">
            <button
              class="inline-flex justify-center items-center group hidden-outline"
              aria-haspopup="true"
              aria-expanded="false"
              @click="dropToggle"
            >
              <img
                class="w-8 h-8 rounded-full"
                src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAIAAAAlC+aJAAAD/ElEQVR4Ae2axXorRxCFq+by3VyT2NkENTecrC4zMz5A3sIw3mUXfoLQNsywCTOzMSiIhWZ7ZrpSU25NmGFGX/p8UneV8Pzq023E63edg3aWBVHIABgAA2AADIABMAAGwAAYAANw9VU39HTbbQzgurNbNvdv2zKQ6LHbEqBYfAsBerrz27b0b98mGO0FUG+MLi42AJFrdr9je//OHYPJhN1Om7hQehuImCEYAZOJ/M4dA7t2DqaSdnsAFEtvE0+BeQwmaVLJ/O5dA3v2CEbMASqVjzxvQawHEAKCXLJSCXvvnoF9+5x0yo4vgFJe+dv3CMQ4sAQkkCwIYipx2b59gwcOCEYMAeQselPME0tAQNTaGNJzqA4eHDx4yMmk7dgBlMvvKd+TJcBl51oUVrpIJ/OHDg0ePuxkMnaMAFxvfrL6MZBsgnA/i3QlM2kezKTzR444R486WcGIGkBUKLzV8qgllUzCxQPKLuFeWuJFOHp08NhxJ5u1owcold5CvY918kH6oAmF4UCo78dcxj5xwuFLLmdHCTC/0KjVRmUF9L5FSZNuxDFJp4VIROHj2f3Jk0OnTju9ghEBAKtQfDtcAVG4CsGgG11ryp88PpfdyAxnzg719m6MAqDwpvgKP2nkWawShkAo+QlZfunxuWz+7Fnn7PmhC/4Yxkr4h6SIFmZ5EPlKEciVS1KuxyVXvk++y6PyPd/3lL64ynU9Hj3X95Y8d8lnGG/F1wsrp8H6DwHSqesBqJVsZCJEUhRwoGUBIykgkHv0GMzyYFkTIrmbrX+zsPJFz/oKRP8dQCp5HeiDkidFSodFWEhnXbWSREIgt+IyE+IifDFjPb+04ssINvHaNR2dnRcF7nTukaVDjhZpKtAi7Tx8+IL/RWXprpq6dwm/d/+frkA6dR0p0oenUmISpBNJQlQAoS+Ss4Bj1p2oTD87701AqIgArkcLKYi5nJhIIsGAAAmxFSENB7OL46Xa07NL4yCKEmDVynXdnbYEwyImQFRilIH0kW9ZchgBWgA+TM+PFSaf4BFE0QMkE1ezRUAdaH2qy74Ux0ra4NqcHv2q9PjU7Gi8vp1OZ663GACAlAq//xEICb5lcd+YHvlo5PaPxu7Q7uMDYFkrE91XinVAxiC9AgIRDI2p4Xc+vvm9T29tzIzAzxV5hHq6L1+1ar18/CTBRzn1iYHqzeHRiYfqzc8gVOwA5ADFIOcKEclXgMCqNYdHxh6sNbT1WANkUtcSkYW4nKdK7dOR0Qeq9U9BFHeAjo6LV6/pANFk9dOR4ftD620BIN/AIVYqnwyP3F+taevtBLB69fpXXrmxItajkvl/IQNgAAyAATAABsAAGAADYAD+vwDfAQSHHlNp5b1mAAAAAElFTkSuQmCC"
                width="32"
                height="32"
                alt="User"
              />
              <div class="flex items-center truncate">
                <span
                  class="truncate ml-2 text-sm font-medium group-hover:text-gray-800"
                >{{ user.name }}</span>
                <akar-icons-chevron-down class="text-sm" />
              </div>
            </button>
            <div
              v-show="dropVisible"
              class="origin-top-right z-10 absolute top-full right-0 min-w-44 bg-white border border-gray-200 py-1.5 rounded shadow-lg overflow-hidden mt-1 exit-done"
            >
              <div>
                <div class="pt-0.5 pb-2 px-3 mb-1 border-b border-gray-200">
                  <div class="font-medium text-gray-800">{{ user.name }}</div>
                  <div class="text-xs text-gray-500 italic">Administrator</div>
                </div>
                <ul>
                  <li>
                    <router-link
                      class="font-medium text-sm text-indigo-500 hover:text-indigo-600 flex items-center py-1 px-3"
                      to="/settings"
                      @click="dropToggle"
                    >Settings</router-link>
                  </li>
                  <li>
                    <a
                      class="font-medium text-sm text-indigo-500 hover:text-indigo-600 flex items-center py-1 px-3"
                      @click="signout"
                    >Sign Out</a>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>
