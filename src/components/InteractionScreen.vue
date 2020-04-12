<template>
  <div>
    <v-row justify="center">
      <v-col cols="12" sm="10" md="5">
        <v-row>
          <v-col>
            <v-window
              v-model="step"
              class="elevation-1"
            >
              <v-window-item
                v-for="n in 3"
                :key="n"
              >
                <v-card flat>
                  <v-card-text>
                    <h3>Hello {{fname}}, I'm Claire</h3>
                    <p>
                      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
                      incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
                    </p>
                  </v-card-text>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="info" depressed @click="submit">Submit</v-btn>
                  </v-card-actions>
                </v-card>
              </v-window-item>
            </v-window>

          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import backend from '@/services/backend'

export default {
  data: () => ({
    step: 0,
    form: {}
  }),
  computed: {
    ...mapGetters([
      'getUser'
    ]),
    fname () {
      return this.getUser.name.split(' ')[0]
    }
  },
  methods: {
    submit () {
      backend().post('/interaction', {
        level: 1
      })
        .then(d => {
          console.log(d)
        })
    }
  }
}
</script>
