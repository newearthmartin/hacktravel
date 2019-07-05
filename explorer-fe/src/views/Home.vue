<template>
  <div class="hello">

    <SearchComponent></SearchComponent>
    <OrgListComponent></OrgListComponent>
  </div>
</template>

<script>
import SearchComponent from '@/components/SearchComponent.vue';
import OrgListComponent from '@/components/OrgListComponent.vue';
import VerifySignature from '@/views/VerifySignature.vue';

export default {
  name: 'Home',
  components: {
    SearchComponent,
    OrgListComponent
  },
  data () {
    return {};
  },
  mounted() {},
}
</script>

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
