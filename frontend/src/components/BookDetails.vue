<template>
    <section v-if="data.data" class="flex-wrap-row-space-evenly">
      <section>
        <img :src="data.data.path" alt="book cover" />
      </section>
      <section>
        <section class="flex-column-align-items-center">
        <h2>
          {{ data.data.title }} 
          <span class="auth-tit">
            |by
            <small v-for="author in [data.data.author]" :key="author">{{ author }}</small>
          </span></h2>
        <p>
          Published {{ data.data.year }} by
            <small v-for="publisher in [data.data.published_by]" :key="publisher">{{ publisher }}</small> 
          <span v-if="data.data.reviews">Rating: {{data.data.reviews.rating}} by {{data.data.reviews.name}}</span>
        </p>
          </section>
        <section class="description flex-wrap-row-space-evenly">
          <p>{{ data.data.description }}</p>
        </section>
        <section class="genre flex-row-justify-center">
          <p v-for="genre in data.data.genre" :key="genre">{{ genre }}</p>
        </section>
      </section>
    </section>
    <section v-else>
      <h2>The data is not available at the moment</h2>
    </section>
</template>
  
<script setup lang="ts">
  //  Importing required dependencies
  import { storedData } from '../stores/formStore';
  import { onMounted, onUnmounted, reactive } from 'vue';
  import type { Book } from '@/types';
  
  //  Initializing reactive objects
  const bookStore = storedData();
  const data = reactive<{ data: Book | null }>({
    data: null,
  });

  onUnmounted(() => {
    bookStore.clearData();
  });
  onMounted(() => {
    data.data = bookStore.data;
  });
</script>
