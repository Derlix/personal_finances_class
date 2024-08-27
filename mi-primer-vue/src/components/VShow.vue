<template>
    <div>
        <button @click="mostrar = !mostrar">Toggle Mostrar </button>
        <p v-show="mostrar">Este parrafo se oculta o muestra sin eliminar del dom</p>
    </div>
</template>

<script>
export default{
    data(){
        return{
            mostrar:true
        };
    }
};
</script>