<template>
  <div id="app">
    <VueHeader/>

    <div class="container-fluid">
      <div class="row">
        <div class="col-lg-8">
          <VuePanel style="height:100%">
            <map-view/>
          </VuePanel>
        </div>
        <div class="col-lg-4">
          <VuePanel style="height:50%">
            <punchCardView/>
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
import VuePanel from './components/xpanel.vue';
import MapView from './components/MapView.vue';
import VueHeader from './components/header.vue';
import RouteView from './components/routeView';
import punchCardView from './components/punchCardView';
export default {
  data(){
    return{
      
    }
  },
  components:{
    VuePanel,
    VueHeader,
    MapView,
    RouteView,
    punchCardView,
  },
  computed:{

  }
}
</script>
<style lang="scss">
@import './assets/css/style.scss'
</style>
