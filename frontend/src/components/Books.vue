<template>
        <section  v-for="book in data.books" :key="book.id">
            <div @click="bookInfo(book.id)">
                <img :src="book.path" alt="book cover.jpg" />
                <div>
                    <h3>{{ book.title }}
                        <span class="auth-tit">
                            |by
                            <small v-for="author in book.author">{{ author }}</small>
                        </span>
                    </h3>
                    <p>
                        <span v-if="book.reviews">Rating: {{book.reviews.rating}} by {{book.reviews.name}}</span>
                    </p>
                </div>
            </div>
            <div v-if="props.nav">
                <Navigation :data="props.data" :book="book" />
            </div>
        </section>
</template>

<script setup>
    //  Importing required dependencies
    import { useRouter } from 'vue-router';
    import { defineEmits, onMounted } from 'vue';
    
    import { storedData } from '../stores/formStore.js';
    import { Response, data } from '../assets/js/apiService.js';
    

    //  Importing components
    import Navigation from './misc_components/Navigation.vue';

    const router = useRouter();
    const shareData = storedData();
    const emit = defineEmits(['book-id']);

    const props = defineProps(
        {
            data:
            {
                type: Object,
                required: true
            },
            nav:
            {
                type: Boolean,
                required: false
            }
        }
    );

    //  Function to get the book's information
    function bookInfo(id)
    {
        //  Ensure that the data is not empty
        if (data.books) 
        {

        const book =  data.books.find(book => book.id === id)
        
            shareData.setData(book);
            
             router.push({name: 'BookDetails'});
        }
    };

    // Initialize the data
    onMounted(Response);

</script>