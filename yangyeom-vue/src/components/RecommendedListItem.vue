<template>
  <div class="my-3">
    <img class="movie--poster my-3" :src="poster_url" :alt="recom.movie.name" style="height:100%;width:100%">
    <h3>{{ recom.movie.name }}</h3>
    <button @click="test" class="btn btn-primary" data-toggle="modal" :data-target="'#movie-' + recom.movie.code">예상: {{ recom.score }}점/5.0점</button>
  </div>
</template>

<script>

export default {
  name: 'RecommendedListItem',
  props:{
    recom: {
      type: Object,
      required: true,
    }
  },
  computed: {
    poster_url() {
      return `http://image.tmdb.org/t/p/w500/${this.recom.movie.poster_url}`
    }
  },
    methods: {
        test() {
            console.log(this.movie)
        },
  }
}
</script>

