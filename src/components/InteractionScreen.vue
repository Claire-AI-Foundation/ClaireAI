<template>
  <div>
    <v-row justify="center">
      <v-col cols="12" sm="10" md="5">
        <v-row>
          <v-col>
            <v-window
              v-model="step"
              class="elevation-0"
            >
              <v-window-item :value="1">
                <v-card flat>
                  <v-card-text>
                    <h3>Hello {{fname}}, I'm Claire</h3>
                    <p>
                      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
                      incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
                    </p>
                    <p>Which of the following symptoms do you have?</p>
                    <template v-for="(val, key) in symptoms">
                      <v-checkbox :key="key" :label="key" v-model="symptoms[key]" hide-details></v-checkbox>
                    </template>
                  </v-card-text>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="info" depressed @click="submit" :loading="loading">Submit</v-btn>
                  </v-card-actions>
                </v-card>
              </v-window-item>
              <v-window-item :value="2">
                <v-card flat>
                  <div class="v-card__title">Results</div>
                  <v-card-text>
                    <p>Here are my recommendations based on your symptoms</p>
                    <ul>
                      <li v-for="(recommendation, i) in recommendations" :key="i + '_rec'">
                        {{recommendation}}
                      </li>
                    </ul>
                  </v-card-text>
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
    loading: false,
    symptoms: {
      'Fever': false,
      'Cough': false,
      'Shortness of Breath': false,
      'Trouble breathing': false,
      'Persistent Chest Pain or Pressure': false,
      'New confusion or inability to arouse': false,
      'Bluish lips or face': false
    },
    recommendations: [],
    questions: [],
    action: []
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
    async submit () {
      this.loading = true
      try {
        const obj = {}
        Object.entries(this.symptoms).map(d => {
          obj[d[0]] = d[1] ? 'yes' : 'no'
        })
        const resp = await backend().post('/interaction', obj)
        // console.log(resp.data, this.symptoms)

        this.recommendations = resp.data.comments
        this.questions = resp.data.questions
        this.actions = resp.data.actions

        this.loading = false
        this.step = 2
      } catch (error) {
        console.log(error)
        this.loading = false

        this.$notify({
          group: 'app',
          title: 'Error',
          text: error.response ? error.response.data : 'Something went wrong',
          type: 'error'
        })
      }
    }
  }
}
</script>
