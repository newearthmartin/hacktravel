<template>
  <div class="hello">
      Hola
  </div>
</template>

<script>
export default {
  name: 'ExplorerDetails',
  data() {
    return {
      url: null
    };
  },
  mounted() {
    this.url = this.$route.params.orgId;
    console.log(this.url);
  }
};
</script>

<style scoped>
</style>
