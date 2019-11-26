<template>
    <div class="container flex-nowrap justify-content-center text-center bg-dark shadow text-shadow">
        <h1>영화 목록</h1>
        <div class="row">
            <div v-for="movie in movies" :key="movie.code" class="col-2 flex-nowrap shadow">
                <MovieRatingListItem :movie_id="movie.code" @cntUp="cntUp" :movie="movie"/>
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
    },
    methods: {
        cntUp() {
            console.log("list")
            this.$emit('cntUp')
        }
    }
}
</script>

<style>

</style>