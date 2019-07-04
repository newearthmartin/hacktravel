<template>
  <div class="test">
      Hola
  </div>
</template>

<script>
import helper from '@/helper.js';
import axios from 'axios';

export default {
  name: 'ExplorerDetails',
  data() {
    return {
      orgId: null,
      libs: null,
    };
  },
  mounted() {
    this.libs = helper.getLibs();
    this.orgId = this.$route.params.orgId;
    this.getOrgJson();
  },
  methods: {
    getOrgJson() {
      console.log("Parameter is " + this.orgId);
      this.loadedOrg = this.libs.getOrganization(this.orgId);
      var myThis = this;
      this.loadedOrg.orgJsonUri.then(function (value) {
        console.log("Calling from inside promise");
        console.log(value);
        myThis.shownOrg = value;
        myThis.loadJsonFromUrl(value);
      });
      console.log("Call done");
    },
    async loadJsonFromUrl(url) {
      var httpResponse = await axios.get(url);
      console.log(JSON.stringify(httpResponse));
      this.currentlySelectedOrg = httpResponse.data;
    }
  }
};
</script>

<style scoped>
</style>
