<template>
  <div id="app">
    <crowdCard v-if="crowdCardVisible">
      <dateView/>
    </crowdCard>
    <VueHeader/>
    <div class="container-fluid">
      <div class="row">
        <div class="col-lg-8">
          <VuePanel style="height:100%">
            <search/>
            <map-view/>
          </VuePanel>
        </div>
        <div class="col-lg-4">
          <VuePanel style="height:50%">
            <punchCardView v-if='getSelectedRoute'/>
          </VuePanel>
          <VuePanel style="height:50%">
            <RouteView/>
          </VuePanel>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import store from './store'
import VuePanel from './components/xpanel.vue';
import MapView from './components/MapView.vue';
import VueHeader from './components/header.vue';
import RouteView from './components/routeView';
import punchCardView from './components/punchCardView';
import crowdCard from './components/crowdCard';
import dateView from './components/dateView';
import search from './components/search';
export default {
  data(){
    return{
      isShowCrowd:false
    }
  },
  store,
  components:{
    VuePanel,
    VueHeader,
    MapView,
    RouteView,
    punchCardView,
    crowdCard,
    dateView,
    search,
  },
  computed:{
      getSelectedRoute(){
        return store.state.selectedRoute
      },
      getSelectedStop(){
        return store.state.selectedStop
      },
      crowdCardVisible(){
        return store.state.crowdCardVisible
      }
  },
  methods:{
    
  }
  
}
</script>
<style lang="scss">
@import './assets/css/style.scss'
</style>
