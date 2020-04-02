<template>
  <div class="main login">
    <v-row justify="center">
      <v-col cols="12" sm="5" md="6">
        <v-form>
          <v-card height="500" class="mt-9" flat tile>
            <v-row no-gutters>
              <v-col cols="12" sm="6">
                <v-card-text class="">

                  <div class="title primary--text text-capitalize"
                    :class="[{'my-5': state == 'signup', 'my-12': state == 'login'}]"
                  >
                    {{state}}
                  </div>
                  <v-text-field
                    name="name"
                    label="Name"
                    color="primary"
                    v-if="state == 'signup'"
                  ></v-text-field>
                  <v-text-field
                    name="email"
                    label="Email"
                    type="email"
                  >
                  </v-text-field>
                  <v-text-field
                    name="password"
                    label="Password"
                    :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                    :type="show ? 'text' : 'password'"
                    @click:append="show = !show"
                  ></v-text-field>
                </v-card-text>
                <v-card-actions>
                  <v-btn color="success" depressed block v-if="state == 'login'">Login</v-btn>
                  <v-btn color="success" depressed block v-else>Sign Up</v-btn>
                </v-card-actions>
                <div class="text-center my-4">
                  <span>Or login with</span>
                  <v-btn icon small outlined class="mx-3">
                    <v-icon small color="info">mdi-twitter</v-icon>
                  </v-btn>
                  <facebook-login/>
                  <google-login />
                </div>
                <div class="text-center">
                  <small>{{ state == 'login' ? 'Or' : 'Have an account ?'}}</small>
                  <v-btn
                    color="info" text
                    small class="text-capitalize"
                    v-if="state == 'signup'"
                    @click="state = 'login'">
                    Login</v-btn>
                  <v-btn
                    color="info" text
                    small class="text-capitalize"
                    v-if="state == 'login'"
                    @click="state = 'signup'">
                    Sign Up
                  </v-btn>
                </div>
              </v-col>
              <v-col cols="12" sm="6" v-if="$bp.smAndUp">
                <v-img :src="require('@/assets/v.jpg')" width="100%" height="500">
                  <v-row justify="center" style="background: rgba(0,0,0,.4); height: 500px;">
                    <v-col cols="10" sm="10" md="8">
                      <div class="welcome-msg white--text" style="position: absolute; bottom: 40%;">
                        <h2>Claire AI</h2>
                        <h5>Pandemic control and personal medical assistant</h5>
                      </div>
                    </v-col>
                  </v-row>
                </v-img>
              </v-col>
            </v-row>
          </v-card>
        </v-form>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import GoogleLogin from '@/components/GoogleLogin'
import FacebookLogin from '@/components/FacebookLogin'

export default {
  data: () => ({
    show: false,
    state: 'login'
  }),
  computed: {
    $bp () {
      return this.$vuetify.breakpoint
    }
  },
  components: {
    GoogleLogin,
    FacebookLogin
  },
  methods: {
    //
  }
}
</script>

<style scoped>
  .login {
    height: 100vh;
    background: #36D1DC;  /* fallback for old browsers */
    background: -webkit-linear-gradient(to right, #5B86E5, #36D1DC);  /* Chrome 10-25, Safari 5.1-6 */
    background: linear-gradient(to right, #5B86E5, #36D1DC); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  }
</style>
