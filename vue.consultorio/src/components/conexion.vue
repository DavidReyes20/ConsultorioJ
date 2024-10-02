<template>
    <div>
      <h1>Datos de la API</h1>
      <ul>
        <li v-for="(item, index) in data" :key="index">
          {{ item.documento }}{{ item.nombre }} {{ item.apellido }} {{ item.correo }} {{ item.celular }} 
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import { ref, onMounted } from 'vue';
 export default {
  setup() {
    const data = ref([]);

    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/clientes/');
    
          data.value = response.data;
      
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    onMounted(fetchData);

    return { data };
  }
};
  </script>
  