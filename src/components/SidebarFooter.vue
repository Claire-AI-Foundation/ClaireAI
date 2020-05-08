<template>
  <div class=" mt-4 px-2 text-right" v-show="!mini">
    <v-btn class="px-1 text-normal" x-small text to="help">Help</v-btn>
    <v-btn class="px-1 text-normal" x-small text to="/terms">Terms</v-btn>
    <v-btn class="px-1 text-normal" x-small text to="/privacy-policy">Privacy policy</v-btn>
    <v-btn class="px-1 text-normal" x-small text @click="$store.dispatch('logout')">Logout</v-btn>
    <br>
    <v-btn class="px-3 text-normal" x-small text> &copy; 2020 Claire-ai Foundation </v-btn>
  </div>
</template>

<script>
export default {
  props: ['mini']
}
</script>
