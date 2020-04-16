import axios from 'axios'

// const vuex = localStorage.getItem('vuex')
const instance = axios.create({
  baseURL: process.env.VUE_APP_BASE_URL
  // headers: { 'Authorization': 'Bearer ' + vuex.authToken }
})

export default () => instance
