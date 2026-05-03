//  Fetching the books from the server

//  Importing dependencies
import axios, { type AxiosResponse } from 'axios';
import { reactive } from 'vue';
import type { Book } from '@/types';

interface ApiResponse {
    books: Book[];
    status: number;
    message: string;
}

interface State {
    books: Book[] | null;
}

//  Initializing the data
export const data = reactive<State>({books: null,});

//  Fetch the books from the server
export const Response = async (): Promise<void> =>
    {
        //  Initialize the path
        const path = 'http://localhost:5000/';
        axios.get<ApiResponse>(path).then((res: AxiosResponse<ApiResponse>) => {

                //  Assign the response data to the data object
                data.books = res.data.books;

        }).catch((error: any) => {
            console.error(error);
        });
    };
