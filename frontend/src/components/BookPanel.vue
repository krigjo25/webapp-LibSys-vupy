#  The first Vue project
<template>

  <nav class="flex-wrap-row-space-evently">
    <Btn :data="{
          type: 'submit',
          name: 'Create book',
          cls: 'bi bi-plus',
          action: upsertEvent
        }"/>
  </nav>
  <section class="flex-wrap-row-space-evenly">
    <Books :nav="buttons.nav" :data="buttons.data"/>
  </section>
</template>

<script setup>

  //  Importing required dependencies
  import { useRouter } from 'vue-router';
  import { onMounted, reactive} from 'vue';
  import { storedData } from '../stores/formStore.js';
  import { removeBook, updateBook, createBook } from '../assets/js/bookCrud.js';
  
  //  Importing components
  import Books from './Books.vue';
  import Btn from './misc_components/ActionButton.vue';
  
  //  Initializing reactive objects
  const router = useRouter();
  const buffy = storedData();

  const buttons = reactive(
    { 
      nav : true,
      data:
      [
        {
          id: 2,
          type: 'button',
          cls: 'bi bi-arrow-clockwise',
          action:upsertEvent
        },
        {
          id: 3,
          type: 'button',
          cls: 'bi bi-trash',
          action:removeBook,
        }
    ]});

  //  Router push
  function upsertEvent(book = null)
  {

    buffy.setData(book);
    router.push({name: 'UpsertBook'});
  }

  //  Create or Update a book
  async function upsertBook(data) 
      {
        //  Ensure the data's integerty
        data.id ? updateBook(data) : createBook(data);
  };

onMounted(() => {
  if (buffy.data)
  {
    upsertBook(buffy.data);
  }
});

</script>