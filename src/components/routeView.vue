<template>
    <div id="routeView">
        <div v-for="(route,index) in routeData" :key = index >
            <route :route="route"/>
        </div>
    </div>
</template>
<script>
//在这里加载所有的路径

import route from "./route"
import store from '../store'
export default {
    data(){
        return{
            routeData:[],
        }
    },
    store,
    components:{
        route
    },
    computed:{
        getSelectedRouteDom(){
            return store.state.selectedRouteDom
        },
        getSelectedStopDom(){
            return store.state.selectedStopDom
        },
    },
    watch:{
       getSelectedRouteDom(newDom,oldDom){
           if(newDom){
                newDom.style.border = "green solid 1px"
           }
           if(oldDom){
                oldDom.style.removeProperty("border")
           }
       },
       getSelectedStopDom(newDom,oldDom){
           if(newDom){
                newDom.setAttribute("stroke","red")
           }
           if(oldDom){
                newDom.setAttribute("stroke-width",1)
                oldDom.removeAttribute("stroke")
           }
       },
    },
    created(){
        this.axios.get('api/routes').then(res=>{
            let routes = res.data;
            routes.forEach(element => {
                let route = {}
                route["routeName"] = element["name"]
                route["new_name"] = element["new_name"]
                route["stopNums"] = element["stopsCount"]
                route["stops"] = element["stops"]
                this.routeData.push(route)
            });
        })
    }
}
</script>

<style lang="scss" scoped>
#routeView{
    // position: relative;
    width:inherit;
    height: 310px;
    // height: inherit;
    // bottom: 0;
    overflow:scroll;
}
 /*滚动条样式*/
#routeView::-webkit-scrollbar {/*滚动条整体样式*/
    width: 10px;     /*高宽分别对应横竖滚动条的尺寸*/
    height: 10px;
    background-color: rgb(245, 245, 245); 
}
#routeView::-webkit-scrollbar-thumb {/*滚动条里面小方块*/
    border-radius: 10px;  
    -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,.3);  
    background-color: #AAA;
}
#routeView::-webkit-scrollbar-track {/*滚动条里面轨道*/
    -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);  
    border-radius: 10px;  
    background-color: #FFF;  
}
svg:hover{
    background-color: #06d9d9;
}
svg{
    margin: 5px 5px 5px 10px;
}
</style>