<template>
  <div class="rating">
    <h1>열 개의 영화를 평가해주세요!</h1>
    <MovieRatingList :movies="movies"/>
  </div>
</template>

<script>
import MovieRatingList from '@/components/MovieRatingList.vue'
import axios from 'axios'

export default {
    name: 'home',
    components: {
        MovieRatingList,
    },
    data() {
        return {
            movies: [],
        }
    },
    methods: {
        getMovies(){
            axios.get('http://127.0.0.1:8000/api/v1/movies/rating/')
                .then(response => {
                    console.log(response)
                    this.movies = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        }
    },
    mounted() {
        this.getMovies()
    }
}
</script>

<style>

</style>