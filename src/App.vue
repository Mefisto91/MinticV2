<template>
  <div>
  <img alt="Vue logo" src="@/assets/logo.png">
  <LoginEs msg="Hospital Paso Al Infierno"/>
  </div>
</template>

<script>
import LoginEs from '@/components/LoginEs.vue'

export default {
  name: 'App',
  components: {
    LoginEs,
    
}

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
@keyframes sharingan {
        to {transform: rotate(360deg);}
    }
    .circulo {
        position: absolute;
        height: 20px;
        width: 20px;
        background-color: black;
        top: 20%;
        border-radius: 50%;
    }
    .lineainterior {
        width: 70%;
        height: 70%;
        outline-style: solid;
        border-radius: 50%;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }
    .triangulos {
        height: 18px;
        width: 10px;
        background-color: black;
        position: relative;
        top: -9px;
        left: 4px;
        border-radius: 0% 145% 0% 90%;
        transform: rotateZ(60deg) skew(30deg);
    }
    .sharingan {
        background-color: red;
        width: 200px;
        height: 200px;
        border: solid black;
        border-radius: 50%;
        position: absolute;
        top: 9%;
        left: 25%;
        animation: sharingan 1s linear infinite;
    }
    .LoginEs{
        background-color: #85C6DF ;
        border: 2px transparent;
        padding: 15px;
        text-align: center;
        margin:10px auto ;
        width: 400px;
    }
    #title{
        font: bold 20px Tahoma;
        width: 100%;
    }
    #Enter{
        background-color: #BDCDD3;
    }
    .windowGUI{
        background-color: #85C6DF ;
        border: 2px transparent;
        padding: 15px;
        text-align: center;
        margin:10px auto ;
        width: 400px;
    }
</style>
