<template>
    <div class="greetings">
        <h1>¡Bienvenido <span> {{username}} </span>!</h1>
        <h2>Id: <span>{{id}}</span></h2>
        <h2>Nombre: <span>{{nombre}}</span></h2>
        <h2>Apellido: <span>{{apellido}}</span></h2>
        <h2>Edad: <span>{{edad}}</span></h2>
        <h2>Rol: <span>{{id_rol}}</span></h2>
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
    import jwt_decode from "jwt-decode";
    import axios from 'axios';

    export default {
        name: "Home",

        data: function(){
            return {
                id: "",
                username: "",
                nombre: "",
                apellido: "",
                edad: "",
                id_rol: "",
                }
            },
            
        methods: {
            getData: async function () {
                if (localStorage.getItem("token_access") === null || localStorage.getItem("token_refresh") === null) {
                    this.$emit('logOut');
                    return;
                }
                
                await this.verifyToken();
                
                let token = localStorage.getItem("token_access");
                let userId = jwt_decode(token).user_id.toString();
                
                axios.get(`http://127.0.0.1:8000/user/${userId}/`, {headers: {'Authorization': `Bearer ${token}`}})
                    .then((result) => {
                        this.id = result.data.id;
                        this.username = result.data.username;
                        this.nombre = result.data.nombre;
                        this.apellido = result.data.apellido;
                        this.edad = result.data.edad;
                        this.id_rol = result.data.id_rol;
            })
                    .catch(() => {
                        this.$emit('logOut');
                    });
            },
            
            verifyToken: function () {
                return axios.post("http://127.0.0.1:8000/refresh/", {refresh: localStorage.getItem("token_refresh")}, {headers: {}})
                
                    .then((result) => {
                        localStorage.setItem("token_access", result.data.access);
                    })
                    
                    .catch(() => {
                        this.$emit('logOut');
                    });
                },

            logOut: function () {
                localStorage.clear();
                this.$router.push({ name: "logIn" });
                this.verifyAuth();
                },
           },
           
           created: async function(){
                this.getData();
            },
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
