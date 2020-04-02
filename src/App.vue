<template>
  <div>
    <router-view/>
    <notifications group="auth" />
    <notifications group="app" />
  </div>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  })
}
</script>
<style lang="scss">
  html {
    overflow-y: auto !important;
  }
  .vue-notification {
    &.success {
      background: 'green'
    }
  }
</style>
