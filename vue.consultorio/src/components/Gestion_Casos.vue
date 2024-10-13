<template>
    <div class="cajamayor">
      <h2>Gestion de Caso</h2>
      
      <div class="buscar-agregar">
        <form @submit.prevent="agregarCaso" class="form-agregar">
          <input v-model="nuevoCaso.numero_caso" placeholder="Num_caso" required />
          <input v-model="nuevoCaso.nombre_usuario" placeholder="Nom_Usuario" required />
          <input v-model="nuevoCaso.apellido_usuario" placeholder="Ape_Usuario" required />
          <input v-model="nuevoCaso.documento_usuario" placeholder="Doc_Usuario" required />
          <input v-model="nuevoCaso.tipo_caso" placeholder="Tipo de caso" required />
          <input v-model="nuevoCaso.estado_caso" placeholder="estado caso" required />
          <input v-model="nuevoCaso.link_carpeta" placeholder="Link Carpeta" required />
          <input v-model="nuevoCaso.id_persona_abre_caso" placeholder="cc_estudiante" required />
          <button id="agregar" type="submit">Agregar</button>
        </form>
        
    </div>
        
      
  
      <table>
        <thead>
          <tr>
            <th>Num_caso</th>
            <th>Nom_Usuario</th>
            <th>Ape_Usuario</th>
            <th>Doc_Usuario</th>
            <th>Tipo de caso</th>
            <th>Estado Caso</th>
            <th>Link Carpeta"</th>
            <th>CC_estudiante"</th>
            <th>Opciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(usuario, index) in usuariosFiltrados" :key="index">
            <td>{{ usuario.numero_caso }}</td>
            <td>{{ usuario.nombre_usuario }}</td>
            <td>{{ usuario.apellido_usuario }}</td>
            <td>{{ usuario.documento_usuario }}</td>
            <td>{{ usuario.tipo_caso }}</td>
            <td>{{ usuario.estado_caso }}</td>
            <td>{{ usuario.link_carpeta }}</td>
            <td>{{ usuario.id_persona_abre_caso}}</td>
            <td>
            <div class="botones-opciones">
              <button class="btn-eliminar" @click="eliminarCaso(usuario.numero_caso)">Eliminar</button>
            </div>
          </td>
          </tr>
        </tbody>
      </table>
      <!-- Ejecuta la función al presionar Enter  -->
      <input 
        v-model="terminoBusqueda"
        placeholder="Buscar usuario..."
        @keyup.enter="buscarUsuario"  
      />
    </div>
  </template>
  
  
  <script setup>
    import { ref, onMounted } from 'vue';
    import axios from 'axios';
    
    const usuarios = ref([]);
    const usuariosFiltrados = ref([]);
    const nuevoCaso = ref({
        numero_caso: '',
        nombre_usuario: '',
        apellido_usuario: '',
        documento_usuario: '',
        tipo_caso: '',
        estado_caso: '',
        link_carpeta: '',
        id_persona_abre_caso: ''
    });
    const terminoBusqueda = ref('');
    
    const obtenerUsuarios = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/consultar_lista_casos');
        usuarios.value = response.data;
        usuariosFiltrados.value = usuarios.value; // Inicializa usuariosFiltrados
      } catch (error) {
        console.error('Error al obtener usuarios:', error);
      }
    };
    
    const agregarCaso = async () => {
      try {
        const response = await axios.post('http://127.0.0.1:8000/insertar_caso', nuevoCaso.value);
        usuarios.value.push(response.data); // Agrega el nuevo usuario
        usuariosFiltrados.value.push(response.data); // También a la lista filtrada
        nuevoCaso.value = { num_caso: '', nom_usuario: '', ape_usuario: '', doc_usuario: '', tipo_caso: '', link_carpeta: '', cc_estudiante: ''}; // Reinicia el formulario
      } catch (error) {
        console.error('Error al agregar usuario:', error);
      }
    };



    const eliminarCaso = async (n_caso) => {
        try {
          await axios.delete(`http://127.0.0.1:8000/eliminar_casos/${n_caso}/`);
          usuarios.value = usuarios.value.filter(usuario => usuario.numero_caso !== n_caso); // Elimina el usuario de la lista
          usuariosFiltrados.value = usuariosFiltrados.value.filter(usuario => usuario.numero_caso !== n_caso); // Actualiza la lista filtrada
        } catch (error) {
          console.error('Error al eliminar usuario:', error);
        }
    };

    const buscarUsuario = () => {
    const busqueda = terminoBusqueda.value.toLowerCase();
    usuariosFiltrados.value = usuarios.value.filter(usuario => {
      return (
        usuario.numero_caso.toString().toLowerCase().includes(busqueda) ||
        usuario.nombre_usuario.toLowerCase().includes(busqueda) ||
        usuario.apellido_usuario.toLowerCase().includes(busqueda) ||
        usuario.documento_usuario.toLowerCase().includes(busqueda) ||
        usuario.tipo_caso.toLowerCase().includes(busqueda) ||
        usuario.estado_caso.toLowerCase().includes(busqueda) ||
        usuario.link_carpeta.toLowerCase().includes(busqueda) ||
        usuario.id_persona_abre_caso.toLowerCase().includes(busqueda)
      );
    });
};
    
    
    onMounted(obtenerUsuarios);

  </script>
  
  <style scoped>
    .cajamayor {
      width: 95%;
      margin-left: auto;
      margin-right: auto;
    }

    h2 {
      margin-bottom: 10px;
    }

    .buscar-agregar {
      display: flex;
      align-items: flex-end;
      margin-bottom: 0px;
    }

    .input-busqueda {
      margin-left: 200px; 
      padding: 8px;
      border: 1px solid #ddd;
      border-radius: 4px;
    }

    .form-agregar {
      width: 100%;
      display: flex;
      flex-wrap: wrap; /* Para permitir que los inputs se ajusten */
      gap: 10px; /* Espacio entre los inputs */
    }

    form input {
      flex: 1 1 calc(25% - 10px); /* Hace que cada input ocupe el 25% del ancho disponible menos 10px de espacio */
      padding: 8px;
      border: 1px solid #ddd;
      border-radius: 4px;
      min-width: 150px; /* Ancho mínimo para que no se haga muy pequeño en pantallas pequeñas */
    }

    button {
      padding: 8px 12px;
      border: none;
      color: white;
      border-radius: 4px;
      cursor: pointer;
      flex: 1 1 100%; /* Hace que el botón ocupe toda la fila */
    }

    button:hover {
      opacity: 0.9; 
    }

    .btn-modificar {
      background-color: #007bff; 
      margin-right: 5px; 
    }

    .btn-eliminar {
      background-color: #dc3545; 
    }

    #agregar {
      background-color: #05dc28; 
    }

    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 20px;
    }

    th, td {
      border: 1px solid #ddd;
      padding: 8px;
      text-align: left;
    }

    th {
      background-color: #f2f2f2;
    }

    tbody tr:hover {
      background-color: #f5f5f5;
    }

    .botones-opciones {
      display: flex; 
    }
    .badd{
      background-color: white;
      margin-top: 10px;
    }
</style>

  