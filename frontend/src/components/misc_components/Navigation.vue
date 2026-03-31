<template>
    <nav>
        <Btn v-for="btn in props.data" :key="props.book.id" :data="btn" :book="props.book"/>
    </nav>
</template>

<script setup>

    //  Importing Components
    import Btn from './ActionButton.vue';

    const props = defineProps(['data', 'book']);
</script>