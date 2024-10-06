<template>
  <div class="form-container">
    <h1>Registrar Usuario</h1>
    <form @submit.prevent="registrarUsuario">
      <div class="form-group">
        <label for="documento">Documento (10 caracteres)</label>
        <input type="number" v-model="usuario.documento" required />
        <div v-if="documentoError" class="error">{{ documentoError }}</div>
      </div>

      <div class="form-group">
        <label for="nombre">Nombre</label>
        <input type="text" v-model="usuario.nombre" required />
        <div v-if="nombreError" class="error">{{ nombreError }}</div>
      </div>

      <div class="form-group">
        <label for="apellido">Apellido</label>
        <input type="text" v-model="usuario.apellido" required />
        <div v-if="apellidoError" class="error">{{ apellidoError }}</div>
      </div>

      <div class="form-group">
        <label for="correo">Correo</label>
        <input type="email" v-model="usuario.correo" required />
        <div v-if="correoError" class="error">{{ correoError }}</div>
      </div>

      <div class="form-group">
        <label for="password">Contraseña (mínimo 8 caracteres, incluye letras y caracteres especiales)</label>
        <input type="password" v-model="usuario.password" required />
        <div v-if="passwordError" class="error">{{ passwordError }}</div>
      </div>

      <div class="form-group">
        <label for="rol">Rol</label>
        <select v-model="usuario.rol" required>
          <option value="" disabled selected>Selecciona un rol</option>
          <option value="administrador">Administrador</option>
          <option value="profesor">Profesor</option>
          <option value="estudiante">Estudiante</option>
        </select>
      </div>

      <button type="submit">Registrar</button>

      <div v-if="mensaje" class="mensaje">{{ mensaje }}</div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

// Variables reactivas para almacenar los datos del usuario y los mensajes
const usuario = ref({
  documento: '',
  nombre: '',
  apellido: '',
  correo: '',
  password: '',
  rol: '',
});

const mensaje = ref('');
const documentoError = ref('');
const nombreError = ref('');
const apellidoError = ref('');
const correoError = ref('');
const passwordError = ref('');

// Función para validar los campos del formulario
const validarFormulario = () => {
  let isValid = true;
  
  // Validar documento
  if (String(usuario.value.documento).length !== 10) {
    documentoError.value = 'El documento debe tener 10 caracteres';
    isValid = false;
  } else {
    documentoError.value = '';
  }

  // Validar nombre
  if (!/^[a-zA-Z]+$/.test(usuario.value.nombre)) {
    nombreError.value = 'El nombre solo debe contener letras';
    isValid = false;
  } else {
    nombreError.value = '';
  }

  // Validar apellido
  if (!/^[a-zA-Z]+$/.test(usuario.value.apellido)) {
    apellidoError.value = 'El apellido solo debe contener letras';
    isValid = false;
  } else {
    apellidoError.value = '';
  }

  // Validar correo
  if (!/\S+@\S+\.\S+/.test(usuario.value.correo)) {
    correoError.value = 'El correo debe contener un "@" y un "."';
    isValid = false;
  } else {
    correoError.value = '';
  }

  // Validar contraseña
  if (!/^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$/.test(usuario.value.password)) {
    passwordError.value = 'La contraseña debe tener al menos 8 caracteres, una letra mayúscula, una letra minúscula y un carácter especial';
    isValid = false;
  } else {
    passwordError.value = '';
  }

  return isValid;
};

// Función para registrar el usuario
const registrarUsuario = async () => {
  if (validarFormulario()) {
    try {
      const response = await axios.post('http://127.0.0.1:8000/insertar', usuario.value);
      mensaje.value = 'Usuario registrado con éxito';
      console.log('Registro exitoso:', response.data);

      // Limpia el formulario después del registro exitoso
      usuario.value = {
        documento: '',
        nombre: '',
        apellido: '',
        correo: '',
        password: '',
        rol: '',
      };
    } catch (error) {
      console.error('Error al registrar usuario:', error);
      mensaje.value = 'Error al registrar usuario';
    }
  }
};
</script>

<style scoped>
.form-container {
  max-width: 400px;
  margin: 50px auto;
  padding: 1em;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: #f9f9f9;
}

h1 {
  text-align: center;
  background: transparent;
}

.form-group {
  margin-bottom: 1em;
}

label {
  display: block;
  margin-bottom: 0.5em;
}

input, select {
  width: 100%;
  padding: 0.5em;
  box-sizing: border-box;
  border-radius: 4px;
  border: 1px solid #ccc;
}

button {
  width: 100%;
  padding: 0.7em;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

.error {
  color: red;
  font-size: 0.9em;
}

.mensaje {
  margin-top: 1em;
  text-align: center;
  color: green;
}
</style>

