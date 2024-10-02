<template>
 <div class="seccion">
        <div class="seccion-imagen">
            <img src="../assets/img/fondo section 1.jpg" alt="Consultorio Jurídico Medellín">
            <div class="overlay-texto">
                <h1>Consultorio Jurídico Colegio Mayor De Cundinamarca</h1>
            </div>
        </div>
        <div class="seccion-contenido">
            
            <h2>Consultorio Jurídico y Centro de Conciliación Pío XII de la Facultad de Derecho, UPB-Cundinamarca</h2>
            <div class="sidebar">
                <h3>Requisitos</h3>
                    <ul>
                        <li>Acreditar pertenecer a estratos 1 y 2 o puntaje equivalente en el SISBEN (categoría A, B y C).</li>
                        <li>Fotocopia de la cédula de ciudadanía o documento equivalente.</li>
                        <li>Fotocopia de un recibo de servicio público, con dirección y donde se especifique el estrato.</li>
                        <li>El servicio de representación en procesos judiciales o administrativos está supeditado a las competencias que la ley permite, actuando como apoderado un estudiante de la Carrera de Derecho de los últimos semestres.</li>
                        <li>De manera excepcional, sin consideración al estrato o SISBEN, se podrán atender casos de marcada vulnerabilidad, sujetos de especial protección, comunidades o personas jurídicas sin ánimo de lucro o asociaciones o agremiaciones de tipo comunitario o territorial.</li>
                    </ul>

            </div>
        </div>
    </div>
    <section class="news-section">
        <h2>Últimas Noticias</h2>
        <div class="news-container">
            <article class="news-item">
                <img src="../assets/img/im1.jpeg" alt="Noticia 1">
                <div class="news-content">
                    <h3>Conciliación gratuita</h3>
                    <p>Inscribete en la conciliaton de manera gratuta en el consultorio de la universidad Cundinamarca.</p>
                </div>
            </article>

            <article class="news-item">
                <img src="../assets/img/im2.jpg" alt="Noticia 2">
                <div class="news-content">
                    <h3>Potcas</h3>
                    <p>En terate de como solucionar conflictos familiares.</p>
                </div>
            </article>

            <article class="news-item">
                <img src="../assets/img/img3.jpeg" alt="Noticia 3">
                <div class="news-content">
                    <h3>Tutorias</h3>
                    <p>Tutorias de Dereche procesal.</p>
                </div>
            </article>

            <article class="news-item">
                <img src="../assets/img/nota-2-consultorio.png" alt="Noticia 3">
                <div class="news-content">
                    <h3>Conflictos</h3>
                    <p>Mecanismos alternativos de soluciones de conflictos.</p>
                </div>
            </article>
            <article class="news-item">
                <img src="../assets/img/sala-laboral.jpg" alt="Noticia 3">
                <div class="news-content">
                    <h3>Consultorio de asesorias </h3>
                    <p>Derecho civil y familiar Decho penal Derecho laboral y seguridad social .</p>
                </div>
            </article>
        </div>
    </section>
    
</template>

<script setup>
</script>

<style scoped>
.seccion {
    display: flex;
    flex-direction: column;
}
h1{
  background: transparent;
}
.seccion-imagen {
    position: relative;
    width: 100%;
    max-height: 500px;
    overflow: hidden;
}

.seccion-imagen img {
    width: 100%;
    height: auto;
}

.overlay-texto {
    position: absolute;
    bottom: 20px;
    left: 20px;
    color: white;
    background-color: rgba(0, 0, 0, 0.5);
    padding: 10px 20px;
    border-radius: 5px;
    
}

.seccion-contenido {
    padding: 20px;
}

.sidebar {
    background-color: #3366CC; 
    color: white;
    padding: 15px;
    border-radius: 5px;
}

.sidebar h3 {
    margin-top: 0;
}

.sidebar ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.sidebar ul li {
    margin-bottom: 10px;
}

.sidebar ul li a {
    text-decoration: none;
    color: white;
}

.sidebar ul li a:hover {
    text-decoration: underline;
}
.news-section {
    max-width: 1200px;
    margin: 20px auto;
    padding: 20px;
    background-color: #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
}

.news-section h2 {
    text-align: center;
    margin-bottom: 20px;
    font-size: 2rem;
    color: #333;
}

.news-container {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
 

}

.news-item {
    flex: 1 1 calc(33.333% - 20px);
    background-color: #f9f9f9;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s;
    border: solid 1px rgb(230, 199, 0);
}

.news-item:hover {
    transform: translateY(-5px);
}

.news-item img {
    width: 100%;
    height: auto;
    display: block;
}

.news-content {
    padding: 15px;
}

.news-content h3 {
    font-size: 1.5rem;
    margin-bottom: 10px;
    color: #007BFF;
}

.news-content p {
    font-size: 1rem;
    color: #666;
}

</style>