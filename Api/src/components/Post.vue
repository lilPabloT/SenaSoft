<template>
    <div style="width: 45%; height: 100%; padding-top: 100px">
        <v-text-field 
        label="Titulo de la tarea"
        v-model=titulo
        variant="solo-filled">
        </v-text-field>

        <v-text-field
        label="Informacion de la tarea"
        v-model="texto"
        variant="solo-filled">
        </v-text-field>

        <v-btn @click="post"> Crear tarea </v-btn>
    </div>
</template>

<script>

    import { useAppStore } from '@/store/app';
    import { reactive, toRefs } from 'vue';

    export default{

        setup(){

            const store = useAppStore()

            // Conjunto de variables para enviar el post

            const variablesPost = reactive({

                titulo: '',
                texto: '',

                // Cuadro de confirmacion cuando se ejecute la funcion

                postEnviado: false,
                postError: false

            })

            function post(){

                fetch("http://127.0.0.1:8000/api/tareas/", {
                    method: 'POST',
                    body: JSON.stringify({
                        titulo: variablesPost.titulo,
                        texto: variablesPost.texto,
                        estado: 'Pendiente'
                    }),
                    headers: {"Content-type" : "application/json"}
                })

                setTimeout(() => {

                    fetch("http://127.0.0.1:8000/api/tareas/")
                        .then(res => res.json())
                        .then(data => {store.tareas = data.reverse()})

                }, 500)

            }

            return{...toRefs(variablesPost), post}

        }

    }

</script>