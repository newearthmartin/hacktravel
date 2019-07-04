<template>
  <div class="hello">
    <SearchComponent></SearchComponent>
  </div>
</template>

<script>
import SearchComponent from '@/components/SearchComponent.vue';

export default {
  name: 'Home',
  components: {
    SearchComponent
  },
  data () {
    return {
      orgidIn: '',
      libs: 'undefined',
      loadedOrg: {},
      shownOrg:{},
      currentlySelectedOrg: {},
    };
  },

  mounted() {
  },
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
