<template>
  <v-btn icon small outlined @click="signIn">
    <v-icon small color="red">mdi-google</v-icon>
  </v-btn>
</template>

<script>
import Auth from '@/plugins/auth'
export default {
  data: () => ({
    GoogleAuth: null
  }),
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

        auth2.then(f => {
          this.GoogleAuth = f
        })

        // auth2.attachClickHandler('google-signin-button', {},
        //   this.onsuccess,
        //   this.onfailure
        // )
      })
    },
    signIn () {
      // eslint-disable-next-line no-undef
      // var isSignedIn = this.GoogleAuth.isSignedIn.get()

      // if (isSignedIn) {
      //   this.onsuccess()
      // } else {
      this.GoogleAuth.signIn()
        .then((d) => {
          this.onsuccess(d)
        }).catch(e => {
          this.authFailed(e)
        })
      // }
    },
    onsuccess (e) {
      var GoogleUser = this.GoogleAuth.currentUser.get()
      var userData = GoogleUser.getAuthResponse(true)
      Auth.authenticateWithBackend('google', userData.id_token)
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
