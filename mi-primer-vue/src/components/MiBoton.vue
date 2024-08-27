<template>
    <button @click="enviarMensaje" >Has click aqui</button>
</template>

<script>

export default{
    methods: {
        enviarMensaje(){
            this.$emit('mensaje-envia',"Hola desde componenete hiji");
        }
        
    }
};

</script>
