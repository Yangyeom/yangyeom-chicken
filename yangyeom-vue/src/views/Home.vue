<template>
  <div class="home">
    <MovieList :movies="movies"/>
  </div>
</template>

<script>
// @ is an alias to /src
import { mapGetters } from 'vuex'
import router from '../router'
import axios from 'axios'
import MovieList from '@/components/MovieList.vue'


export default {
  name: 'home',
  components: {
    MovieList,
  },
  data() {
    return {
      movies: [],
    }
  },
  computed: {
    ...mapGetters([
      'options',
      'user'
    ])
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
    isLogined(){
      this.$session.start()
      if (!this.$session.has('jwt')){
        router.push('/login')
      } else {
        this.$store.dispatch('login', this.$session.get('jwt'))
      }
    }
  },
  mounted() {
    // this.isLogined()
    this.getMovies()
  }
}
</script>
