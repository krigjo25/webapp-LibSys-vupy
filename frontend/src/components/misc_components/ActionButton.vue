<template>
    <button :type="props.data.type" @click="props.data.action(book)">
        <i :class="props.data.cls"></i>
        {{ props.data.name }}
    </button>
</template>

<script setup>

    //  Importing Components
    
    const props = defineProps(['data', 'book']);
</script>