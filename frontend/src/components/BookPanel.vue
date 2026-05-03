<template>

  <nav class="flex-wrap-row-space-evently">
    <Btn :data="{
          type: 'submit',
          name: 'Create book',
          cls: 'bi bi-plus',
          action: () => upsertEvent()
        }" :book="{} as Book"/>
  </nav>
  <section class="flex-wrap-row-space-evenly">
    <Books :nav="buttons.nav" :data="buttons.data"/>
  </section>
</template>

<script setup lang="ts">

  //  Importing required dependencies
  import { useRouter } from 'vue-router';
  import { onMounted, reactive} from 'vue';
  import { storedData } from '../stores/formStore';
  import { removeBook, updateBook, createBook } from '../assets/js/bookCrud';
  import type { Book, NavigationData } from '@/types';
  
  //  Importing components
  import Books from './Books.vue';
  import Btn from './misc_components/ActionButton.vue';
  
  //  Initializing reactive objects
  const router = useRouter();
  const buffy = storedData();

  interface ButtonState {
    nav: boolean;
    data: NavigationData;
  }

  const buttons = reactive<ButtonState>(
    { 
      nav : true,
      data:
      [
        {
          type: 'button',
          cls: 'bi bi-arrow-clockwise',
          action: upsertEvent,
          name: 'Update'
        },
        {
          type: 'button',
          cls: 'bi bi-trash',
          action: removeBook,
          name: 'Delete'
        }
    ]});

  //  Router push
  function upsertEvent(book: Book | null = null)
  {
    if (book) {
        buffy.setData(book);
    } else {
        buffy.clearData();
    }
    router.push({name: 'UpsertBook'});
  }

  //  Create or Update a book
  async function upsertBook(data: Book) 
  {
    //  Ensure the data's integrity
    data.bookID ? await updateBook(data) : await createBook(data);
  };

onMounted(() => {
  if (buffy.data)
  {
    upsertBook(buffy.data);
  }
});

</script>
