<template>
    <div class="LoginUs">
          
      <h1 id="@keyframes sharingan"></h1>
      <h2 id="title">Step to Hell Hospital</h2>
      <form>
          <input type="utf-8" name="Identificación">
      </form>
      <form>
          <input type="utf-8" name="Contraseña">
      </form>
      <button id="Enter">Enter</button>
      <h3>
      </h3>
      <h6></h6>
      <h4>
      </h4>
      <h6>
          <a href="login.html">Español(España)</a>
          <a href="LoginUs.html">Englis(US)</a>
          <a href="LoginFR.html">Francais(France)</a>
          <a href="LoginBR.html">Portugues(Brasil)</a>
          <a href="LoginIT.html">Italiano</a>
          <button>+
              <a href="index.html"></a>
          </button>
      </h6>
      <h6></h6>
      <h6></h6>
      <h6></h6>
    
          </div>
          
  </template>
  
  <script>
  export default {
    name: 'LoginUS',
    props: {
      msg: String
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
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
  .LoginUs{
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