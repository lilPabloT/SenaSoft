<template>
  <v-app>
    <div style="background: #0af">
      <h1 class="text-center text-h1 my-15 text-white"> To do list </h1>
      <v-main style="display: flex; justify-content:space-evenly; width:100%; height:95vh">
        <HelloWorld />
        <Post />
      </v-main>
    </div>
  </v-app>
</template>

<script setup>
  import HelloWorld from '@/components/HelloWorld.vue'
  import Post from '@/components/Post.vue'
</script>
