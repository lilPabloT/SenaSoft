<template>
  <div style="width: 45%; height:100%; overflow:auto; display:flex; align-content:center; flex-direction:column;">
    <v-expansion-panels style="width: 80%; padding:20px" v-for="(tarea, i) in store.tareas" :key="i">
      <v-expansion-panel
        :title=tarea.titulo
        :text=" tarea.texto + ', Estado de la tarea: '  + tarea.estado ">
        <v-btn class="ma-5" @click="actualizarTarea(tarea.id)"> Actualizar tarea </v-btn>
      </v-expansion-panel>
    </v-expansion-panels>

    <v-dialog v-model="tablaActualizacionConfirmada">
      
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

            method: 'PUT',
            headers: {"content-type" : "application/json"},
            body: JSON.stringify({
              titulo: tareaSeleccionada.titulo,
              texto: tareaSeleccionada.texto,
              estado: "En ejecucion"
            })

          })

        }

        // Realizar put para actualizar de pendiente a completada

        else{

          fetch(`http://127.0.0.1:8000/api/tareas/${id}/`,{
            method: 'PUT',
            headers: {"content-type" : "application/json"},
            body: JSON.stringify({
              titulo: tareaSeleccionada.titulo,
              texto: tareaSeleccionada.texto,
              estado: "Completada"
            })

          })

          setTimeout(() => {

            fetch("http://127.0.0.1:8000/api/tareas/")
              .then(res => res.json())
              .then(data => {store.tareas = data.reverse()})

          },500)

        }  

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