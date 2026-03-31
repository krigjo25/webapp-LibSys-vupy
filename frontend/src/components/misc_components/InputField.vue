
<template>
    <legend>{{ props.data.title }}</legend>
    <div v-for="dt in data" class="flex-wrap-row-align-center-justify-space-between">
        
        <label :for="dt.name">{{ dt.name}} :</label>
        
        <input v-if="dt.type != 'textarea'" :type="dt.type" :id="dt.id" :name="dt.name" :placeholder="dt.placeholder" v-model="dt.value"/>
        <textarea v-if="dt.type == 'textarea'" :type="dt.type" :id="dt.id" :name="dt.name" :placeholder="dt.placeholder" v-model="dt.value" maxlength="255"></textarea>
    </div>
</template>

<script setup>

    //  Importing required dependencies
    import {reactive, watch, defineEmits } from 'vue';

    //  Initializing reactive objects
    const props = defineProps(
    {
        data:{
            type: Object,
            required: true,
        }
    });

    const buffer = reactive({});
    const data = props.data.data;
    const emit = defineEmits(['upsert-form']);


    //  Watch for changes in the data
    watch(data, (n, o) => {

        //  Initialize variables
        const file = 'Upload an image';
        const array = ['.jpg', '.png', '.jpeg', '.gif'];

        //  Ensure that the book id is pushed to the buffer
        buffer["id"] = props.data.bookid;

        //  Loop through the new data
        for (let i = 0; i < n.length; i++) 
        {
            
            if (n[i].name == file)
            {
                //  Ensure that the file includes an acceptable image
                for (let j = 0; j < array.length; j++) 
                {
                    const element = n[i].value || 'null';
                    
                    //  Ensure that the file includes an acceptable image
                    if (element.endsWith(array[j])) 
                    {
                        buffer['image'] = n[i].value;
                        break;
                    }
                    buffer['image'] = null;
                }
            }
            buffer[n[i].name] = n[i].value;
        }

    emit('upsert-form', buffer);
    console.log("collected data :",buffer);
    });
</script>