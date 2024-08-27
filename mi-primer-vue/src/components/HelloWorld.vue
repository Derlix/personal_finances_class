<template>
  <div>
    <div class="col-12 col-sm-6 col-md">
      <div class="card" style="width: 18rem">
        <img src="../assets/logo.png" class="card-img-top" alt="..." />
        <div class="card-body">
          <h5 class="card-title">{{ msg }}</h5>
          <p class="card-text">{{ texto }}</p>
          <a href="#" class="btn btn-primary">{{ texto_enlance }}</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'HelloWorld',
  props:{
    msg: String,
    texto: String,
    texto_enlance:String
  }
  // setup() {
  //   const message = ref(
  //     "Aprendiendo fundamentos de vue uwuwuwuwuwuwwuwuwuwuwuwuwuwuwuwuwuwuwuwu Vue 3!"
  //   );

  //   const updateMessage = () => {
  //     message.value = "mensaje actualizado!";
  //   };
  //   //funcion flecha se asigna a una constante de esta manera () =>{ #todo el codigo}
  //   return { message, updateMessage };
  // },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
