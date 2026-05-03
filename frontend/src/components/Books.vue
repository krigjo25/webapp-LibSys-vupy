<template>
        <section v-for="book in data.books" :key="book.bookID">
            <div @click="book.bookID && bookInfo(book.bookID)">
                <img :src="book.path" alt="book cover.jpg" />
                <div>
                    <h3>{{ book.title }}
                        <span class="auth-tit">
                            |by
                            <small v-for="author in [book.author]" :key="author">{{ author }}</small>
                        </span>
                    </h3>
                    <p>
                        <span v-if="book.reviews">Rating: {{book.reviews.rating}} by {{book.reviews.name}}</span>
                    </p>
                </div>
            </div>
            <div v-if="props.nav && props.data">
                <Navigation :data="props.data" :book="book" />
            </div>
        </section>
</template>

<script setup lang="ts">
    //  Importing required dependencies
    import { useRouter } from 'vue-router';
    import { onMounted } from 'vue';
    
    import { storedData } from '../stores/formStore';
    import { Response, data } from '../assets/js/apiService';
    import type { Book, NavigationData } from '@/types';

    //  Importing components
    import Navigation from './misc_components/Navigation.vue';

    const router = useRouter();
    const shareData = storedData();

    const props = defineProps<{
        data?: NavigationData,
        nav?: boolean
    }>();

    //  Function to get the book's information
    function bookInfo(id: string)
    {
        //  Ensure that the data is not empty
        if (data.books) 
        {
            const book = data.books.find(book => book.bookID === id)
            if (book) {
                shareData.setData(book);
                router.push({name: 'BookDetails'});
            }
        }
    };

    // Initialize the data
    onMounted(Response);

</script>
