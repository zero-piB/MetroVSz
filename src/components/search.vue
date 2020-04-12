<template>
    <div>
        <input type="search" placeholder="输入搜索线路">
		<ul>
			
		</ul>
    </div>
</template>

<script>
import EventUtil from '../utils/event-util-vue'
import {_} from 'vue-underscore';
import store from '../store/index'
export default {
    methods:{
        setUlListStyle(target){
            target.style.position = 'relative'
            target.style.left = '5px'
            target.style.backgroundColor= 'white';
            target.style.listStyleType = 'disc';
            target.style.width= '230px';
            target.style.boxSizing = 'border-box';
            target.style.padding=0;
            target.style.margin=0;
            target.style.borderRadius='3px'
        },
        onInput(e){
            if(e.target.value.trim()!=''){	
                let value = encodeURI(this.$el.firstElementChild.value.trim())
                let vm = this
                this.axios.get(`api/routes/search&line_name=${value}`).then(res=>{
                    if(res.data.length>0){
                        vm.createList(res.data)
                    }else{
                        vm.createList([])
                    }
                })
            }
        },
        createList(data){
            let vm = this
            let ulList = this.$el.childNodes[1]    //  document.getElementsByTagName('ul')[0];
            let newUlist=document.createElement('ul');
            data.forEach(item=>{
                let li=document.createElement('li');
                li.textContent=item['name'];
                li.style.fontSize = '13px'
                li.style.lineHeight = '25px'
                EventUtil.addHandler(li,'click',()=>{
                    store.commit('setSelectedRoute',li.textContent)
                }) 
                newUlist.appendChild(li);
            });
            this.setUlListStyle(newUlist)
            vm.$el.replaceChild(newUlist,ulList);
            ulList=null;//垃圾回收

            newUlist.childNodes.forEach((item)=>{
                EventUtil.addHandler(item,'mouseenter',function(event){
                    let target = event.target ||event.srcElement;
                    if(target.tagName.toLowerCase()==='li'){
                        target.style.cursor = 'pointer'
                        target.style.backgroundColor = 'rgb(168,213,252)';
                    }
                });
                EventUtil.addHandler(item,'mouseout',function(event){
                    let target=event.target||event.srcElement;
                    if(target.tagName.toLowerCase()==="li"){
                        target.style.backgroundColor = 'transparent'
                    }
                })
            }); 
        },

        showList(){
            this.$el.childNodes[1].style.visibility = 'visible';
        },
        //输入框失去焦点触发
        hideList(e){
            let target=e.target||e.srcElement;
            let tagName=target.tagName.toLowerCase();
            // let ulList=this.$el.lastElementChild;
            if(tagName!=='li'&&tagName!=='input'){
                // EventUtil.addClass(ulList,'hide');
                this.$el.childNodes[1].style.visibility='hidden'
            }
        }
    },
    store,
    mounted(){
        let txtInput=this.$el.firstElementChild;
        EventUtil.addHandler(txtInput,'input',_.debounce(this.onInput,300));
        EventUtil.addHandler(txtInput,'focus',this.showList);
        EventUtil.addHandler(window,'click',this.hideList);
        EventUtil.addHandler(window,'keydown',this.onKeydown);
    },

}

</script>
<style lang="scss" scoped>
$width: 300px;
div {
    position: absolute;
    width:$width;
    top:15px;
    left: 30px;
    // left: $left;
    z-index: 10000;
    user-select: none;
    input{
        height: 30px;
        line-height: 30px;
        outline: none;
    }

    input[type=search] {
        -webkit-appearance: textfield;
        -webkit-box-sizing: content-box;
        font-family: inherit;
        font-size: 100%;
    }
    input::-webkit-search-decoration,
    input::-webkit-search-cancel-button {
        display: none;
    }

    input[type=search] {
        background: #ededed url(../assets/img/search-icon.png) no-repeat 10px center;
        border: solid 1px #ccc;
        padding: 4px 4px 4px 32px;
        width: 60px;

        -webkit-border-radius: 10em;
        -moz-border-radius: 10em;
        border-radius: 10em;

        -webkit-transition: all .8s;
        -moz-transition: all .8s;
        transition: all .8s;
    }
    input[type=search]:focus {
        width: $width - 100;
        background-color: #fff;
        border-color: #3385ff;

        -webkit-box-shadow: 0 0 5px rgba(109,207,246,.5);
        -moz-box-shadow: 0 0 5px rgba(109,207,246,.5);
        box-shadow: 0 0 5px rgba(109,207,246,.5);
    }
}
</style>