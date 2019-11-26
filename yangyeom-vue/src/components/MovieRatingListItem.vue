<template>
  <div class="my-3">
    <img class="movie--poster my-3" :src="poster_url" :alt="movie.name" style="height:100%;width:100%">
    <h3>{{ movie.name }}</h3>
    <form @submit.prevent="">
        <star-rating v-model="score_rating" :glow="5" :show-rating="true" :star-size="30" :increment="0.5" :border-width="1" border-color="#d8d8d8" :rounded-corners="true" :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]"/>
        <button class="btn btn-danger" type="submit">콕</button>
    </form>
  </div>
</template>

<script>
// 1-1. 저장되어 있는 MovieListItemModal 컴포넌트를 불러오고,
// import MovieListItemModal from './MovieListItemModal.vue'
import StarRating from 'vue-star-rating'
import axios from 'axios'

export default {
  name: 'MovieRatingListItem',
  // 1-2. 아래에 등록 후
  components: {
      StarRating
  },
  props:{
    movie: {
      type: Object,
      required: true,
    }
  },
  data () {
    return {
      poster_url: `http://image.tmdb.org/t/p/w500/${this.movie.poster_url}`,
      content_rating: '',
      score_rating: 0,
    }
  },
  methods: {
    save() {
      const data = {
        score: this.score_rating,
        user: this.user,
        movie: this.movie.code
      }
      axios.post(`http://127.0.0.1:8000/api/v1/movie/${this.movie.code}/reviews/`, data, this.options)
        .then(response => {
          console.log(response)
          const review = {
            content: response.data.content,
            score: response.data.score,
            username: response.data.username,
          }
          this.reviews.push(review)
          console.log('리뷰들', this.reviews)
        })
        .catch(error => {
          console.log(error)
        })
    },
  }
}
</script>

