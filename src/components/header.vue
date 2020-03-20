<template>
    <header class="header">
			<h3>公交网络服务水平系统</h3>
	</header>
</template>

<style lang="scss">
$headerH:42px;
.header{
  margin:10px auto;
  width: 100%;
  height: $headerH;
  background: url("../assets/img/header-left.png") left center no-repeat, 
  url("../assets/img/header-right.png") right center no-repeat;
  background-size:40% 80%, 40% 80%;
  overflow:hidden;
}

.header h3{
  margin: 0;
  padding: 0;
  line-height: $headerH;
  text-align: center;
  font-size:24px;
  color: #5dc2fe;
}

@media (max-width: 1199px) {
	.header {
		background-size:25% 60%, 25% 60%;
	}
}
</style>