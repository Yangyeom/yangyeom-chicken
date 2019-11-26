<template>
<!-- vue 콘솔에서 확인하여, 추가 정보들도 출력하세요. -->
<!-- 고유한 모달을 위해 id 속성을 정의하시오. 예) movie-1, movie-2, ... -->
<div class="modal fade bd-example-modal-lg" tabindex="-1" role="dialog" :id="'movie-' + movie.code">
  <div class="modal-dialog modal-xl" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <!-- 영화 제목을 출력하세요. -->
        <h5 class="modal-title">{{ movie.title }}</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <img :src="poster_url" :alt="movie.title" width="200px">
      </div>
      <div class="modal-body">
        <hr>
        <p>{{ movie.description }}</p>
      </div>
      <div class="modal-body">
        <hr>
        <!-- <h6>{{review.username}}</h6> -->
            <!-- <h6>{{review.score}}</h6>
            <h6>{{review.content}}</h6>
            <button @click="review_delete(review.id)">삭제</button>
            <hr> -->
        <div v-for="review in reviews"  :key="review.id">
            <h6>{{review.username}}</h6>
            <h6>{{review.score}}</h6>
            <h6>{{review.content}}</h6>
            <button v-if="writerCheck(review.user)" @click="reviewDelete(review.id)">삭제</button>
            <hr>
        </div>
        <form @submit.prevent="">
          <star-rating v-model="score_rating" :glow="10" :show-rating="true" :increment="0.5" :border-width="1" border-color="#d8d8d8" :rounded-corners="true" :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]"/>
          <input type="text" v-model="content_rating" @change="save">
          <button type="submit">확인</button>
        </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import { mapGetters } from 'vuex'
import StarRating from 'vue-star-rating'

export default {
  name: 'movie-list-item-modal',
  computed: {
    ...mapGetters([
      'options',
      'user'
    ])
  },
  props: {
    movie: {
      type: Object,
      required: true,
    }
  },
  components: {
    StarRating
  },
  data() {
      return {
          poster_url: `http://image.tmdb.org/t/p/w500/${this.movie.poster_url}`,
          reviews: [],
          content_rating: '',
          score_rating: 0,
      }
  },
  methods: {
    save() {
      const data = {
        content: this.content_rating,
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
    reviewDelete(review_id) {
      axios.delete(`http://127.0.0.1:8000/api/v1/movie/${this.movie.code}/reviews/${review_id}/`, this.user, this.options)
        .then(response => {
            console.log(response)
            this.reviews = this.reviews.filter(review => review.id !== review_id)
        })
        .catch(error => {
            console.log(error)
        })
    },
    writerCheck(writer) {
      return writer === this.user
    }
  },
  mounted(){
      axios.get(`http://127.0.0.1:8000/api/v1/movie/${this.movie.code}/reviews/`, this.options)
        .then(response => {
            this.reviews = response.data
        })
        .catch(error => {
            console.log(error)
        })
  }
}
</script>

<style>

</style>
