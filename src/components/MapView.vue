<template>
    <div id="mapView">

    </div>
</template>
<script>

import remoteLoad from '@/utils/remoteLoad.js'
import { MapKey} from '@/config'
export default {
    data(){
        return{

        }
    },
    methods:{
        initMap(){
            let map = new window.AMap.Map('mapView', {
                mapStyle: 'amap://styles/dark',
                zoom: 11,
                zooms: [4,15],//设置地图级别范围
                // viewMode:'3D',  //视图模式
                center: [114.09863543,22.646354],//[114.05096,22.541009]
                features: ['bg', 'road']  //定义显示样式
            });
            let currentCenter = map.getCenter(); 
            console.log(currentCenter)
        }
    },
    async created (){
        // 已载入高德地图API，则直接初始化地图
        if (window.AMap && window.AMapUI){
            this.initMap()
        }else{
            // 未载入高德地图API，则先载入API再初始化
            await remoteLoad(`http://webapi.amap.com/maps?v=1.4.15&&key=${MapKey}`)
            // await remoteLoad('https://webapi.amap.com/ui/1.0/main.js')
            this.initMap()
        }
    } 
}
</script>
<style lang="scss" scoped>
#mapView{
    height: 100%;
    width: 100%;
}
</style>