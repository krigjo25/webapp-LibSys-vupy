//  Fetching the books from the server

//  Importing dependencies
import axios from 'axios';
import { reactive } from 'vue';

//  Initializing the data
export const data = reactive({books: null,});

//  Fetch the books from the server
export const Response = async () =>
    {
        //  Initialize the path
        const path = 'http://localhost:5000/';
        axios.get(path).then((res) => {

                //  Assign the response data to the data object
                data.books = res.data.books;

        }).catch((error) => {
            console.error(error);
        });
    };