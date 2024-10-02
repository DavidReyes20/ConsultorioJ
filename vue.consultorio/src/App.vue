<template>
  <div id="app">
        
     <Header v-if="visible"></Header> 
         
    <router-view></router-view> 
    <footer> 
        <footer>
            <div id="supppp">
                <div id="div1">
                   
                    <img id="uni" src="./img/Logo-Universidad.png" alt="">
                </div>
                  <div id="div2">
                    <span id="texffff">Donde encontrarnos</span>
                    <span id="texfff">Dirección: Sede Principal: Calle 28 No. 5B-02 Bogotá D.C. Colombia - Sur America</span>
                    <span id="texfff">Código postal: 110311</span>
                    <span id="texfff">Horario de atención: Horario: Lunes a Viernes: 8:00 a.m. a 5:00 p.m</span>
                    
                
                  </div>
                  <div id="div4">
                    <span id="texffff">Contactanos</span>
                    <span id="texfff">Teléfono PBX: 57 601 2418800 (En Mantenimiento)</span>
                    <span id="texfff">Teléfono atención al usuario: 571 282 5716 (En Mantenimiento)</span>
                    <span id="texfff">Teléfono resto del país: 018000 113044 (En Mantenimiento)</span>
                    <span id="texfff">Correo institucional: contacto@unicolmayor.edu.co</span>
                    <span id="texfff">Correo notificaciones judiciales: notificacionesjudiciales@unicolmayor.edu.co</span>
                
                  </div>
                 
        
            </div>
        
                
                <div id="div3">
                    <img id="logo22" src="../src/assets/img/logo1.png" alt="">
                    <img id="logo22" src="../src/assets/img/logo2.png" alt="">
                    <img id="logo22" src="../src/assets/img/logo3.png" alt="">
                    <img id="logo22" src="../src/assets/img/logo4.png" alt="">
                </div>
                  
        </footer>

    </footer>
  </div>
</template>

<script setup>
import{ref, watch} from 'vue'
import { useRouter } from 'vue-router';
import Header from './components/Header.vue';

const rutasmostrar= ['/profesor']

const ruta= useRouter()
const visible=ref(true)

watch(
  ()=>ruta.path,
  (nuevaruta)=>{
    visible.value=!rutasmostrar.includes(nuevaruta)
  },
  {immediate:true}
)

</script>

<style>

footer{
    background-color: rgb(230, 199, 0);
    width: 100%;
    height: auto;
    margin-top: 100px;
    position: absolute;
    display: flex;
    flex-direction: column;
}
#supppp{
    width: 100%;
    height: 300px;
    position: absolute;
    display: flex;
    flex-direction: row;
}
#div1{
    display: flex;
    flex-direction: column;
    width: 10%;
    position: relative;
    margin-top: 30px;
    margin-left: 6%;

}
#imgf{
    width: 70px;
    height: 70px;
    
}
#texf{
    margin-top: 40px;
    color: aliceblue;
    font-size: 30px;
    font-weight: bold;
}
#texf:hover{
    color: blueviolet;
}
#texff{

    color: aliceblue;
    font-size: 20px;
    font-weight: 500;
}
#div2{
    display: flex;
    flex-direction: column;
    width: 20%;
    position: relative;
    margin-top: 30px;
    margin-left: 20%;
    height: 500px;
}
#div4{
    display: flex;
    flex-direction: column;
    width: 20%;
    position: relative;
    margin-top: 30px;
    margin-left: 10%;
    height: 500px;
}


#texfff{
    margin-top: 15px;
    color: aliceblue;
    font-size: 15px;
    font-weight: 500;
}
#texffff{
    margin-top: 15px;
    color: aliceblue;
    font-size: 20px;
    font-weight: 800;
}
#texffff:hover{
    color: blueviolet;
}
#texfff:hover{
    color: blueviolet;
}

#div3{

    width: 260px;
    height: 100px;
    margin-top: 30px;
    margin-left:auto;
    margin-right: auto;
    display: flex;
    flex-direction: row;
    margin-top: 350px;

}
#logo22{
    margin-top: 15px;
    width: 50px;
    height: 50px;
    margin-left: 10px;
}

#uni{
    width: 300px;
    height: auto;
    margin-top: 20px;
}

</style>
