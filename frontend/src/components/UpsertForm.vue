<template>
  <h2>{{ data.title }}</h2>
  <form class="flex-wrap-column-align-space-around">
    <Input :data="inputs" @upsert-form="handleData"/>

    <div>
      <Btn v-for="btn in data.btn" :data="btn" @click="btn.action()"/>
    </div>
  </form>
</template>

<script setup>

import { useRouter } from 'vue-router';
import { reactive, computed } from 'vue';
import { storedData } from '../stores/formStore.js';

//  Importing components
import Btn from './misc_components/ActionButton.vue';
import Input from './misc_components/InputField.vue';

//  Initializing reactive objects
const router = useRouter();
const buffy = reactive({});
const buffer = storedData();
const bufferData = buffer.data;

const data = reactive(
  { 
    btn:
    [
      {
        id: 1,
        type: 'submit',
        cls: 'bi bi-plus',
        action: submit
      },
      {
        id: 2,
        type: 'reset',
        action:resetForm,
        cls: 'bi bi-arrow-clockwise',
      },
    ]
});
const inputs = reactive(
  {
    title: computed( () => {return 'Insert A book'}),
    bookid: computed( () => {return bufferData ? bufferData.id : null}),
    data: 
    [
      {
        value: null,
        type: 'file',
        name: 'Upload an image',
      },
      {
        
        type: 'text',
        name: 'title',
        placeholder: computed( () => {return bufferData ? bufferData.title : 'E.G The Alchemist'}),
        value: null
      },
      {
        name: 'author',
        type: 'text',
        placeholder: computed( () => {return bufferData? bufferData.author : 'E.G Paulo Coelho'}),
        value: null
      },
      {
        name: 'year',
        type: 'number',
        placeholder: computed( () => {return bufferData ? bufferData.year : new Date().getFullYear()}),
        value: null
      },
      {
          name: 'genre',
          type: 'text',
          placeholder: computed( () => {return bufferData ? bufferData.genre : 'E.G Fiction, Non-Fiction'}),
          value: null
      },
      {
        name: 'description',
        type: 'textarea',
        placeholder: computed( () => {return  bufferData ? bufferData.description : ' E.G A The Alchemist is a novel by Brazilian author Paulo Coelho that was first published in 1988. Originally written in Portuguese, it became an international bestseller translated into some 70 languages as of 2016. An allegorical novel, The Alchemist follows a young Andalusian shepherd in his journey to the pyramids of Egypt, after having a recurring dream of finding a treasure there. '}),
        value: null
      },
      {
        name: 'published_by',
        type: 'text',
        placeholder: computed( () => {return bufferData ? bufferData.reviews.name : 'E.G Harper Collins books'}),
        value: null
      },
      {
        name: 'Rewiew',
        type: 'number',
        placeholder: computed( () => {return bufferData ? bufferData.reviews.name + ", " + bufferData.reviews.rating : 'E.G 0.0, John Doe'}),
        value: null
      },
    ]
});

//  Handle  buffer data
const handleData = (data) =>
{
  Object.assign(buffy, data);
}

async function submit()
{
  await buffer.setData(buffy);
  
  //ResetForm();
  router.push({name: 'BookPanel'});
  
}

function resetForm()
{
  buffy.title = ''
  buffy.genre = ''
  buffy.author = ''
  buffy.published = ''
  buffy.description = ''
  buffy.published_by = ''
}

</script>
