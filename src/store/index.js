import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    selectedRoute:'',
    selectedStop:''
  },
  mutations: {
    setSelectedRoute(state,val){
      state.selectedRoute = val
    },
    setSelectedStop(state,val){
      state.selectedStop = val
    }
  },
  actions: {
  },
  getters:{
    selectedRoute:state=>{
      return state.selectedRoute
    },
    selectedStop:state=>{
      return state.selectedStop
    }
  },
  modules: {
  }
})
