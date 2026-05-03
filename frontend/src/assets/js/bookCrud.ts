//  Initializing CRUD operations for the book

// Importing the axios module
import axios from 'axios';
import { Response } from './apiService';
import type { Book } from '@/types';

// Create a bok and send a Post Request
export async function createBook(payload: Book): Promise<void>
{
    // Initialize the path
    const path = 'http://localhost:5000/';

    // Send a post request to the server
    await axios.post(path, payload).then(() => 
        {
            Response();

        }).catch((error: any) => {
            console.error(error);
        });
};
// Delete a book and send a delete request
export async function removeBook(book: Book): Promise<void>
{
    if (!book.bookID) return;
    
    // Initialize the path
    const path = `http://localhost:5000/${book.bookID}`;
    
    // Send a delete request to the server
    await axios.delete(path).then(() => 
        {
            Response();

        }).catch((error: any) => {
            console.error(error);
        });
};

// Update a book and send Put Request
export async function updateBook(payload: Book): Promise<void>
{
    if (!payload.bookID) return;

    //  Initialize the path
    const path = `http://localhost:5000/${payload.bookID}`;
    // Send a post request to the server
    await axios.put(path, payload).then(() => 
        {
            Response();
            console.log('Book updated successfully', payload);
        }).catch((error: any) => {
        console.error(error);
        });
};
