import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    selectedRoute:'',
    selectedStop:'',
    selectedRouteDom:null,
    selectedStopDom:null,
    crowdCardVisible:false,
  },
  mutations: {
    setSelectedRoute(state,val){
      state.selectedRoute = val
    },
    setSelectedStop(state,val){
      state.selectedStop = val
    },
    setSelectedRouteDom(state,val){
      state.selectedRouteDom = val
    },
    setSelectedStopDom(state,val){
      state.selectedStopDom = val
    },
    setCardVisble(state,val){
      state.crowdCardVisible = val
    },
  },
  actions: {
  },
  getters:{
    selectedRoute:state=>{
      return state.selectedRoute
    },
    selectedStop:state=>{
      return state.selectedStop
    },
    selectedRouteDom:state=>{
      return state.selectedRouteDom
    },
    selectedStopDom:state=>{
      return state.selectedStopDom
    },
    crowdCardVisible:state=>{
      return state.crowdCardVisible
    },
  },
  modules: {
  }
})
