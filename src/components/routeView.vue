<template>
    <div id="routeView" >
        <div v-for="(item,index) in msg" :key = index>
            <route/>
        </div>
    </div>
</template>
<script>
//在这里加载所有的路径

import route from "./route"
export default {
    data(){
        return{
            msg:[1,2,3,4,5,6,7,8,9,10]
        }
    },
    components:{
        route
    }
}
</script>

<style lang="scss">
#routeView{
    width:inherit;
    height: inherit;
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

.graf:hover{
    fill: rgb(0, 255, 106);
}

svg:hover{
    background-color: #06d9d9;
}
</style>