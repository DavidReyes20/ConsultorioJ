import { createRouter, createWebHistory } from 'vue-router';
import insertar from '@/components/insertar.vue';
import conexion from '@/components/conexion.vue';
import actualizar from '@/components/actualizar.vue';
import loginregistro from '@/components/loginregistro.vue';
import profesor from '@/components/profesor.vue';
import HomeComponent from '@/components/HomeComponent.vue';
import Recursos from '@/components/Recursos.vue';
import estudiante from '@/components/estudiante.vue';
import administrador from '@/components/administrador.vue';
import crudusers from '@/components/crudusers.vue';
import Gestion_Casos from '@/components/Gestion_Casos.vue';


const routes = [
 
  {
    path: '/home',
    name: '/HomeComponent',
    component: HomeComponent
  },
  {
    path: '/recursos',
    name: '/recursos',
    component: Recursos
  },

  {
    path: '/insertar',
    name: '/insertar',
    component: insertar
  },
  

  {
    path: '/login',
    name: 'loginregistro',
    component: loginregistro
  },
  {
    path: '/profesor',
    name: 'profesor',
    component: profesor
  },
  {
    path: '/estudiante',
    name: 'estudiante',
    component: estudiante
  },
  {
    path: '/administrador',
    name: 'administrador',
    component: administrador
  },
  {
    path: '/crudusers',
    name: 'crudusers',
    component: crudusers
  },
  {
    path: '/gestion_casos',
    name: 'gestion_casos',
    component: Gestion_Casos
  }

];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
