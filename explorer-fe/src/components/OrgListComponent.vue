<template>
  <div class="orgListComponent">
    <el-table
      :data="tableData"
      style="width: 100%">
      <el-table-column
        label="ORG ID">
        <template slot-scope="scope">
        <router-link :to="{path: '/explore/'+scope.row.org_id}">{{ scope.row.org_id }}</router-link>
      </template>
      </el-table-column>
      <el-table-column label="Name"
        >
      <template slot-scope="scope">
        <p>{{ parseName(scope.row.json_text) }}</p>
      </template>
      </el-table-column>
      <el-table-column
        prop="lif_balance"
        label="LIF Balance">
      </el-table-column>
      <el-table-column label="Actions">
        <template slot-scope="scope">
          <el-button @click="goToVerify(scope.row.org_id)">Verify Signed Msg</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import axios from 'axios';
import helper from '@/helper.js';

export default {
  name: 'orgListComponent',
  data() {
    return {
      tableData: [],
    };
  },
  mounted() {
    this.loadOrgs();

  },
  methods: {
    async loadOrgs () {
      var response = await axios.get('http://localhost:8000/orgs');
      console.log("Data: ", JSON.stringify(response.data));
      this.tableData = response.data;
      console.log("After parsing: " + this.tableData);
    },
    parseName(jsonString){
      console.log("jsonString: " + jsonString);
      try{
      var jsonText = JSON.parse(jsonString);
      }catch(e){
        return "NOT AVAILABLE";
      }
      if(jsonText == null || jsonText.legalEntity == null){
        return "NOT AVAILABLE"
      }
      return jsonText.legalEntity.name;
    },
    goToVerify(orgId) {
      this.$router.push('/verify?orgId='+orgId);
    }
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
