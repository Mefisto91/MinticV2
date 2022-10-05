<template>
    <div class="M1Mod">
		<h1>
			<div class="sharingan">
				<div class="linea interior">
						<div class="triangulo">	
						</div>
				</div>
				<div class="linea interior" style="width: 50%;height: 50%;background-color:black ;">	
				</div>
			</div>
		</h1>
		<h2 id="title">Step to Hell Hospital</h2>
		<h3>Modulo de Actualizacion</h3>
			<div class="tabs">
				<table>
					<tr>
						<td>ID</td>
						<td>
							<form>
								<output type="username" required="" name="username">
							</form>
						</td>
                        <td>
							<form>
								<input type="username" required="" name="username">
							</form>
						</td>
					</tr>
					<tr>
						<td>Nombre Usuario</td>
						<td>
							<form>
								<output type="nombre" required="" name="nombre">
							</form>
						</td>
                        <td>
							<form>
								<input type="nombre" required="" name="nombre">
							</form>
						</td>
						</tr>
						<tr>
                            <td>Apellidos Usuario</td>
                            <td>
                                <form>
                                    <output type="apellido" required="" name="apellido">
                                </form>
                            </td>
                            <td>
                                <form>
                                    <input type="apellido" required="" name="apellido">
                                </form>
                            </td>
                        </tr>
                        <tr>
                            <td>Nombre Medico Asignado</td>
						    <td>
							    <form>
								    <output type="NUser" required="" name="NUser">
							    </form>
						    </td>
                            <td>
							    <form>
								    <input type="NUser" required="" name="NUser">
							    </form>
						    </td>
						</tr>
						<tr>
                            <td>Nombre Familiar</td>
                            <td>
							    <form>
								    <output type="id_familiar" required="" name="id_familiar">
							    </form>
						    </td>
                            <td>
							    <form>
								    <input type="id_familiar" required="" name="id_familiar">
							    </form>
						    </td>
						</tr>
						<tr>
                            <td>Dirección</td>
						    <td>
							    <form>
								    <output type="direccion" required="" name="direccion">
							    </form>
						    </td>
                            <td>
							    <form>
								    <input type="direccion" required="" name="direccion">
							    </form>
						    </td>
						</tr>
						<tr>
                            <td>contraseña</td>
						    <td>
							<form>
								<output type="password" required="" name="password">
							</form>
						    </td>
                            <td>
							<form>
								<input type="password" required="" name="password">
							</form>
						    </td>
					    </tr>
                        <tr>
                            <td>Tipo de registro</td>
						    <td>
							<form>
								<output type="id_rol" required="" name="id_rol">
							</form>
						    </td>
                            <td>
							<form>
								<input type="id_rol" required="" name="id_rol">
							</form>
						    </td>
					</tr>
				</table>
			</div>
			<div>	
			<button id="Modificar">Actualizar</button>
			</div>
	</div>
</template>
<script>
    import axios from "axios";
    export default {
      name: 'M1Mod',
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
    .M1Mod{
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
    #Modificar{
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
    .tabs{
	text-align: left;
	text-decoration-color: gray;
    }
    </style>