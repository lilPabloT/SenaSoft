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

        <v-dialog v-model="postEnviado">
            <v-alert style="margin: auto; width: max-content" class="pa-5" type="success">
              <v-alert-title> Enviado! </v-alert-title>
              El registro se ha enviado correctamente
              <br>
              <br>
              <v-btn @click="postEnviado = false"> Cerrar </v-btn>
            </v-alert>
        </v-dialog>
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

                variablesPost.postEnviado = true

            }

            return{...toRefs(variablesPost), post}

        }

    }

</script>