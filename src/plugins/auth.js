import $store from '../store'
import backend from '@/services/backend'

export default {
  async login (payload) {
    try {
      const { email, password, name } = payload
      const resp = await backend().post('/login', {
        email,
        password,
        name
      })

      console.log({ resp })

      $store.dispatch('setUser', resp.data.token)
      return true
    } catch (err) {
      throw new Error(err.response ? err.response.data.message : err)
    }
  },

  async signup (payload) {
    try {
      console.log({ payload })
      const resp = await backend().post('/signup', payload)
      console.log(resp)
      $store.dispatch('setUser', resp.data.token)
    } catch (err) {
      throw new Error(err.response ? err.response.data.message : err)
    }
  },

  async authenticateWithBackend (idToken) {
    // call api
    // try {
    //   const resp = await backend().post('/auth', {
    //     idToken
    //   })

    //   store.dispatch('setUser', resp)
    // } catch (error) {
    //   //
    // }

    await $store.dispatch('setUser', idToken)
    return true
  }
}
