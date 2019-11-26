<template>
  <div class="rating">
    <h1>{{counter}}개의 영화를 평가해주세요!</h1>
    <MovieRatingList @cntUp="cntUp" :movies="movies"/>
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
            counter: 10,
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
        },
        cntUp(){
            this.counter = this.counter - 1
        }
    },
    mounted() {
        this.getMovies()
    },
      watch: {
        // 질문이 변경될 때 마다 이 기능이 실행됩니다.
        counter: function () {
            if(this.counter === 0){
                window.location.href = '/';
            }
    }
  },
}
</script>

<style>

</style>