<template>
  <div id="app">
    <el-menu
    mode="horizontal"
    background-color="#545c64"
    text-color="#fff">
      <el-menu-item index="1"><el-button @click="$router.push('/')"><router-link to="/">List</router-link></el-button></el-menu-item>
    </el-menu>
    <router-view/>
  </div>
</template>

<script>
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}
a {
  color: #42b983;
}
</style>
