<template>
  <div>
    <div v-html="description"></div>
  </div>
</template>

<script>
import marked from "marked";
import axios from "axios";

export default {
  data: function() {
    return {
      description: ""
    };
  },
  props: ["competition_id"],
  watch: {
    competition_id:function(newVal,oldVal){
        axios
      .get("api/v1/get/description/" + newVal)
      .then(response => {
        this.description = marked(response.data.message);
      });
    }
  },
  mounted:function(){
    axios
      .get("api/v1/get/description/" + this.competition_id)
      .then(response => {
        this.description = marked(response.data.message);
      });
  }
};
</script>
