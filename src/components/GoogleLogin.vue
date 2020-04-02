<template>
  <v-btn icon small outlined id="google-signin-button">
    <v-icon small color="red">mdi-google</v-icon>
  </v-btn>
</template>

<script>
import Auth from '@/plugins/auth'
export default {
  methods: {
    mountScript () {
      var el = document.createElement('script')
      el.setAttribute('src', 'https://apis.google.com/js/api:client.js')
      document.head.appendChild(el)
      el.onload = this.initScript
    },
    initScript () {
      // eslint-disable-next-line no-undef
      gapi.load('auth2', (g) => {
        // eslint-disable-next-line no-undef
        var auth2 = gapi.auth2.init({
          client_id: process.env.VUE_APP_GOOGLE_CLIENT_ID
        })

        auth2.attachClickHandler('google-signin-button', {},
          this.onsuccess,
          this.onfailure
        )
      })
    },
    onsuccess (e) {
      Auth.authenticateWithBackend(e.uc.id_token)
        .then((d) => {
          this.$router.push('/')
        }).catch(err => console.log(err))
    },
    authFailed (e) {
      //
    }
  },
  mounted () {
    this.mountScript()
  }
}
</script>
