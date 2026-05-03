<template>
    <nav>
        <Btn v-for="btn in props.data" :key="btn.name" :data="btn" :book="props.book"/>
    </nav>
</template>

<script setup lang="ts">

    //  Importing Components
    import Btn from './ActionButton.vue';
    import type { Book, NavigationData } from '@/types';

    const props = defineProps<{
        data: NavigationData,
        book: Book
    }>();
</script>
