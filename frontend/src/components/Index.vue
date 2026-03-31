<template>
  <section class="flex-wrap-row-space-evenly">
    <BookTable :data="data"/>
  </section>
</template>

<script setup>

  //  Importing Components
  import BookTable from './Books.vue';


  //  Importing required dependencies
  import { reactive } from 'vue';

  //  Initializing reactive objects
  const Book = reactive
  (
      {
        id    :null,
        title :null,
        author:null,
      }
  );

  const data = reactive(  
    {
      title: null,
      author: null,
  });
</script>