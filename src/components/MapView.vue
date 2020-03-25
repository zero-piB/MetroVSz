<template>
    <div id="mapView">

    </div>
</template>
<script>

import remoteLoad from '@/utils/remoteLoad.js'
import { MapKey} from '@/config'
import store from '../store'
export default {
    data(){
        return{
            map:Object(),
        }
    },
    methods:{
        initMap(){
            const map = new window.AMap.Map('mapView', {
                mapStyle: 'amap://styles/dark',
                zoom: 11,
                zooms: [4,15],//设置地图级别范围
                // viewMode:'3D',  //视图模式
                center: [114.09863543,22.646354],//[114.05096,22.541009]
                features: ['bg', 'road']  //定义显示样式
            });

            //加载缩放控件
            window.initAMapUI();
            window.AMapUI.loadUI(['control/BasicControl'], function(BasicControl) {
                let zoomCtrl = new BasicControl.Zoom({
                    theme:'dark',
                    position: 'br', //left top，左上角
                    showZoomNum: true //显示zoom值
                });
                map.addControl(zoomCtrl);
            })
            this.map = map;
        },
        drawRoute(routeName){
            if(!window.pathSimplifierIns){
                const map = this.map;
                window.AMapUI.loadUI(['misc/PathSimplifier'],(PathSimplifier)=>{
                    window.pathSimplifierIns = new PathSimplifier({
                        zIndex: 100,
                        map:map,
                        clickToSelectPath:false,
                        getHoverTitle:(pathData)=>pathData.name, 
                        getPath: pathData => pathData.path,
                        renderOptions:{
                            renderAllPointsIfNumberBelow: -1 //绘制路线节点，如不需要可设置为-1
                        }
                    })
                    this.setRouteData(routeName)
                })
            }
            else{
                this.setRouteData(routeName)
            }
        },
        drawStop(stop){
            if(store.state.selectedRoute.length===0) return
            const map = this.map;
            // this.axios.get(`api/sitePosition&site=${stop}`)
            // .then(res=>{
            //     console.log(res)
            //     new window.AMap.Marker({
            //         map: map,
            //         position: res.data,    
            //     }) 
            // })
            setTimeout(()=>{
                this.axios.post(`api/sitePosition`,{
                    "site": stop,
                    "line_name": store.state.selectedRoute
                })
                .then(res=>{
                    // console.log(res)
                    new window.AMap.Marker({
                        map: map,
                        position: res.data,    
                    }) 
                })
            },80)
            
        },
        setRouteData(routeName){
            //加载数据
            this.axios.get(`api/routes&line_name=${routeName}`).then(res=>{
                window.pathSimplifierIns.setData(res.data)
            })
        }
    },
    store,
    computed:{
        getSelectedRoute(){
            return store.state.selectedRoute
        },
        getSelectedStop(){
            return store.state.selectedStop
        }
    },
    watch:{
       getSelectedRoute(val){
           this.map.clearMap()
           this.drawRoute(val);
       },
       getSelectedStop(val){
           this.drawStop(val)
       }
    },
    async created (){
        // 已载入高德地图API，则直接初始化地图
        if (window.AMap && window.AMapUI){
            this.initMap()
        }else{
            // 未载入高德地图API，则先载入API再初始化
            await remoteLoad(`https://webapi.amap.com/maps?v=1.4.15&&key=${MapKey}`)
            await remoteLoad('https://webapi.amap.com/ui/1.0/main-async.js')
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