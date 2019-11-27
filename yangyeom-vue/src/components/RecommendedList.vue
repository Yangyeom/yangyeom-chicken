<template>
    <div class="container flex-nowrap justify-content-center text-center bg-dark shadow text-shadow">
        <h1>영화 목록</h1>
        <div class="row">
            <div v-for="recom in recommended" :key="recom.id" class="col-3 flex-nowrap shadow">
                <RecommendedListItem :recom="recom"/>
            </div>
        </div>
    </div>
</template>

<script>
import RecommendedListItem from '@/components/RecommendedListItem.vue'

export default {
    name: 'RecommendedList',
    data() {
        return {
            
        }
    },
    components: {
        RecommendedListItem
    },
    props: {
        recommended: {
            type: Array,
            required: true
        }
    }
}
</script>

<style>

</style>