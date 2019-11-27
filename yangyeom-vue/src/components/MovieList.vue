<template>
    <div class="container flex-nowrap justify-content-center text-center bg-dark shadow text-shadow">
        <h1>영화 목록</h1>
        <div class="row">
            <div v-for="movie in movies" :key="movie.id" class="col-3 flex-nowrap shadow">
                <MovieListItem :movie="movie"/>
            </div>
        </div>
    </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem.vue'

export default {
    name: 'MovieList',
    data() {
        return {
            
        }
    },
    components: {
        MovieListItem,
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