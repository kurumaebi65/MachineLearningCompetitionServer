<template>
    <div class="upload-form">
        <input type="file" accept=".csv" @change="updateSelectedFile">
        <button @click="uploadFile">send</button>
        {{message}}
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data:function(){ 
        return{
            selectedFile:null,
            message:''
        }
    },
    props:["competition_id"],
    methods:{
        updateSelectedFile: function(e){
            e.preventDefault();
            let files = e.target.files;
            this.selectedFile = files[0];
        },
        uploadFile: function(){
            if (this.selectedFile === null){
                this.message = 'please select your file'
                return
            }
            let formData = new FormData();
            formData.append('file',this.selectedFile);
            let config = {
                headers: {
                    'content-type' : 'multipart/form-data'
                }
            };
            axios
                .post('api/v1/action/upload/'+this.competition_id,formData)
                .then(response => {
                    this.message = response.data.message
                    this.selectedFile = null;
                })
                .catch(err => {
                    this.message = err.response.data.message;
                })
            return
        }
    }
}
</script>

<style scoped>
.upload-form{
    width: 80%;
    display: block;
    margin: auto;
}
</style>

