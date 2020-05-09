<template>
  <div class="mt-8 mx-md-12">
    <article class="pa-0 mb-5" v-for="(msg,i) in chatMessages" :key="i">
      <div flat class="msg-block px-3">

        <div class="d-inline-block msg-avatar mr-5">
          <v-avatar
            size="40" tile class="rounded-1"
            :color="$helpers.colorMinder(msg.author.name.charAt(0))">
            <img v-if="msg.author.photo" :src="msg.author.photo" alt="alt">
            <span v-else class="white--text">{{msg.author.name.charAt(0)}}</span>
          </v-avatar>
        </div>

        <div class="d-inline-block msg-text">
          <div class="msg-meta">
            <span class="pr-3 font-weight-bold">{{msg.author.name}}</span>
            <small class="grey--text">{{$helpers.parseDate(msg.date_created)}}</small>
          </div>
          <div class="msg-body">

            <div v-html="msg.body"></div>

            <!-- IMAGES -->
            <v-row v-if="msg.imgs && msg.imgs.length > 0">
              <v-col cols="12" sm="8">
                <!-- <image-grid :imgs="msg.imgs"/> -->
              </v-col>
            </v-row>

          </div>
        </div>
      </div>
    </article>
    <input-box @oninput="sendMessage" :mode="mode" :items="symptoms" :disable-innput="disableInput"/>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import backend from '@/services/backend'
import InputBox from '@/components/InputBox'

export default {
  data: () => ({
    step: 1,
    mode: 'select',
    loading: false,
    disableInput: null,
    symptoms: [
      'Fever',
      'Cough',
      'Shortness of Breath',
      'Trouble breathing',
      'Persistent Chest Pain or Pressure',
      'New confusion or inability to arouse',
      'Bluish lips or face'
    ],
    recommendations: [],
    questions: [],
    action: [],
    form: {
      userInput: ''
    },
    messages: []
  }),
  computed: {
    ...mapGetters([
      'getUser'
    ]),
    fname () {
      return this.getUser.name.split(' ')[0]
    },
    chatMessages () {
      return [
        {
          body: `Hey ${this.fname}. I'm Claire. 
            Which of the following symptoms do you have? <br>
            ${this.symptoms.join('<br>')}
            `,
          type: 'select',
          author: {
            name: 'Claire',
            photo: ''
          },
          date_created: Date.now()
        },
        ...this.messages
      ]
    }
  },
  methods: {
    startInteraction () {
      this.mode = 'select'
    },
    sendMessage (e) {
      this.messages.push({
        body: `${e}`,
        author: {
          name: 'You',
          photo: this.getUser.photo
        },
        date_created: Date.now()
      })

      this.submit(e)
    },
    async submit (msg) {
      this.loading = true
      try {
        const obj = {}
        this.symptoms.map(d => {
          obj[d] = msg.includes(d) ? 'yes' : 'no'
        })

        const resp = await backend().post('/interaction', {
          token: this.$store.state.authToken,
          data: obj
        })

        this.recommendations = resp.data.comments
        this.questions = resp.data.questions
        this.actions = resp.data.actions

        setTimeout(() => {
          this.messages.push({
            body: `Here are my recommendations based on your answer:
            ${this.recommendations.map(i => `<li> ${i} </li>`).join('')}`,
            author: {
              name: 'Claire',
              photo: ''
            },
            type: 'text',
            date_created: Date.now()
          })
          this.mode = 'text'
          this.disableInput = false
        }, 1000)
      } catch (error) {
        console.log(error)

        this.$notify({
          group: 'app',
          title: 'Error',
          text: error.response ? error.response.data : 'Something went wrong',
          type: 'error'
        })
      }
    }
  },
  components: {
    InputBox
  }
}
</script>
<style scoped lang="scss">
.rounded-1 {
  border-radius: 4px;
}
.msg-avatar {
  float: left;
}
.msg-text {
  float: left;
  width: 77%;
}
.msg-block {
  clear: both;
  overflow: auto;
  min-height: 60px;
}
</style>
