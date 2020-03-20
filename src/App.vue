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
          <VuePanel style="height:50%"/>
          <VuePanel style="height:50%"/>
        </div>
      </div>
    </div>
  </div>
   
</template>
<script>
import VuePanel from './components/xpanel.vue';
import MapView from './components/MapView.vue';
import VueHeader from './components/header.vue';

export default {
  data(){
    return{
      
    }
  },
  components:{
    VuePanel,
    VueHeader,
    MapView
  },
  computed:{

  }
}
</script>
<style lang="scss">
@import './assets/css/style.scss'
</style>
