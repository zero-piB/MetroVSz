<template>
    <div class="xpanel-wrapper">
        <div class="xpanel">
            <slot/>
        </div>
    </div>
</template>

<style lang="scss">
.xpanel-wrapper {padding-bottom:15px;box-sizing:border-box;}
.xpanel {
	padding:8px;
    height:100%;
    width: 100%;
	min-height:170px;
	background:url("../assets/img/panel.png")  no-repeat;
	background-size:100% 100%;
	box-sizing:border-box;
}
</style>