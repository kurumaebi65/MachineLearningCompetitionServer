<template>
  <div class="menu">
    <h1>Competitions</h1>
    <div class="menu-table">
      <table>
        <tr>
          <th>competition name</th>
          <th>compeititon type</th>
        </tr>
        <tr v-for="competition in competitions" :key="competition.id">
          <td>
            <router-link :to="'/dashboard/' + competition.id">{{competition.competition_name}}</router-link>
          </td>
          <td>{{competition.competition_type}}</td>
        </tr>
      </table>
    </div>
  </div>
</template>


<script>
import axios from "axios";

export default {
  data: function() {
    return {
      competitions: {}
    };
  },
  mounted: function() {
    axios.get("/api/v1/get/competition/competitions/").then(response => {
      this.competitions = response.data;
    });
  }
};
</script>

<style scoped>
.menu {
  width: 80%;
  margin: auto;
}
table {
  display: inline-block;
  margin: auto;
}
th {
  border: solid 2px rgba(0, 0, 0, 0.4);
  padding: 5px 10px;
  font-weight: bold;
}
td {
  border: solid 1px rgba(0, 0, 0, 0.4);
  padding: 5px 10px;
}
</style>
