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
        <div v-for="review in reviews" :key="review.id">
            <h6>{{review.score}}</h6>
            <h6>{{review.username}}</h6>
            <h6>{{review.content}}</h6>
            <hr>
        </div>
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

export default {
  name: 'movie-list-item-modal',
  // 0. props 데이터를 받이 위하여 설정하시오.
  // movie 타입은 Object이며, 필수입니다.
  // 설정이 완료 되었다면, 상위 컴포넌트에서 값을 넘겨 주세요.
  // 그리고 적절한 곳에 사용하세요.
  props: {
    movie: {
      type: Object,
      required: true,
    }
  },
  data() {
      return {
          poster_url: `http://image.tmdb.org/t/p/w500/${this.movie.poster_url}`,
          reviews: [],
      }
  },
  computed: {
    ...mapGetters([
      'options',
      'user'
    ])
  },
  mounted(){
      axios.get(`http://127.0.0.1:8000/api/v1/movies/${this.movie.code}/`, this.options)
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
