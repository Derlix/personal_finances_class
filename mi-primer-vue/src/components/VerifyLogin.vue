<template>
    <div>
        <button @click="toggleLogin">{{ isLoggedIn ? 'Cerrar Sesion' : 'Iniciar Sesion' }}</button>
        <p v-if="isLoggedIn">Ha iniciado Sesion</p>
        <p v-else>No has iniciado Sesion</p>
    </div>
</template>

<script>
export default{
    data(){
        return{
            isLoggedIn: false
        };
    },
    methods: {
        toggleLogin(){
            this.isLoggedIn = !this.isLoggedIn;
        }
    }
};
</script>