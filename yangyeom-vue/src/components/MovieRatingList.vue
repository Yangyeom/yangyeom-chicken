<template>
    <div class="container flex-nowrap justify-content-center text-center bg-dark shadow text-shadow">
        <h1>영화 목록</h1>
        <div class="row">
            <div v-for="movie in movies" :key="movie.id" class="col-2 flex-nowrap shadow">
                <MovieRatingListItem :movie="movie"/>
            </div>
        </div>
    </div>
</template>

<script>
import MovieRatingListItem from '@/components/MovieRatingListItem.vue'

export default {
    name: 'MovieRatingList',
    data() {
        return {
            
        }
    },
    components: {
        MovieRatingListItem
    },
    props: {
        movies: {
            type: Array,
            required: true
        }
    }
}
</script>

<style>

</style>