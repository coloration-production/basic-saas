<script lang="ts">
import { defineComponent, onBeforeUnmount, ref, watchEffect } from 'vue'
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
    <iframe
      ref="videoRender"
      :src="`/liveplayer/index.html?url=${url}`"
      style="width:100%; height:35rem;"
      frameborder="no"
      border="0"
    />
  </div>
</template>
