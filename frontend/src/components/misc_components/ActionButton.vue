<template>
    <button :type="props.data.type" @click="props.data.action(book)">
        <i :class="props.data.cls"></i>
        {{ props.data.name }}
    </button>
</template>

<script setup lang="ts">
    import type { Book, ActionButtonData } from '@/types';
    
    const props = defineProps<{
        data: ActionButtonData,
        book?: Book
    }>();
</script>