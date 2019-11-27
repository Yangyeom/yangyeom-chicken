<template>
  <div class="my-3">
    <img class="movie--poster my-3" :src="poster_url" :alt="movie.name" style="height:100%;width:100%">
    <h3>{{ movie.name }}</h3>
    <button @click="test" class="btn btn-primary" data-toggle="modal" :data-target="'#movie-' + movie.code">영화 정보 상세보기</button>
    <MovieListItemModal :movie="movie"/>
  </div>
</template>

<script>
import MovieListItemModal from '@/components/MovieListItemModal.vue'

export default {
  name: 'MovieListItem',
  components: {
      MovieListItemModal
  },
  props:{
    movie: {
      type: Object,
      required: true,
    }
  },
  computed: {
    poster_url() {
      return `http://image.tmdb.org/t/p/w500/${this.movie.poster_url}`
    }
  },
  methods: {
      test() {
          console.log(this.movie)
      }
  }
}
</script>

