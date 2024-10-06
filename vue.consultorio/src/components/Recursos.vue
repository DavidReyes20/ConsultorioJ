<template>
  <div v-if="tarjetas.length" class="tarjeta-container">
    <div class="tarjeta" v-for="tarjeta in tarjetas" :key="tarjeta.id_documento">
      <div class="card">
        <img :src="getImage(tarjeta.extension)" alt="Card image" class="card-image" />
        <h5 class="card-title">{{ tarjeta.nombre_recurso }}</h5>
        <p class="card-text">{{ tarjeta.descripcion }}</p>
        <button @click="eliminarTarjeta(tarjeta.id_documento)" class="btn-eliminar">Eliminar</button>
      </div>
    </div>
  </div>

  <div id="caja-formu">
    <form @submit.prevent="crearTarjeta" class="form-container">
      <div class="form-group">
        <label for="id">ID</label>
        <input v-model="id_documento" id="id" placeholder="Id del documento" required />
      </div>
      <div class="form-group">
        <label for="titulo">Título</label>
        <input v-model="titulo" id="titulo" placeholder="Título" required />
      </div>
      <div class="form-group">
        <label for="rol">Extensión</label>
        <select v-model="extension" required>
          <option value="" disabled selected>Selecciona una extensión</option>
          <option value="docx">docx</option>
          <option value="pptx">pptx</option>
          <option value="xlm">xlm</option>
          <option value="otros">otros</option>
        </select>
      </div>
      <div class="form-group">
        <label for="descripcion">Descripción</label>
        <textarea v-model="descripcion" id="descripcion" placeholder="Descripción" required></textarea>
      </div>
      <div class="form-group">
        <label for="imagenUrl">Tipo</label>
        <input v-model="tipo" id="imagenUrl" placeholder="tipo de recurso" required />
      </div>
      <button type="submit" class="btn-submit">Crear Tarjeta</button>
    </form>
  </div>
</template>
  
  <script setup>
  import wordImage from '../assets/img/word.png';
  import powerImage from '../assets/img/power.png';
  import xlmImage from '../assets/img/xlm.png';
  import defaultImage from '../assets/img/logo-cortesuprema.png';
  import { ref, onMounted } from 'vue';
  import axios from 'axios';

  const id_documento = ref('');
  const titulo = ref('');
  const descripcion = ref('');
  const tipo = ref('');
  const tarjetas = ref([]);


  const extension = ref('');


// se tiene que usar require() para poder llamar la ruta de las imgs desde el script
  const getImage = (extension) => {
    switch (extension) {
      case 'docx':
        return wordImage; // Aquí no necesitas require
      case 'pptx':
        return powerImage;
      case 'xlm':
        return xlmImage;
      //El error esta aca al tener la img default al actualizar la pag siempre va a quedar la imsma img  
      default:
        return defaultImage;
    }
  };


  
  const obtenerTarjetas = async () => {
    const response = await axios.get('http://127.0.0.1:8000/consultarRecurso');
    tarjetas.value = response.data;
  };
  
  onMounted(() => {
    obtenerTarjetas();
  });
  

  const crearTarjeta = async () => {
  const nuevaTarjeta = {  
    id_documento: id_documento.value,
    nombre_recurso: titulo.value,
    descripcion: descripcion.value,
    tipo: tipo.value,
    extension: extension.value 
  };

  try {
    await axios.post('http://127.0.0.1:8000/insertarRecurso', nuevaTarjeta);
    tarjetas.value.push(nuevaTarjeta); 
    // Reiniciar campos
    id_documento.value = '';
    titulo.value = '';
    descripcion.value = '';
    tipo.value = '';
    extension.value = ''; 
  } catch (error) {
    console.error('Error al crear tarjeta:', error);
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

  </script>
  
  <style scoped>


  .tarjeta-container {
    display: flex;
    flex-wrap: wrap;
    margin-left: 3%;
    gap: 20px; 
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

  label {
    display: block; 
    font-weight: bold; 
    margin-bottom: 0.5rem; 
  }

  select {
    width: 100%; 
    padding: 0.5rem; 
    border: 1px solid #ccc; 
    border-radius: 4px; 
    font-size: 15px; 
  }

  select:focus {
    border-color: #007bff;
    outline: none; 
  }


  
  </style>
  
