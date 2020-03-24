<template>
    <div>
        <input :name = "routeName" type="radio" @input="handleClick"/>
    </div>
</template>
<script>
import * as d3 from 'd3'
export default {
    name:"route",
    data(){
        return {
            routeName:"琼丹",
            routes:["王魏华","陈修艺","李春晓","李莉颖","陈湘宇","罗琦","刘婷婷","李幸静"]
        }
    },
    methods:{
        handleClick(){
            console.log(this.routeName)
        }
    },
    mounted(){
        let r = 10;
        let svg = d3.select(this.$el)
                    .append("svg")
                    .attr("width",r*2*this.routes.length)
                    .attr("height",2*r);

        let route = svg.selectAll("circle")
                        .data(this.routes)
                        .enter()
                        .append("circle")
                        .attr("r",0)
                        .attr("cy",r)
                        .attr("cx",(data,index)=>{
                            return r + index*2*r
                        })
                        .attr("class", "graf")
                        .attr("fill","steelblue")
                        .on("click",(d)=>{
                            alert(d)
                        })

        route.transition()
             .delay(100)     //延迟500ms再开始
             .duration(600) //过渡时长为1000ms
             // .ease("bounce") //过渡样式
             .attr("r",r); //目标属性

    }
}
</script>

<style lang="scss" scoped>
div{
    width: 100%;
    margin: 0;
}
input{
    zoom:1.2;
    position: relative;
    top:2px;
    margin: 0 8px 0 5px;
}
</style>