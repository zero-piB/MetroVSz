<template>
    <transition name="fade" disabled="false">
      <div class="float-card" :key="1">
        <div class="remove icon"  @click="handleClose"></div>
        <slot/>
      </div>
    </transition>
</template>

<script>
// import draggable from 'vuedraggable'
import EventUtil from '../utils/event-util-vue'
import store from '../store/index'
export default {
    data() {
      return {
        // cardVisible: true,
        dragging:null,
        diffX:0,
        diffY:0,
      };
    },
    store,
    components:{
      // draggable,
    },
    methods: {
      handleClose(){
        store.commit("setCardVisble",false)
        // this.cardVisible=false;
      },
      handleEvent(event){
        event = EventUtil.getEvent(event);
        let target = EventUtil.getTarget(event);
        //确定事件类型
        
        switch(event.type){
          case "mousedown":
            if(target.className.indexOf("float-card") > -1){
              this.diffX = event.clientX - target.offsetLeft;
              this.diffY = event.clientY - target.offsetTop;
              this.dragging = target;
            }
            break;
          case "mousemove":
            if(this.dragging){
              this.dragging.style.left = (event.clientX - this.diffX) +"px";
              this.dragging.style.top = (event.clientY - this.diffY) +"px";
            }
            break;
          case "mouseup":
            this.dragging = null;
            break;
        }
      },
      // 防抖动函数
      debounce(func, wait, immediate) {
        let timeout, result;
        let debounced = function(){
          let context = this;
          let args = arguments;
          if(immediate){
            let callNow = !immediate
            timeout = setTimeout(()=>{
              timeout = null
            },wait);
            if(callNow) result = func.apply(context,args)
          }else{
            timeout = setTimeout(()=>{
              func.apply(context,args)
            },wait)
          }
          return result
        }
        console.log(timeout)
        return debounced
      }
    },
    
    mounted(){
      let vm = this;
      // this.$el.addEventListener('mousedown',this.handleEvent)
      // this.$el.addEventListener('mousemove',this.debounce(vm.handleEvent,50))
      // this.$el.addEventListener('mouseup',this.handleEvent)
      EventUtil.addHandler(this.$el,"mousedown",this.debounce(vm.handleEvent,10));
      EventUtil.addHandler(this.$el,"mousemove",this.debounce(vm.handleEvent,10));
      EventUtil.addHandler(this.$el,"mouseup",this.handleEvent);
    }
};
</script>

<style lang="scss" scoped>
$iconRadius:20px;
.float-card{
    position:absolute;
    background-color:rgba(253, 253, 253, 0.8);
    z-index: 200;
    border-radius: 20px;
    border: 2px solid rgb(45, 161, 238);
    top:10%;
    left: 20%;
    height: 600px;
    width: 1000px;
    padding-top: 25px;
}
.remove.icon {
  position: absolute;
  right: 2px;
  top: 2px;
  width: $iconRadius;
  height: $iconRadius;
  background-color: rgb(29, 118, 235);
  border: 1px solid white;
  border-radius: 100%;
  outline: 6px solid rgba(230, 248, 248, 0.932);
  outline-offset: -15px;
  cursor: pointer;
  transform: rotate(45deg);
}

.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to{
  opacity: 0;
}
</style>