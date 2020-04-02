import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersistence from 'vuex-persist'
import jwtDecode from 'jwt-decode'
import { vm } from '@/main'

Vue.use(Vuex)

const vuexLocal = new VuexPersistence({
  storage: window.localStorage,
  reducer: (state) => ({ authToken: state.authToken })
})

export default new Vuex.Store({
  plugins: [vuexLocal.plugin],
  state: {
    user: null,
    authToken: null
  },
  mutations: {
    setUser (state, data) {
      if (data) {
        var user = jwtDecode(data)
        user.photo = user.picture

        state.user = user
        state.authToken = data
      }
    },
    logout (state) {
      state.user = null
      state.authToken = null
      vm.$router.replace('login')
    }
  },
  actions: {
    setUser ({ commit }, data) {
      commit('setUser', data)
    },
    logout ({ commit }) {
      commit('logout')
    }
  },
  getters: {
    isLoggedIn: state => state.authToken,
    getUser: state => {
      if (!state.authToken) return null

      var user = jwtDecode(state.authToken)
      user.photo = user.picture
      return user
    }
  }
})
