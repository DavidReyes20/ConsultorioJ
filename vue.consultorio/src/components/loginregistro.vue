<template>
  <div class="auth_container">
    <h1>Iniciar sesión</h1>
    <form @submit.prevent="loginUsuario">
      <div class="form-group">
        <label for="documento">Documento</label>
        <input type="number" id="documento" v-model="documento" required />
      </div>

      <div class="form-group">
        <label for="rol">Rol</label>
        <select id="rol" v-model="rol" required>
          <option value="">Seleccionar rol</option>
          <option value="administrador">Administrador</option>
          <option value="profesor">Profesor</option>
          <option value="estudiante">Estudiante</option>
        </select>
      </div>

      <div class="form-group">
        <label for="password">Contraseña</label>
        <input type="password" id="password" v-model="pasword" required />
      </div>

      <button type="submit">Iniciar sesión</button>
      <div v-if="menError" class="error">{{ menError }}</div>
    </form>
  </div>
</template>

<script setup>
import Swal from 'sweetalert2';
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

const router = useRouter();
const documento = ref('');
const rol = ref(''); 
const pasword = ref('');
const menError = ref('');

const loginUsuario = async () => {
  // Verificar si el rol es válido
  if (!['administrador', 'profesor', 'estudiante'].includes(rol.value)) {
    menError.value = 'Por favor, seleccione un rol válido.';
    return; // Salir de la función si el rol no es válido
  }

  try {
    const response = await axios.post('http://127.0.0.1:8000/login', {
      documento: documento.value,
      password: pasword.value,
      rol: rol.value, // Incluyendo el rol en la solicitud
    });

    const { rol: userRol } = response.data;  // Obtener el rol 

    // Redirigir según el rol
    if (userRol === 'administrador') {
      router.push('/administrador');
    } else if (userRol === 'profesor') {
      router.push('/profesor');
    } else if (userRol === 'estudiante') {
      router.push('/estudiante');
    } else {
      throw new Error('Rol no válido');  
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
      text: error.response?.data?.detail || 'Error al iniciar sesión. Inténtalo de nuevo.',
    });
  }
};
</script>

<style scoped>
.auth_container {
  max-width: 400px;
  margin: 50px auto;
  padding: 1em;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: white;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

h1 {
  margin-bottom: 1em;
  text-align: center;
  color: #333;
  background: transparent;
}

.form-group {
  margin-bottom: 1em;
}

label {
  display: block;
  margin-bottom: 0.5em;
  font-weight: bold;
}

input, select {
  width: 100%;
  padding: 0.5em;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

button {
  background-color: #007bff;
  color: white;
  padding: 0.7em;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  width: 100%;
  margin-top: 10px;
}

button:hover {
  background-color: #0056b3;
}

.error {
  color: red;
  margin-top: 1em;
  text-align: center;
}
</style>


