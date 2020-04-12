<template>
    <div>
    </div>
</template>

<script>
import echarts from 'echarts'
import store from '../store/index'
export default {
    data(){
        return{
            crowdedData :[],
            averageTime:[],
            color:['#ffffff','#a0e19f','#61e1d9','#ffff7f','#e0973c','#dc5d59','#b30404'],
            stops: [],
            option:{},
            startTime:'',
            endTime:'',
            myChart:null,
        }
    },
    store,
    methods:{
        toCrowedLevel(){

        },
        renderItem(params, api) {
            let categoryIndex = api.value(0);
            let start = api.coord([api.value(1), categoryIndex]);
            let end = api.coord([api.value(2), categoryIndex]);
            let height = api.size([0, 1])[1] * 0.7;

            let rectShape = echarts.graphic.clipRectByRect({
                x: start[0],
                y: start[1] - height / 2,
                width: end[0] - start[0],
                height: height
            }, {
                x: params.coordSys.x,
                y: params.coordSys.y,
                width: params.coordSys.width,
                height: params.coordSys.height
            });

            return rectShape && {
                type: 'rect',
                shape: rectShape,
                style: api.style()
            };
        },
        //时间戳转换方法    date:时间戳数字
        formatDate(date1) {
            let date = new Date(date1);
            let YY = date.getFullYear() + '-';
            let MM = (date.getMonth() + 1 < 10 ? '0' + (date.getMonth() + 1) : date.getMonth() + 1) + '-';
            let DD = (date.getDate() < 10 ? '0' + (date.getDate()) : date.getDate());
            let hh = (date.getHours() < 10 ? '0' + date.getHours() : date.getHours()) + ':';
            let mm = (date.getMinutes() < 10 ? '0' + date.getMinutes() : date.getMinutes()) + ':';
            let ss = (date.getSeconds() < 10 ? '0' + date.getSeconds() : date.getSeconds());
            return YY + MM + DD +" "+hh + mm + ss;
        },
        async fetchAndUpdate(){
            let vm = this
            vm.crowdedData =[]
            vm.stops = []
            let res = await vm.axios.get(`api/routes/crowdData&line_name=${store.getters.selectedRoute}`)
            if(res.status===200){
                vm.data = res.data[0]
                let data = res.data[0];
                // console.log(data)
                vm.startTime =  data['startTime']
                vm.endTime = data['endTime']
                data['route'].forEach(element => {
                    let site_name = element['site_name']
                    vm.stops.push(site_name)
                    vm.averageTime.push(element['averageTime'])
                    let records = element['records'];

                    records.sort((record1,record2)=>{
                        if(record1['arriveTime']>record2['arriveTime']){
                            return 1;
                        }
                        else return -1;
                    });
                    
                    for(let i = 0; i < records.length-1; i++){
                        let curTime = vm.formatDate(1000*records[i]['arriveTime'])
                        let nextTime = vm.formatDate(1000*records[i+1]['arriveTime'])
                        let crowdNum = records[i]['crowdNum']
                        let tag = records[i]['bus']
                        let crowdData_stop = [site_name,curTime,nextTime,crowdNum,tag]

                        vm.crowdedData.push({
                            value:crowdData_stop,
                            itemStyle: {
                                normal: {
                                    color: crowdNum<vm.color.length?vm.color[crowdNum]:vm.color.slice(-1)[0]
                                }
                            }
                        });
                    }

                });

               //更新图表
                let option = {
                    title:{
                        text:store.getters.selectedRoute
                    },
                    yAxis:{
                        data: vm.stops
                    },
                    series:[{
                        id:'crowdedData',
                        data:vm.crowdedData
                    }]
                }
                this.myChart.setOption(option)
                this.myChart.hideLoading()
            }

        },
        setEchartOption(){
            let vm = this;
            vm.option = {
                tooltip: {
                    formatter: function (params) {
                        return params.marker + `${params.value[0]}</br> ${params.value[1]}  到   ${params.value[2]}</br>拥挤等级: ${params.value[3]}`;
                    }
                },
                title: {
                    text: store.getters.selectedRoute,
                    left: 'center'
                },
                xAxis: {
                    type: 'time',
                    position: 'top',
                    splitLine: {
                        show:true,
                        interval:0,
                        lineStyle: {
                            color: ['#aaa']
                        }
                    },
                    axisLabel: {
                        color: '#929ABA',
                        inside: false,
                        align: 'center'
                    }
                },
                yAxis:{
                    data: [],
                    splitLine: {
                        show:true,
                        interval:0,
                        lineStyle: {
                            color: ['#aaa']
                        }
                    },
                },
                grid:{
                    show:true
                },
                dataZoom:[{
                    type:'slider',
                    xAxisIndex: 0,
                    filterMode: 'weakFilter',
                    height: 10,
                    start: 20,
                    end: 90,
                    showDataShadow: false,
                    handleIcon: 'M10.7,11.9H9.3c-4.9,0.3-8.8,4.4-8.8,9.4c0,5,3.9,9.1,8.8,9.4h1.3c4.9-0.3,8.8-4.4,8.8-9.4C19.5,16.3,15.6,12.2,10.7,11.9z M13.3,24.4H6.7V23h6.6V24.4z M13.3,19.6H6.7v-1.4h6.6V19.6z',
                    handleSize: 20,
                    handleStyle: {
                        shadowBlur: 6,
                        shadowOffsetX: 1,
                        shadowOffsetY: 2,
                        shadowColor: '#aaa'
                    },
                },{
                    type:'slider',
                    yAxisIndex: 0,
                    filterMode: 'weakFilter',
                    start:20,
                    end:50,
                    width:10,
                    right:20,
                    showDataShadow: false,
                    handleIcon: 'M10.7,11.9H9.3c-4.9,0.3-8.8,4.4-8.8,9.4c0,5,3.9,9.1,8.8,9.4h1.3c4.9-0.3,8.8-4.4,8.8-9.4C19.5,16.3,15.6,12.2,10.7,11.9z M13.3,24.4H6.7V23h6.6V24.4z M13.3,19.6H6.7v-1.4h6.6V19.6z',
                    handleSize: 20,
                    handleStyle: {
                        shadowBlur: 6,
                        shadowOffsetX: 1,
                        shadowOffsetY: 2,
                        shadowColor: '#aaa'
                    },
                },
                ],
                series:[{
                    id:'crowdedData',
                    type: 'custom',
                    itemStyle: {
                        opacity: 0.8
                    },
                    encode:{
                        // y:0,
                        x:[1,2]
                    },
                    renderItem: vm.renderItem,
                    data:[]
                }]
            }
            vm.myChart.setOption(vm.option);
        },
    },
    mounted(){
        this.myChart = echarts.init(this.$el)
        this.setEchartOption();
        this.myChart.showLoading({
            text: '数据正在努力加载...',
        })
        this.fetchAndUpdate()
    },
    computed:{
        getSelectedRoute(){
            return store.state.selectedRoute
        },
    },
    watch:{
        getSelectedRoute(){
            this.myChart.showLoading({
                text: '数据正在努力加载...',
            })
            this.fetchAndUpdate()
       },
    }
}
</script>

<style lang="scss" scoped>
div{
    height: 100%;
}
</style>