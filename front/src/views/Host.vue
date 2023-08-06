

<template>
  <h3>主机管理</h3>
</template>




<script>
import axios from "axios";
  export default {
    name:"Host",

    mounted() {
      axios.get("http://api.zcx321.cc:8888/host/get").then((res)=>{
        console.log("res",res)
      })
    }
  }
</script>
<style scoped>

</style>