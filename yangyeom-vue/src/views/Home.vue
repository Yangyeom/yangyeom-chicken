<template>
  <Movie class="movie"/>
</template>

<script>
// @ is an alias to /src
import Movie from '@/components/Movie.vue'

export default {
  name: 'home',
  components: {
    Movie
  },
  data() {
    return {}
  }
}
</script>
