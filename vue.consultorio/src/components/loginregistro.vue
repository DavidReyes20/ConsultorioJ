<script setup>
import Swal from 'sweetalert2';
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

const router = useRouter();
const nombreUsuario = ref('');
const pasword = ref('');
const rol = ref('');
const documento = ref('');
const documentos = ref([]);
const frmlogin = ref(true);
const menError = ref('');

const cambioForm = async () => {
  frmlogin.value = !frmlogin.value;
  if (!frmlogin.value) {
    try {
      const response = await axios.get('http://127.0.0.1:8000/cliente/documento/');
      documentos.value = response.data;
    } catch (error) {
      menError.value = 'Error al consultar documentos';
    }
  }
};

const loginUsuario = async () => {
  if (frmlogin.value) {
    try {
      const response = await axios.post('http://127.0.0.1:8000/login', {
        nombre_usuario: nombreUsuario.value,
        password: pasword.value,
      });
      const { rol: userRol } = response.data;
      if (userRol === 'cliente') {
        router.push('/cliente');
      } else if (userRol === 'empleado') {
        router.push('/empleado');
      } else {
        errorMessages.value = 'Rol no se encontró';
      }
      Swal.fire({
        icon: 'success',
        title: 'Inicio de sesión exitoso',
        text: 'Bienvenido a tu cuenta',
      });
    } catch (error) {
      menError.value = 'Error de inicio de sesión';
      Swal.fire({
        icon: 'error',
        title: 'Error de inicio de sesión',
        text: 'Error de inicio de sesión',
      });
    }
  } else {
    try {
      const response = await axios.post('http://127.0.0.1:8000/registrousuario', {
        nombre_usuario: nombreUsuario.value,
        password: pasword.value,
        rol: rol.value,
        documento: documento.value,
      });
      Swal.fire({
        icon: 'success',
        title: 'Usuario Registrado',
        text: 'Su usuario se registró de manera exitosa',
      });
    } catch (error) {
      menError.value = 'Error en el registro de usuario';
      Swal.fire({
        icon: 'error',
        title: 'Error en el registro',
        text: 'No se pudo registrar el usuario. Por favor, inténtelo de nuevo',
      });
    }
  }
};
</script>

<template>
  <div class="auth_container">
    <h1>{{ frmlogin ? 'Iniciar sesión' : 'Registrarse' }}</h1>
    <form @submit.prevent="loginUsuario">
      <div class="form-group" v-if="!frmlogin">
        <label for="documento">Documento</label>
        <select name="documento" v-model="documento" id="documento">
          <option value="">Seleccionar documento</option>
          <option v-for="doc in documentos" :key="doc" :value="doc">
            {{ doc }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label for="nombreUsuario">Nombre Usuario</label>
        <input type="text" id="nombreUsuario" v-model="nombreUsuario" required />
      </div>

      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" id="password" v-model="pasword" required />
      </div>

      <div class="form-group" v-if="!frmlogin">
        <label for="rol">Rol</label>
        <input type="text" id="rol" v-model="rol" required />
      </div>

      <button type="submit">{{ frmlogin ? 'Iniciar sesión' : 'Registrarse' }}</button>
      <div v-if="menError" class="error">{{ menError }}</div>
      <button type="button" @click="cambioForm">
        {{ frmlogin ? 'Crear una cuenta' : 'Iniciar sesión' }}
      </button>
    </form>
  </div>
</template>

<style scoped>
.auth_container {
  max-width: 400px;
  margin: 50px auto; /* Agregar margen superior */
  padding: 1em;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: white; /* Fondo blanco */
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); /* Sombra ligera */
}

h1 {
  margin-bottom: 1em;
  text-align: center;
  color: #333; /* Color del texto */
  background-color: transparent; /* Asegurar que no haya fondo azul */
}

.form-group {
  margin-bottom: 1em;
}

label {
  display: block;
  margin-bottom: 0.5em;
  font-weight: bold;
  color: #333; /* Color del texto */
}

input, select {
  width: 100%;
  padding: 0.5em;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

button {
  background-color: #007bff; /* Botón azul */
  color: white;
  padding: 0.7em;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  width: 100%;
  margin-top: 10px;
}

button:hover {
  background-color: #0056b3; /* Azul más oscuro al pasar el ratón */
}

button[type="button"] {
  background-color: #ffc107; /* Botón amarillo */
  color: black;
  margin-top: 1em;
}

button[type="button"]:hover {
  background-color: #e0a800; /* Amarillo más oscuro al pasar el ratón */
}

.error {
  color: red;
  margin-top: 1em;
  text-align: center;
}
</style>

