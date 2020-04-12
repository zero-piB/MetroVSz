<template>
    <svg>
    </svg>
</template>
<script>
import * as d3 from 'd3'
import store from '../store'
// import * as underscore from 'underscore' 
export default {
    data(){
        return {
            routeName:"",
            routes:[],
            svg:null,
        }
    },
    store,
    computed:{
        getSelectRouted(){
            return store.state.selectedRoute
        }
    },
    watch:{
        getSelectRouted(newVal){
            if(newVal === this.routeName){
                console.log(this.svg)
                store.commit('setSelectedRouteDom',this.svg["_groups"][0][0]); 
            }
            
        }
    },
    methods:{
    },
    props:["route"],
    created(){
        this.new_name= this.route["new_name"]
        this.routeName = this.route["routeName"]
        this.routes = this.route["stops"]
    },
    mounted(){
        let r = 10;
        let vm = this
        this.svg = d3.select(this.$el)
                    .attr("width",r*2*this.routes.length + 150)
                    .attr("height",2*r + r)
                    .on("click",()=>{
                        store.commit('setSelectedRoute',this.routeName);
                        let svgDom = vm.svg["_groups"][0][0];
                        store.commit('setSelectedRouteDom',svgDom);       
                    })
        let tooltip = d3.select('body')
                    .append('div')
                    .style('position', 'absolute')
                    .style('z-index', '10')
                    .style('color', 'white')
                    .style('visibility', 'hidden')   // 是否可见（一开始设置为隐藏）
                    .style('font-size', '13px')
                    .text('')

        let trip = vm.svg.selectAll("circle")
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
                        .on("click",(d,i)=>{
                            store.commit('setSelectedStop',d["site_name"]);
                            let [routeDom] = trip["_groups"]
                            store.commit('setSelectedStopDom',routeDom[i]);
                            // d3.event.stopPropagation();  //阻止事件冒泡
                        })
                        .on('mouseover', (d) => {
                            tooltip.style('visibility', 'visible').text(d['site_name'])
                        })
                        .on('mousemove', ()=> {
                            tooltip.style('top', (event.pageY-15)+'px').style('left',(event.pageX+10)+'px')
                        })
                        .on('mouseout',()=>tooltip.style('visibility', 'hidden'))
        trip.transition()
             .delay(300)     //延迟300ms再开始
             .duration(1000) //过渡时长为1000ms
             // .ease("bounce") //过渡样式
             .attr("r",r); //目标属性

        vm.svg.append("text")
          .text(this.new_name + "路")
          .attr("font-size",0)
          .attr("x",r*2*this.routes.length + 10)
          .attr("y",r*2)
          .style("fill","white")
          .transition()
          .delay(300)
          .duration(1000)
          .attr("font-size",13)
    },
    

}
</script>

<style lang="scss">
.graf:hover{
    fill: rgb(0, 255, 106);
}
</style>