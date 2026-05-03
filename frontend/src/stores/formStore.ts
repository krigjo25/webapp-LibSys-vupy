//  TS document for Pinia Store

// Importing necessary modules
import { defineStore } from 'pinia';
import type { Book } from '@/types';

interface State {
    data: Book | null;
}

// Defining the store
export const storedData = defineStore('shareData', {
    state: (): State => ({
        data: null,
    }),
    actions: {
        setData(data: Book) {
            this.data = data;
        },
        clearData() {
            this.data = null;
        },
    },
});
