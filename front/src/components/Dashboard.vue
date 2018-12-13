<template>
  <table>
    <thead>
      <tr>
        <th v-for="key in column" :key="key">{{key}}</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="rows in results" :key="rows.file_name">
        <td v-for="key in column" :key="key">{{rows[key]}}</td>
      </tr>
    </tbody>
  </table>
</template>


<script>
import axios from "axios";

export default {
  data: function() {
    return {
      column: ["file_name", "result"],
      results: []
    };
  },
  props: ["competition_id"],
  mounted() {
    axios.get("api/v1/get/result/" + this.competition_id).then(response => {
      this.results = response.data.message;
    });
  }
};
</script>

<style scoped>
table {
  width: 80%;
  border: solid 1px black;
  border-collapse: collapse;
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