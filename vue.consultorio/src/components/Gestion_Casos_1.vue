<template>
    <template>
    <div class="cajamayor">
      <h2>Agregar Usuario</h2>
      
      <!-- <div class="buscar-agregar">
        <form @submit.prevent="getLocalCase" class="form-agregar">
          <input v-model="nuevoUsuario.documento" placeholder="Documento" required />
          <input v-model="nuevoUsuario.nombre" placeholder="Nombre" required />
          <input v-model="nuevoUsuario.apellido" placeholder="Apellido" required />
          <input v-model="nuevoUsuario.correo" placeholder="Correo" required />
          <button id="agregar" type="submit">Agregar</button>
        </form> -->
  
        <!-- <input 
          v-model="terminoBusqueda"
          placeholder="Buscar usuario..."
          @input="buscarUsuario"
          class="input-busqueda"
        /> -->
      </div>
      
  
      <!-- <table>
        <thead>
          <tr>
            <th>Documento</th>
            <th>Nombre</th>
            <th>Apellido</th>
            <th>Correo</th>
            <th>Opciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(usuario, index) in usuariosFiltrados" :key="index">
            <td>{{ usuario.documento }}</td>
            <td>{{ usuario.nombre }}</td>
            <td>{{ usuario.apellido }}</td>
            <td>{{ usuario.correo }}</td>
            <td>
            <div class="botones-opciones">
              <button class="btn-modificar" @click="modificarUsuario(usuario)">Modificar</button>
              <button class="btn-eliminar" @click="eliminarUsuario(usuario.documento)">Eliminar</button>
            </div>
          </td>
          </tr>
        </tbody>
      </table> -->
               <!-- <button @click="getLocalCases">consultar usuario</button> -->
               <!-- <ul>
    <li v-for="value in cases" :key="value.id" >
      {{ value}}
    </li> -->
  <!-- </ul> -->
    <!-- </div> -->

  </template>

    
 

  
      

  
  
  <script >
    import { ref, onMounted } from 'vue';
    import axios from 'axios';
    import getCases from '@/services/cases/getCases';
    
    
export default {
    data() {
        return {
            cases: []
        }
    },
    mounted(){
        this.getLocalCases()
    },
    methods: {
        async getLocalCases ()  {
            this.cases= await getCases()
            
        }
    }
}

  </script>
  
  <style scoped>
    .cajamayor {
      width: 90%;
      margin-left: auto;
      margin-right: auto;
    }

    h2 {
      margin-bottom: 10px;
    }

    .buscar-agregar {
      display: flex;
      align-items: flex-end;
      margin-bottom: 20px;
    }

    .input-busqueda {
      margin-left: 200px; 
      padding: 8px;
      border: 1px solid #ddd;
      border-radius: 4px;
    }

    .form-agregar {
      display: flex;
    }

    form input {
      margin-right: 10px;
      padding: 8px;
      border: 1px solid #ddd;
      border-radius: 4px;
    }

    button {
      padding: 8px 12px;
      border: none;
      color: white;
      border-radius: 4px;
      cursor: pointer;
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
  </style>
  