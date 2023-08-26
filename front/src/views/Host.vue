

<template>
  <h3>主机管理</h3>
</template>




<script>
import axios from "axios";
  export default {
    name:"Host",

    mounted() {
      axios.get(this.$settings.api_host+"/host",{
        headers:{
          "Content-Type":"application/json;charset=UTF-8",
          "Authorization":"Bearer "+this.$store.getters.token
        }
      }).then((res)=>{
        console.log("res",res)
      }).catch(err=>{
        console.log("err",err)
        this.$router.push("/login")
      })
    }
  }
</script>
<style scoped>

</style>