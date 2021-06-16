<script lang="ts">
import { computed, defineComponent, onBeforeUnmount, ref, watchEffect } from 'vue'
// import 'videojs-flvjs-es6'

export default defineComponent({
  props: {
    url: {
      type: String,
      default: null,
    },
    autoplay: {
      type: Boolean,
      default: false,
    },
  },
  setup(props) {
    const videoRef = ref<HTMLVideoElement>()
    // const player = ref<any>(null)
    function disposeLastPlayer() {
      // if (player.value) player.value.dispose()
    }

    watchEffect(() => {
      if (props.url === null || !videoRef.value) return
      const address = `${import.meta.env.VITE_MEDIA_URL}${props.url}`
      window.console.log('liveing address', address)
      videoRef.value.setAttribute('video-url', address)
      disposeLastPlayer()
    })

    onBeforeUnmount(() => {
      disposeLastPlayer()
    })

    return {
      video: videoRef,
    }
  },
})

</script>
<template>
  <div class="h-full w-full">
    <!-- import global js in /index.html capture 'live-player' tag -->
    <live-player
      ref="video"
      live="true"
      stretch="true"
      show-custom-button="false"
      autoplay
    />
  </div>
</template>
