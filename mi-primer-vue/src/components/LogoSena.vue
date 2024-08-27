https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8j9pIw0IfLLzo0gQVekd6-1Ji2jAI3aSjCQ&s

<template>
    <img id="logo" :src="imagenURL" :alt="imagenALT">
</template>

<script>

export default {
    data() {
        return {
            imagenURL:"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8j9pIw0IfLLzo0gQVekd6-1Ji2jAI3aSjCQ&s",
            imagenALT:"Logo de un gato gordo"
        };
    }
};
</script>


<style>
#logo{
    border-radius: 60%;
    border: 5px solid rebeccapurple;
}
</style>