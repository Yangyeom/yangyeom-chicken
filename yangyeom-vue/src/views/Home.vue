<template>
  <div class="home">
      <Cover/>
      <!-- <button @click="getRecommendation">테스트</button> -->
      <RecommendedList v-if="done" :recommended="recommended"/>
      <div style="height: 100px"></div>
      <MovieList :movies="movies"/>
      <MovieListItemModal v-for="movie in movies" :movie_="movie" :key="movie.code" />
      <Footer/>
  </div>
</template>

<script>
// @ is an alias to /src
import { mapGetters } from 'vuex'
// import router from '../router'
import axios from 'axios'
import MovieList from '@/components/MovieList.vue'
import MovieListItemModal from '@/components/MovieListItemModal.vue'
import Cover from '@/components/Cover.vue'
import Footer from '@/components/Footer.vue'
import RecommendedList from '@/components/RecommendedList.vue'


export default {
  name: 'home',
  components: {
    MovieList,
    Cover,
    Footer,
    RecommendedList,
    MovieListItemModal
  },
  data() {
    return {
      movies: [],
      recommended: [],
      done: false
    }
  },
  computed: {
    ...mapGetters([
      'options',
      'user'
    ]),
  },
  created() {
    this.$EventBus.$on('click-icon', () => {
      this.getRecommendation()
    })
  },
  methods: {
    getMovies(){
      axios.get('http://127.0.0.1:8000/api/v1/movies/')
        .then(response => {
          console.log(response)
          this.movies = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    getRecommendation() {
      axios.get(`http://127.0.0.1:8000/accounts/${this.user}/`, this.options)
        .then(response => {
          console.log('결제했는지', response.data.paid)
          if (response.data.paid) {
             const conf = this.options
              conf.user = this.user
             axios.get('http://127.0.0.1:8000/api/v1/recommend', conf)
              .then(response => {
                console.log(response)
                // this.recommended = JSON.parse(response.data)
                this.recommended = response.data
                console.log('추천받은 영화:', this.recommended)
                this.done = true
              })
          }
        })
      // const conf = this.options
      // conf.user = this.user
      
      // axios.get('http://127.0.0.1:8000/api/v1/recommend', conf)
      //   .then(response => {
      //     console.log(response)
      //     // this.recommended = JSON.parse(response.data)
      //     this.recommended = response.data
      //     console.log('추천받은 영화:', this.recommended)
      //   })
      //   .catch(error => {
      //     console.log(error)
      //   })
    },
    isLogined(){
      this.$session.start()
      if (this.$session.has('jwt')){
        this.$store.dispatch('login', this.$session.get('jwt'))
      }
    },
    // test() {
    //   const config = this.options
    //   config.user = this.user
    //   axios.get('http://127.0.0.1:8000/api/v1/test/', config)
    //     .then(response => {
    //       console.log(response)
    //     })
    //     .catch(error => {
    //       console.log(error)
    //     })
    // }
  },
  mounted() {
    this.isLogined()
    this.getMovies()
    this.done = false
  },
  watch: {
    recommend: {
      handler: function() {
        console.log(this.recommend)
        // if (this.recommend) {
        //   this.getMovies()
        // }
      }
    }
  }
}
</script>
