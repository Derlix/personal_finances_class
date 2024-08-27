
<template>
    <div>
        <p>Contador:{{ contador }}</p>
        <button @click="incrementar">Incrementar</button>
    </div>
</template>

<script>
import {ref} from 'vue';

export default {
    setup(){
        const contador = ref(0);

        const incrementar = () => {
            contador.value++;
        };
        return {contador, incrementar};
    }
}
</script>