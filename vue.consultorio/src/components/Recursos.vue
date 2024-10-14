<template>
  <div v-if="mensajeExito" class="mensaje-exito">{{ mensajeExito }}</div>

  <div v-if="tarjetas.length" class="tarjeta-container">
    <div class="tarjeta" v-for="tarjeta in tarjetas" :key="tarjeta.id_documento">
      <div class="card">
        <a :href="tarjeta.Url" target="_blank">
          <img src="../assets/img/power.png" alt="Card image" class="card-image" />
        </a>
        <h5 class="card-title">{{ tarjeta.nombre_recurso }}</h5>
        <p class="card-text">{{ tarjeta.descripcion }}</p>
        <p class="card-text">{{ tarjeta.tipo }}</p>
        <button @click="eliminarTarjeta(tarjeta.id_documento)" class="btn-eliminar">Eliminar</button>
        <button @click="activarEdicion(tarjeta)" class="btn-editar">Actualizar</button>
      </div>
    </div>
  </div>

  <div id="caja-formu">
    <form @submit.prevent="tarjetaEditando ? actualizarTarjeta() : crearTarjeta()" class="form-container">
      <div class="form-group">
        <label for="id">ID</label>
        <input v-model="id_documento" id="id" :disabled="tarjetaEditando" placeholder="Id del documento" required />
      </div>
      <div class="form-group">
        <label for="titulo">Título</label>
        <input v-model="titulo" id="titulo" placeholder="Título" required />
      </div>
      <div class="form-group">
        <label for="descripcion">Descripción</label>
        <textarea v-model="descripcion" id="descripcion" placeholder="Descripción" required></textarea>
      </div>
      <div class="form-group">
        <label for="nuevoAtributo">Url</label>
        <input v-model="Url" id="nuevoAtributo" placeholder="Nuevo atributo" required />
      </div>
      <div class="form-group">
        <label for="imagenUrl">Tipo</label>
        <input v-model="tipo" id="imagenUrl" placeholder="Tipo de recurso" required />
      </div>
      <button type="submit" class="btn-submit">{{ tarjetaEditando ? 'Actualizar Tarjeta' : 'Crear Tarjeta' }}</button>
      <button v-if="tarjetaEditando" type="button" @click="cancelarEdicion" class="btn-submit2">Cancelar</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const id_documento = ref('');
const titulo = ref('');
const descripcion = ref('');
const Url = ref('');
const tipo = ref('');
const tarjetas = ref([]);
const tarjetaEditando = ref(false); 
let tarjetaSeleccionada = ref(null);

const mensajeExito = ref('');

const obtenerTarjetas = async () => {
  const response = await axios.get('http://127.0.0.1:8000/consultarRecurso');
  tarjetas.value = response.data.map(tarjeta => ({ ...tarjeta, editando: false }));
};

onMounted(() => {
  obtenerTarjetas();
});

const activarEdicion = (tarjeta) => {
  tarjetaEditando.value = true; 
  tarjetaSeleccionada.value = tarjeta;
  id_documento.value = tarjeta.id_documento;
  titulo.value = tarjeta.nombre_recurso;
  descripcion.value = tarjeta.descripcion;
  Url.value = tarjeta.Url;
  tipo.value = tarjeta.tipo;
};

const cancelarEdicion = () => {
  tarjetaEditando.value = false;
  tarjetaSeleccionada.value = null;
  limpiarFormulario();
};

const crearTarjeta = async () => {
  const nuevaTarjeta = {
    id_documento: id_documento.value,
    nombre_recurso: titulo.value,
    descripcion: descripcion.value,
    tipo: tipo.value,
    Url: Url.value
  };

  try {
    await axios.post('http://127.0.0.1:8000/insertarRecurso', nuevaTarjeta);
    tarjetas.value.push({ ...nuevaTarjeta, editando: false });
    limpiarFormulario();
  } catch (error) {
    console.error('Error al crear tarjeta:', error);
  }
};

const actualizarTarjeta = async () => {
  const actualizacion = {
    id_documento: id_documento.value,
    nombre_recurso: titulo.value,
    descripcion: descripcion.value,
    tipo: tipo.value,
    Url: Url.value
  };

  try {
    const response = await axios.put(`http://127.0.0.1:8000/actualizarRecurso/${id_documento.value}`, actualizacion);

    const indice = tarjetas.value.findIndex(t => t.id_documento === id_documento.value);
    if (indice !== -1) {
      tarjetas.value[indice] = { ...response.data.recurso, editando: false };
    }

    mensajeExito.value = 'Se actualizó correctamente';
    cancelarEdicion();

    setTimeout(() => {
      mensajeExito.value = '';
    }, 3000);
  } catch (error) {
    console.error('Error al actualizar tarjeta:', error);
  }
};

const eliminarTarjeta = async (id) => {
  try {
    await axios.delete(`http://127.0.0.1:8000/eliminarRecurso/${id}/`);
    tarjetas.value = tarjetas.value.filter(t => t.id_documento !== id);
  } catch (error) {
    console.error('Error al eliminar tarjeta:', error);
  }
};

const limpiarFormulario = () => {
  id_documento.value = '';
  titulo.value = '';
  descripcion.value = '';
  Url.value = '';
  tipo.value = '';
};
</script>

  
  <style scoped>


  .tarjeta-container {
    display: flex;
    flex-wrap: wrap;
    margin-left: 3%;
    gap: 20px; 
  }

  .tarjeta-container .hola{
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 5px;
    margin-top: 150px;
    border: solid 1px rgb(24, 0, 111);
    width: 360px;
    margin-left: 400px;
  }

  .tarjeta-container .hola2{
    display: flex;
    flex-direction: column;
    max-width: 400px;
    margin: 20px 0; 
  }


  .tarjeta {
    flex-basis: calc(25% - 20px); 
    box-sizing: border-box;
  }

  .form-container {
    display: flex;
    flex-direction: column;
    max-width: 400px;
    margin: 20px 0;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  input, textarea {
    width: 100%;
    padding: 8px;
    margin-top: 5px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  button.btn-submit {
    background-color: rgb(230, 199, 0);
    color: white;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  button.btn-submit:hover {
    background-color: #0056b3;
  }

  button.btn-submit2{
    background-color: rgb(230, 199, 0);
    color: white;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    margin-top: 5px;
  }
  
  button.btn-submit2:hover {
    background-color: #0056b3;
  }


  .card {   
    border: 1px solid #e0e0e0;
    border-radius: 10px;
    padding: 15px;
    width: 300px;
    text-align: center;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    margin: 20px 0;
  }
  
  .card-image {
    width: 60px;
    margin-bottom: 15px;
  }
  
  .card-title {
    font-size: 18px;
    font-weight: bold;
  }
  
  .card-text {
    font-size: 14px;
    color: #555;
    margin-bottom: 15px;
  }
  
  h3 {
    font-size: 18px;
    margin-bottom: 20px;
  }

  .btn-eliminar {
    margin-top: 10px;
    padding: 8px 12px;
    border: none;
    border-radius: 4px;
    background-color: #dc3545;
    color: white;
    cursor: pointer;
    margin-right: 10px;
  }
  
  .btn-editar {
    margin-top: 10px;
    padding: 8px 12px;
    border: none;
    border-radius: 4px;
    background-color: #0026ff;
    color: white;
    cursor: pointer;
    margin-left: 10px;
  }
  .btn-eliminar:hover {
    background-color: #c82333;
  }

  #caja-formu{
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 5px;
    margin-top: 150px;
    border: solid 1px rgb(24, 0, 111);
    margin-left: auto;
    margin-right: auto;
    width: 350px;
  }

  .mensaje-exito {
  color: green;
  background-color: #d4edda;
  border: 1px solid #c3e6cb;
  padding: 10px;
  border-radius: 5px;
  margin-bottom: 15px;
  text-align: center;
}
  </style>
  