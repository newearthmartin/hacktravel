<template>
  <div class="searchComponent">
    <H1>ORG.ID explorer</H1>
    <el-row>
      <el-col :span="20"><el-input placeholder="Enter your ORG.ID address" v-model="orgidIn"></el-input></el-col>
      <el-col :span="4"><el-button v-on:click="getOrgJson()" type="primary" plain>Explore</el-button></el-col>
    </el-row>
    <h2>DEBUG: {{ orgidIn }}</h2>
  </div>
</template>

<script>
import helper from '../helper'
export default {
  name: 'search',
  data () {
    return {
      orgidIn: '',
    };
  },

  methods: {
    getOrgJson() {
      console.log("Searching for org id " + this.orgidIn)
      this.$router.push('/explorer/'+ this.orgidIn);
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
