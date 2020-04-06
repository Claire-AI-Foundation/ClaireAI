<template>
  <span class="facebook-login-button">
    <v-btn
      icon
      outlined
      small
      class="mr-3"
      @click="openPopup"
    >
      <v-icon small color="primary">mdi-facebook</v-icon>
    </v-btn>
  </span>
</template>

<script>
import Auth from '@/plugins/auth'
import jwtDecode from 'jwt-decode'

export default {
  methods: {
    mountScript () {
      var el = document.createElement('script')
      el.setAttribute('src', '//connect.facebook.net/en_US/sdk.js')
      var fbs = document.head.appendChild(el)
      fbs.onload = this.initScript
    },
    initScript () {
      // eslint-disable-next-line no-undef
      FB.init({
        appId: process.env.VUE_APP_FACEBOOK_APP_ID,
        xfbml: true,
        version: 'v3.1'
      })
      // eslint-disable-next-line no-undef
      // FB.logout()
    },
    openPopup () {
      // eslint-disable-next-line no-undef
      FB.login((facebookResponse) => {
        if (facebookResponse.status === 'connected') {
          let resp = facebookResponse.authResponse
          console.log(jwtDecode(resp.accessToken))
          // console.log(facebookResponse.authResponse)
          this.onsuccess(resp.accessToken)
        } else {
          // authFailed()
        }
      })
    },
    onsuccess (accessToken) {
      console.log(accessToken)
      Auth.authenticateWithBackend(accessToken)
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
