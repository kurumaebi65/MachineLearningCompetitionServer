<template>
  <div class="register-competition-form">
    <table>
      <tr>
        <td>competition name</td>
        <td>
          <input type="text" v-model="competition_name">
        </td>
      </tr>
      <tr>
        <td>description</td>
        <td>
          <textarea v-model="competition_description"></textarea>
          <input type="button" value="preview" @click="updatePreview">
          <span v-html="competition_description_preview"></span>
        </td>
      </tr>
      <tr>
        <td>training file</td>
        <td>
          <input type="file" id="train" accept=".csv" @change="updateSelectedFile">
        </td>
      </tr>
      <tr>
          <td>test file</td>
        <td>
          <input type="file" id="test" accept=".csv" @change="updateSelectedFile">
        </td>
      </tr>
    </table>
    <input type="button" value="submit" @click="submit">
  </div>
</template>

<script>
import marked from "marked";

marked.setOptions({
  sanitize: true
});

export default {
  data: function() {
    return {
      competition_name: "",
      competition_description: "",
      competition_description_preview: ""
    };
  },
  methods: {
    updatePreview: function() {
      this.competition_description_preview = marked(
        this.competition_description
      );
    }
  }
};
</script>
