<script >

export default {
  data() {
    return {
      message: 'This is some text',
      img:"",
      shows:"",
      prediction:""
    };
  },
  methods:{
    handleFileChange(e){
      this.img=this.$refs.imgInput.files[0]
      this.shows=URL.createObjectURL(this.img);
    },

    async fileUpload(){
      console.log(this.img)
      const formData = new FormData()
      formData.append("image", this.img)
      console.log(formData.getAll("image"))
      fetch('http://127.0.0.1:5000/classifier', {
        method: 'POST',
        body: formData
      }).then(response => {
        return response.json()
      }).then(data=>this.prediction=data['prediction'])
    }
  }
};


</script>

<template>
  <nav class="navbar bg-body-tertiary" id="nav">
    <div class="container-fluid">
      <h1>Fruit Image Identifier</h1>
    </div>
  </nav>
  <div id="main">
    <input type="file" name="image" id="image" ref="imgInput" @change="handleFileChange">
    <img :src="shows" width="250" height="250" v-if="shows" class="m-3 border border-dark-subtle">
    <button @click="fileUpload" class="btn btn-sm btn-primary my-3">Identify</button>
    <br>
    <div v-if="prediction" id="result">
      <h4>Hasil</h4>
      <h1 >{{ prediction }}</h1>
    </div>
  </div>
</template>

<style >
#nav{
  position: absolute;
  top: 0;
  background-color: rgb(5, 255, 234);
  width: 100%;
}
#main{
  padding: 5rem 0;
  margin: auto ;
  display: grid;
  /* background-color: antiquewhite; */
}
img{
  margin: auto;
}
#result{
  margin: auto;
  text-align: center;
}

</style>
