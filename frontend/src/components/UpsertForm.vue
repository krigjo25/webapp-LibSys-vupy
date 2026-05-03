<template>
  <h2>{{ formData.title }}</h2>
  <form class="flex-wrap-column-align-space-around" @submit.prevent>
    <Input :data="inputs" @upsert-form="handleData"/>

    <div>
      <Btn v-for="btn in formData.btn" :key="btn.id" :data="btn" @click="btn.action()"/>
    </div>
  </form>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';
import { reactive, computed } from 'vue';
import { storedData } from '../stores/formStore';
import type { Book, FormConfig, ActionButtonData } from '@/types';

//  Importing components
import Btn from './misc_components/ActionButton.vue';
import Input from './misc_components/InputField.vue';

//  Initializing reactive objects
const router = useRouter();
const buffy = reactive<Partial<Book>>({});
const buffer = storedData();
const bufferData = buffer.data;

interface FormState {
  title: string;
  btn: (ActionButtonData & { id: number })[];
}

const formData = reactive<FormState>({ 
    title: 'Insert A book',
    btn: [
      {
        id: 1,
        type: 'submit',
        cls: 'bi bi-plus',
        action: submit,
        name: 'Submit'
      },
      {
        id: 2,
        type: 'reset',
        action: resetForm,
        cls: 'bi bi-arrow-clockwise',
        name: 'Reset'
      },
    ]
});

const inputs = reactive<FormConfig>({
    title: 'Insert A book',
    bookid: bufferData ? bufferData.bookID : null,
    data: [
      {
        value: null,
        type: 'file',
        name: 'Upload an image',
      },
      {
        type: 'text',
        name: 'title',
        placeholder: computed(() => bufferData ? bufferData.title : 'E.G The Alchemist').value,
        value: null
      },
      {
        name: 'author',
        type: 'text',
        placeholder: computed(() => bufferData ? bufferData.author : 'E.G Paulo Coelho').value,
        value: null
      },
      {
        name: 'year',
        type: 'number',
        placeholder: computed(() => bufferData ? bufferData.year : new Date().getFullYear()).value,
        value: null
      },
      {
          name: 'genre',
          type: 'text',
          placeholder: computed(() => bufferData ? bufferData.genre.join(', ') : 'E.G Fiction, Non-Fiction').value,
          value: null
      },
      {
        name: 'description',
        type: 'textarea',
        placeholder: computed(() => bufferData ? bufferData.description : ' E.G A The Alchemist is a novel by Brazilian author Paulo Coelho...').value,
        value: null
      },
      {
        name: 'published_by',
        type: 'text',
        placeholder: computed(() => bufferData ? bufferData.published_by : 'E.G Harper Collins books').value,
        value: null
      },
      {
        name: 'Review',
        type: 'number',
        placeholder: computed(() => bufferData ? `${bufferData.reviews.name}, ${bufferData.reviews.rating}` : 'E.G 0.0, John Doe').value,
        value: null
      },
    ]
});

//  Handle buffer data
const handleData = (data: Partial<Book>) => {
  Object.assign(buffy, data);
}

async function submit() {
  if (buffy.title) {
    await buffer.setData(buffy as Book);
    router.push({ name: 'BookPanel' });
  }
}

function resetForm() {
  // Logic to reset buffy and inputs value
  inputs.data.forEach(field => field.value = null);
  Object.keys(buffy).forEach(key => delete (buffy as any)[key]);
}

</script>
