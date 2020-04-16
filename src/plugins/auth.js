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

  /**
   * Authenticate the user with the backend
   * @param {string} provider the signin provider
   * @param {string} token access token from the provider
   * @returns {boolean} signed jwt token from server
   */
  async authenticateWithBackend (provider, token) {
    // call api
    try {
      var path = provider.charAt(0).toUpperCase() + provider.slice(1)
      const endpoint = `/loginWith${path}`
      const resp = await backend().post(endpoint, {
        token
      })

      $store.dispatch('setUser', resp.data.token)
      return resp.data.token
    } catch (error) {
      throw new Error(error.response ? error.response.data.message : error)
    }
  }
}
