<template>
  <div class="text-center">
    <img class="movie--poster my-3" :src="poster_url" :alt="movie.name" style="height:30%;width:80%"><br>
    <button @click="test" class="btn btn-dark" data-toggle="modal" :data-target="'#movie-' + movie.code">상세보기</button>
    <MovieListItemModal :movie="movie"/>
  </div>
</template>

<script>
import MovieListItemModal from '@/components/MovieListItemModal.vue'

export default {
  name: 'MovieListItem',
  components: {
      MovieListItemModal,
  },
  props:{
    movie: {
      type: Object,
      required: true,
    },
  },
  data () {
    return {
      poster_url: `http://image.tmdb.org/t/p/w500/${this.movie.poster_url}`
    }
  },
  methods: {
      test() {
          console.log(this.movie)
      }
  }
}
</script>

