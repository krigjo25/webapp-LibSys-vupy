
<template>
    <legend>{{ props.data.title }}</legend>
    <div v-for="dt in props.data.data" :key="dt.name" class="flex-wrap-row-align-center-justify-space-between">
        
        <label :for="dt.name">{{ dt.name}} :</label>
        
        <input v-if="dt.type != 'textarea'" :type="dt.type" :id="dt.name" :name="dt.name" :placeholder="dt.placeholder?.toString()" v-model="dt.value"/>
        <textarea v-if="dt.type == 'textarea'" :id="dt.name" :name="dt.name" :placeholder="dt.placeholder?.toString()" v-model="dt.value" maxlength="255"></textarea>
    </div>
</template>

<script setup lang="ts">
    //  Importing required dependencies
    import { reactive, watch } from 'vue';
    import type { FormConfig } from '@/types';

    //  Initializing reactive objects
    const props = defineProps<{
        data: FormConfig
    }>();

    const buffer = reactive<Record<string, any>>({});
    const emit = defineEmits(['upsert-form']);

    //  Watch for changes in the data
    watch(() => props.data.data, (n) => {
        //  Initialize variables
        const file = 'Upload an image';
        const array = ['.jpg', '.png', '.jpeg', '.gif'];

        //  Ensure that the book id is pushed to the buffer
        buffer["bookID"] = props.data.bookid;

        //  Loop through the new data
        for (let i = 0; i < n.length; i++) 
        {
            if (n[i].name == file)
            {
                //  Ensure that the file includes an acceptable image
                let imgFound = false;
                for (let j = 0; j < array.length; j++) 
                {
                    const element = (n[i].value as string) || 'null';
                    
                    //  Ensure that the file includes an acceptable image
                    if (element.endsWith(array[j])) 
                    {
                        buffer['path'] = n[i].value;
                        imgFound = true;
                        break;
                    }
                }
                if (!imgFound) buffer['path'] = null;
            }
            buffer[n[i].name] = n[i].value;
        }

        emit('upsert-form', buffer);
        console.log("collected data :", buffer);
    }, { deep: true });
</script>
