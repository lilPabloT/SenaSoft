<template>
  <div style="width: 45%; height:100%; overflow:auto; display:flex; align-content:center; flex-direction:column;">
    <v-expansion-panels style="width: 80%; padding:20px" v-for="(tarea, i) in store.tareas" :key="i">
      <v-expansion-panel
        :title="tarea.titulo.toUpperCase()"
        :text=" 'RESUMEN: ' + tarea.texto"
        style="pa-5">
        <p class="ml-5 my-3"> Estado de la tarea: {{ tarea.estado }} </p>
        <v-btn v-if="tarea.estado != 'Completada'" class="ma-5 bg-green" @click="actualizarTarea(tarea.id)"> Actualizar tarea </v-btn>
      </v-expansion-panel>
    </v-expansion-panels>

    <v-dialog v-model="tablaActualizacionConfirmada">
        <v-alert style="margin: auto; width: max-content" class="pa-5" type="success">
          <v-alert-title> ¡Actualizado! </v-alert-title>
          El registro se ha actualizado correctamente
          <br>
          <br>
          <v-btn class="text-black" @click="tablaActualizacionConfirmada = false"> Cerrar </v-btn>
        </v-alert>
    </v-dialog>
  </div>


  
</template>

<script>

  import { onMounted, ref } from 'vue';
  import { useAppStore } from '@/store/app';

  export default{

    setup(){

      // Variable que contendra la tarea a actualizar

      let tareaSeleccionada = ref()

      let tablaActualizacionConfirmada = ref(false)

      // Traer los datos de la store

      const store = useAppStore()

      // Funcion para cambiar las tareas 

      function actualizarTarea(id){

        // Conseguir la tarea especifica para actualizar

        for (let i of store.tareas){

          if(i.id == id){

            tareaSeleccionada = i

          }

        }

        // Realizar put para actualizar de pendiente a en ejecucion

        if (tareaSeleccionada.estado == "Pendiente"){

          fetch(`http://127.0.0.1:8000/api/tareas/${id}/`, {
              method: "PUT",
              headers: {"content-type" : "application/json"},
              body: JSON.stringify({
                  "titulo" : tareaSeleccionada.titulo,
                  "texto" : tareaSeleccionada.texto,
                  "estado" : 'En ejecucion'
              })
          })

        }else{

          fetch(`http://127.0.0.1:8000/api/tareas/${id}/`,{
            method: 'PUT',
            headers: {"content-type" : "application/json"},
            body: JSON.stringify({
              "id" : tareaSeleccionada.id,
              "titulo" : tareaSeleccionada.titulo,
              "texto" : tareaSeleccionada.texto,
              "estado" : "Completada"
            })

          })

          // Volver a pintar la pagina despues del put

        }  

        setTimeout(() => {

          fetch("http://127.0.0.1:8000/api/tareas/")
            .then(res => res.json())
            .then(data => {store.tareas = data.reverse()})

        },500)

        tablaActualizacionConfirmada.value = true

      }

      // Funcion al montar la aplicacion trae la data

      onMounted(() => {

        fetch("http://127.0.0.1:8000/api/tareas/")
          .then(res => res.json())
          .then(data => {store.tareas = data.reverse()})

      })

      return {store, actualizarTarea, tablaActualizacionConfirmada}

    }

  }

</script>