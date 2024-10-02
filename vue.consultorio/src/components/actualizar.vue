<template>
  <div>
    <h1>Actualizar Datos del Documento</h1>
    <form @submit.prevent="fetchDocument">
      <input v-model="documentId" placeholder="Ingresa el ID del documento" />
      <button type="submit">Cargar Datos</button>
    </form>

    <form v-if="data" @submit.prevent="updateData">
      <div>
        <input v-model="data.nombre" placeholder="Campo 1" />
        <input v-model.number="data.apellido" placeholder="Campo 2" type="number" />
      </div>
      <button type="submit">Actualizar Datos</button>
    </form>

    <p v-if="message">{{ message }}</p>
  </div>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';

export default {
  setup() {
    const documentId = ref('');
    const data = ref(null);
    const message = ref('');

    // Función para cargar los datos del documento
    const fetchDocument = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/data/${documentId.value}`); // Ajusta la URL a tu endpoint
        data.value = response.data;
        message.value = '';
      } catch (error) {
        console.error('Error fetching document:', error);
        message.value = 'Error al cargar los datos del documento';
      }
    };

    // Función para actualizar los datos del documento
    const updateData = async () => {
      try {
        await axios.put(`http://localhost:8000/update/${documentId.value}`, data.value); // Ajusta la URL a tu endpoint
        message.value = 'Datos actualizados correctamente';
      } catch (error) {
        console.error('Error updating data:', error);
        message.value = 'Error al actualizar los datos';
      }
    };

    return {
      documentId,
      data,
      message,
      fetchDocument,
      updateData
    };
  }
};
</script>

<style scoped>
/* Estilos opcionales */
</style>
