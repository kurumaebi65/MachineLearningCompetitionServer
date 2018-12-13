<template>
  <div class="tab-table">
    <h1>Challenge</h1>
    <div class="tabs">
      <button
        :class="{'tab-button':!tab.display, 'tab-button-active':tab.display}"
        v-for="tab in contents_index"
        :key="tab"
        @click="change_tab(tab)"
      >{{tab.tab_name}}</button>
    </div>
    <div class="contents">
      <description v-show="contents_index.description.display" :competition_id="competition_id"></description>
      <dashboard v-show="contents_index.ranking.display" :competition_id="competition_id"></dashboard>
      <upload-form v-show="contents_index.uploadform.display" :competition_id="competition_id"></upload-form>
    </div>
  </div>
</template>


<script>
import Dashboard from "./Dashboard.vue";
import Description from "./Description.vue";
import UploadForm from "./UploadForm.vue"
class TabItems {
  constructor(tab_name) {
    this.tab_name = tab_name;
    this.display = false;
  }
}

export default {
  components: {
    Dashboard,
    Description,
    UploadForm
  },
  // props:['competition_id'],
  data: function() {
    return {
      contents_index: {
        description: new TabItems("Description"),
        ranking: new TabItems("Ranking"),
        uploadform: new TabItems("UploadForm")
      }
    };
  },
  computed:{
    competition_id: function(){
      return this.$route.params.competition_id;
    }
  },
  methods: {
    change_tab: function(change_content) {
      for (let content in this.contents_index) {
        this.contents_index[content].display = false;
      }
      change_content.display = true;
    }
  },
  mounted: function(){
    this.contents_index.description.display = true;
  }
};
</script>

<style scoped>
.tab-button {
  display: inline-block;
  max-width: 180px;
  text-align: left;
  border: 2px solid #9ec34b;
  font-size: 16px;
  color: #9ec34b;
  background-color: white;
  text-decoration: none;
  font-weight: bold;
  padding: 8px 16px;
  transition: 0.4s;
}

.tab-button:hover {
  background-color: #9ec34b;
  border-color: #cbe585;
  color: #fff;
}

.tab-button-active {
  display: inline-block;
  max-width: 180px;
  text-align: left;
  border: 2px solid #9ec34b;
  font-size: 16px;
  color: #9ec34b;
  text-decoration: none;
  font-weight: bold;
  padding: 8px 16px;
  transition: 0.4s;
  background-color: #9ec34b;
  color: #fff;
}

.tab-table{
  width: 80%;
  display: block;
  margin: auto;
}
.contents{
  border: 1px solid #9ec34b;
  box-shadow: 3px 3px 3px rgba(0,0,0,0.4);
  padding: 10px;
}
</style>
