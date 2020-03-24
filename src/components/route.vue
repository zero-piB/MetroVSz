<template>
    <svg>
    </svg>
</template>
<script>
import * as d3 from 'd3'
export default {
    data(){
        return {
            routeName:"",
            routes:[]
        }
    },
    methods:{
        handleClick(){
            console.log(this.routeName)
        }
    },
    props:["route"],
    created(){
        this.new_name= this.route["new_name"]
        this.routeName = this.route["routeName"]
        this.routes = this.route["stops"]
    },
    mounted(){
        let r = 10;
        let svg = d3.select(this.$el)
                    .attr("width",r*2*this.routes.length + 150)
                    .attr("height",2*r + r)
                    .on("click",()=>{
                        console.log(this.routeName)
                    })
        

        let trip = svg.selectAll("circle")
                        .data(this.routes)
                        .enter()
                        .append("circle")
                        .attr("r",0)
                        .attr("cy",r + r/2)
                        .attr("cx",(data,index)=>{
                            return r + index*2*r
                        })
                        .attr("class", "graf")
                        .attr("fill","steelblue")
                        .on("click",(d)=>{
                            console.log(d["site_name"])
                            d3.event.stopPropagation();  //阻止事件冒泡
                        })
        trip.transition()
             .delay(300)     //延迟300ms再开始
             .duration(1000) //过渡时长为1000ms
             // .ease("bounce") //过渡样式
             .attr("r",r); //目标属性

        svg.append("text")
          .text(this.new_name)
          .attr("font-size",0)
          .attr("x",r*2*this.routes.length+10)
          .attr("y",r*2)
          .style("fill","white")
          .transition()
          .delay(300)
          .duration(1000)
          .attr("font-size",13)
        //   .style("font-weight","bold")
        // trip.data(this.routeName)
        //      .enter()
        //      .append("text")
        //      .attr("font-size",15)
        //      .attr("text-color","width")

    },
    

}
</script>

<style lang="scss" scoped>
svg{
    margin: 5px 5px 5px 10px;
}
</style>