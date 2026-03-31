//  JS document for Pinia Store

// Importing necessary modules
import { reactive } from 'vue';
import { defineStore } from 'pinia';

// Defining the store
export const storedData = defineStore('shareData', {
    state: () => ({
        data: reactive({}),
    }),
    actions: {
        setData(data) {
            this.data = data;
        },
        clearData() {
            this.data = null;
        },
    },
});