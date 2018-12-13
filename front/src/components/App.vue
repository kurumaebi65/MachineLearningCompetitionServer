<template>
  <div>
    <router-view></router-view>
  </div>
</template>

<script>
import ContentsTab from "./ContentsTab.vue";
import axios from "axios";
import Menu from "./Menu.vue";
import router from "../router/router.js";

export default {
  router: router,
  data: function() {
    return {
      competition_id: ""
    };
  },
  mounted: function() {
    axios.get("/api/v1/get/competition/competitions/").then(response => {
      this.competition_id = response.data[0]["id"];
    });
  }
};
</script>
