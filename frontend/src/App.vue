<template>
  <HeaderView />
  <main>
    <RouterView />
  </main>
</template>

<script setup lang="ts">
import { RouterView } from 'vue-router'
import HeaderView from './components/header_components/AppHeader.vue'
</script>
