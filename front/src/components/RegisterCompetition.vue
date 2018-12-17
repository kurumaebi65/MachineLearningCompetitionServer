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
          <input type="file" id="train" accept=".csv" @change="updateTrainingFile">
        </td>
      </tr>
      <tr>
        <td>test file</td>
        <td>
          <input type="file" id="test" accept=".csv" @change="updateTestFile">
        </td>
      </tr>
      <tr>
        <td>correct file</td>
        <td>
          <input type="file" id="test" accept=".csv" @change="updateCorrectFile">
        </td>
      </tr>
    </table>
    <input type="button" value="submit" @click="submit">
    {{error_message}}
  </div>
</template>

<script>
import marked from "marked";
import axios from "axios";

marked.setOptions({
  sanitize: true
});

export default {
  data: function() {
    return {
      competition_name: "",
      competition_description: "",
      competition_description_preview: "",
      training_file: null,
      test_file: null,
      correct_file: null,
      error_message: ""
    };
  },
  methods: {
    updatePreview: function() {
      this.competition_description_preview = marked(
        this.competition_description
      );
    },
    updateTrainingFile: function(e) {
      e.preventDefault();
      let files = e.target.files;
      this.training_file = files[0];
    },
    updateTestFile: function(e) {
      e.preventDefault();
      let files = e.target.files;
      this.test_file = files[0];
    },
    updateCorrectFile: function(e) {
      e.preventDefault();
      let files = e.target.files;
      this.correct_file = files[0];
    },
    submit: function() {
      if (this.training_file === null || this.test_file === null) {
        this.error_message = "please upload file";
        return;
      }
      if (this.competition_description == "") {
        this.error_message = "please input competition description";
        return;
      }
      if (this.competition_name == "") {
        this.error_message = "please input competition name";
        return;
      }
      let formData = new FormData();
      formData.append("training_file", this.training_file);
      formData.append("test_file",this.test_file);
      formData.append("correct_file",this.correct_file);
      formData.append("competition_name",this.competition_name);
      formData.append("competition_description", this.competition_description)
      let config = {
        headers: {
          "content-type": "multipart/form-data"
        }
      };
      axios
        .post("api/v1/action/register_competition/", formData)
        .then(response => {
          this.message = response.data.message;
          this.selectedFile = null;
        })
        .catch(err => {
          this.message = err.response.data.message;
        });
      return;
    }
  }
};
</script>
