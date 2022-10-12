<template>
    <div class="greetings">
        <h1>¡Bienvenido <span> {{username}} </span>!</h1>
        <h2>Id: <span>{{id}}</span></h2>
        <h2>Nombre: <span>{{nombre}}</span></h2>
        <h2>Apellido: <span>{{apellido}}</span></h2>
        <h2>Edad: <span>{{edad}}</span></h2>
        <h2>Rol: <span>{{rol}}</span></h2>
        <nav>
            <button v-if="!is_auth" v-on:click="logOut" > Salir </button>  
        </nav>
    </div>

    <div>
        <router-view
            v-on:logOut="logOut"
        >
        </router-view>
    </div>
</template>


<script>
    export default {
        name: "Home",
        data: function(){
            return {
                id: localStorage.getItem('id') || "none",
                username: localStorage.getItem('username') || "none",
                nombre: localStorage.getItem('Nombre') || "none",
                apellido: localStorage.getItem('apellido') || "none",
                edad: localStorage.getItem('edad') || "none",
                rol: localStorage.getItem('rol') || "none",
            }
        },

        methods:{
            
            logOut: function () {
                localStorage.clear();
                this.$router.push({ name: "logIn" });
                this.verifyAuth();
                },
            }
        }
</script>


<style>
    .greetings{
        margin: 0;
        padding: 0%;
        display: table;
        text-align: center;
        width: 100%;
        height: 2px;
        }

    .greetings h1{
        font-size: 60px;
        color: #283747;
        }
    
    .greetings h2{
        font-size: 40px;
        color: #283747;
        display: table;
        text-align: center;
        width: 100%;
        height: 2px;
        }

    .greetings span{
        color: crimson;
        font-weight: bold;
        }
    
    .greetings nav button{
        color: #E5E7E9;
        background: #48bff7;
        border: 1px solid #E5E7E9;
        border-radius: 5px;
        padding: 10px 20px;
        align-items: center;
    }

  .greetings nav button:hover{
        color: #48bff7;
        background: #E5E7E9;
        border: 1px solid #E5E7E9;
    }
</style>
