<template>
  <div class="form-container">
    <h1>Registrar Usuario</h1>
    <form @submit.prevent="registrarUsuario">
      <div class="form-group">
        <label for="documento">Documento</label>
        <input type="number" v-model="usuario.documento" required />
      </div>

      <div class="form-group">
        <label for="nombre">Nombre</label>
        <input type="text" v-model="usuario.nombre" required />
      </div>

      <div class="form-group">
        <label for="apellido">Apellido</label>
        <input type="text" v-model="usuario.apellido" required />
      </div>

      <div class="form-group">
        <label for="correo">Correo</label>
        <input type="email" v-model="usuario.correo" required />
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
});

const mensaje = ref('');

// Función para registrar el usuario
const registrarUsuario = async () => {
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
    };
  } catch (error) {
    console.error('Error al registrar usuario:', error);
    mensaje.value = 'Error al registrar usuario';
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

input {
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

.mensaje {
  margin-top: 1em;
  text-align: center;
  color: green;
}
</style>
