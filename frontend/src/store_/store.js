import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    keyword: 'kosong'
  },
  mutations: {
    search (state, keyword) {
      console.log('Search')
    }
  }
})
