<template>
  <div class="my-3">
    <img class="movie--poster my-3" :src="poster_url" :alt="movie.name" style="height:100%;width:100%">
    <h3>{{ movie.name }}</h3>
    <button @click="test" class="btn btn-primary" data-toggle="modal" :data-target="'#movie-' + movie.code">영화 정보 상세보기</button>
  </div>
</template>

<script>
// 1-1. 저장되어 있는 MovieListItemModal 컴포넌트를 불러오고,
// import MovieListItemModal from './MovieListItemModal.vue'

export default {
  name: 'MovieListItem',
  // 1-2. 아래에 등록 후
  components: {
      
  },
  props:{
    movie: {
      type: Object,
      required: true,
    }
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

