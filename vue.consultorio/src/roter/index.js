import { createRouter, createWebHistory } from 'vue-router';
import insertar from '@/components/insertar.vue';
import conexion from '@/components/conexion.vue';
import actualizar from '@/components/actualizar.vue';
import loginregistro from '@/components/loginregistro.vue';
import Profesor from '@/components/profesor.vue';
import Recursos from '@/components/Recursos.vue';
import HomeComponent from '@/components/HomeComponent.vue';



const routes = [
 
  {
    path: '/home',
    name: '/HomeComponent',
    component: HomeComponent
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
    component: Profesor
  },
  {
    path: '/recursos',
    name: 'recursoslegales',
    component: Recursos
  }

];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
