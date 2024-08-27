<template>
  <MiComponenteSlot>
    <template #header>
      <div class="row py-5">
        <VModel/>
      </div>
      <LogoSena></LogoSena>
      <h1>Titulo</h1>
      <VerifyLogin></VerifyLogin>
      <VShow></VShow>
    </template>
    <div class="row">
      
    </div>
    <template #main>
      <div class="row">
        <HelloWorld
          msg="Estrella"
          texto="estrella texto"
          texto_enlance="gei"
        ></HelloWorld>
        <HelloWorld
          msg="Luna"
          texto="Luna"
          texto_enlance="luna hermosa"
        ></HelloWorld>
        <HelloWorld
          msg="Sol"
          texto="texto sola"
          texto_enlance="solo lindo"
        ></HelloWorld>
        <HelloWorld
          msg="jupiter"
          texto="jupiter"
          texto_enlance="gay"
        ></HelloWorld>
      </div>
      <MiContador></MiContador>
    </template>
    
    <template #footer>
      
      <div class="container">
        <MiBoton></MiBoton>
        <div class="row bg-black text-white py-4">
          <MisProductos></MisProductos>
        </div>
      </div>
    </template>
  </MiComponenteSlot>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
import LogoSena from "./components/LogoSena.vue";
import MiBoton from "./components/MiBoton.vue";
import MiComponenteSlot from "./components/MiComponenteSlot.vue";
import MiContador from "./components/MiContador.vue";
import MisProductos from "./components/MisProductos.vue";
import VerifyLogin from "./components/VerifyLogin.vue";
import VModel from "./components/VModel.vue";
import VShow from "./components/VShow.vue";

export default {
  name: "App",
  components: {
    HelloWorld,
    MiBoton,
    MiComponenteSlot,
    MiContador,
    LogoSena,
    VerifyLogin,
    MisProductos,
    VModel,
    VShow
  },
  methods: {
    mostrarMensaje(mensaje) {
      alert(mensaje);
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
