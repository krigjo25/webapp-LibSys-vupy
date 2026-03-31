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
            <small v-for="author in data.data.author">{{ author }}</small>
          </span></h2>
        <p>
          Published {{ data.data.year }} by
            <small v-for="publisher in data.data.publisher">{{ publisher }}</small> 
          <span v-if="data.data.reviews">Rating: {{data.data.reviews.rating}} by {{data.data.reviews.name}}</span>
        </p>
          </section>
        <section class="description flex-wrap-row-space-evenly">
          <p>{{ data.data.description }}</p>
        </section>
        <section class="genre flex-row-justify-center">
          <p v-if="data.data.genre != null && data.data.genre.length > 1" v-for="genre in data.data.genre">{{ genre }}</p>
            <p v-else v-for="genre in data.data.genre">{{ genre }}</p>
        </section>
      </section>
    </section>
    <section v-else>
      <h2>The data is not available at the moment</h2>
    </section>
</template>
  
<script setup>

  
  //  Importing required dependencies
  import { storedData } from '../stores/formStore.js';
  import { onMounted, onUnmounted, reactive } from 'vue';
  
  //  Initializing reactive objects
  const book = storedData();
  const data = reactive({
    data: null,
  });

  onUnmounted(() => {
    book.clearData(null);
  });
  onMounted(() => {
    data.data = book.data;
  });
</script>