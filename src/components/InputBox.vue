<template>
  <v-footer app inset class="mx-md-12 white">
    <v-text-field
      v-if="mode == 'text'"
      name="chatbox"
      label=""
      single-line
      outlined
      v-model="userInput"
      placeholder="Reply"
      :disabled="disabled"
    ></v-text-field>
    <v-select
      v-if="mode == 'select'"
      name="selectbox"
      single-line
      outlined
      chips
      :items="items"
      :multiple="true"
      clearable
      v-model="userInput"
      placeholder="Reply"
      append-outer-icon="mdi-send"
      :disabled="disabled"
      @click:append-outer="submit"
    >
      <template v-slot:selection="{ item, index }">
        <v-chip v-if="index < limit">
          <span>{{ item }}</span>
        </v-chip>
        <span
          v-if="userInput.length > limit && index === (userInput.length - 1)"
          class="grey--text caption"
        >(+{{ userInput.length - limit }} others)</span>
      </template>
    </v-select>
  </v-footer>
</template>

<script>
export default {
  data: () => ({
    userInput: '',
    disabled: false
  }),
  props: {
    mode: {
      type: String,
      default: 'select'
    },
    items: {
      default: function () { return [] }
    },
    disableInput: {
      default: false
    }
  },
  watch: {
    disableInput (to) {
      this.disabled = to
    }
  },
  computed: {
    limit () {
      return this.$vuetify.breakpoint.smAndUp
        ? 4 : 2
    }
  },
  methods: {
    submit (e) {
      const msg = this.mode === 'select' ? this.userInput.join(', ') : this.userInput
      this.$emit('oninput', msg)
      this.disabled = true
    }
  }
}
</script>
