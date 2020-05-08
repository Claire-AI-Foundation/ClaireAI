import axios from 'axios'
import $store from '@/store'

const instance = axios.create({
  baseURL: process.env.VUE_APP_BASE_URL,
  headers: { 'Authorization': 'Bearer ' + $store.state.authToken }
})

export default () => instance
