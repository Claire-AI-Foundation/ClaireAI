import $store from '../store'
// import backend from '@/services/backend'

export default {
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
