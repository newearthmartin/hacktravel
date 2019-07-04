<template>
  <div class="searchComponent">
    <H1>ORG.ID explorer</H1>
    <el-row>
      <el-col :span="22"><el-input placeholder="Enter your ORG.ID address" v-model="orgId" v-on:click="explore()"></el-input></el-col>
      <el-col :span="2"><el-button v-on:click="explore()" type="primary" plain>Explore</el-button></el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'search',
  data() {
    return {
      orgId: null,
    };
  },

  methods: {
    explore() {
      console.log("Searching for org id " + this.orgId);
      this.$router.push('/explore/'+ this.orgId);
    },
  }
}
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
.searchComponent{
  text-align: center;
}
</style>
