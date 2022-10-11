<template>
    <div class="greetings">
        <h1>¡Bienvenido <span> {{username}} </span>!</h1>
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
                username: localStorage.getItem('username') || "none"
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
        height: 10vh;
        width: 100%;
        min-height: 100px;
        display: flex;
        justify-content: center;
        align-items: center;
        }

    .greetings h1{
        font-size: 50px;
        color: #283747;
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
    }

  .greetings nav button:hover{
        color: #48bff7;
        background: #E5E7E9;
        border: 1px solid #E5E7E9;
    }
</style>
