<template>
    <!-- <carousel-3d :space="350" :border="10" :height="600" :width="300" :display="7">
        <div v-for="(movie, index) in movies" :key="movie.id">
            <slide :index="index">
                <MovieListItem :movie="movie"/>
            </slide >
        </div>
    </carousel-3d> -->
    <div style="height:800px" class="row">

    <swiper :options="swiperOption" ref="mySwiper">
    <!-- slides -->
        <!-- <div v-for="movie in movies" :key="movie.id"> -->
            
        <swiper-slide v-for="movie in movies" :key="movie.id">
            <MovieListItem :movie="movie"/>
        </swiper-slide>
        <!-- </div> -->
    <!-- Optional controls -->
    </swiper>
    </div>
</template>

<script>
    import MovieListItem from '@/components/MovieListItem.vue'
    // import { Carousel3d, Slide } from 'vue-carousel-3d';
    import 'swiper/dist/css/swiper.css'

    import { swiper, swiperSlide } from 'vue-awesome-swiper'

    export default {
        name: 'MovieList',
        data() {
            return {
                        swiperOption: {
          effect: 'coverflow',
          grabCursor: true,
          centeredSlides: true,
          slidesPerView: 'auto',
        //   spaceBetween: 5,
          coverflowEffect: {
            rotate: 10,
            stretch: 0,
            depth: 100,
            modifier: 1,
            slideShadows : true
          },
          pagination: {
            el: '.swiper-pagination'
          }
        }
            }
        },
        components: {
            MovieListItem,
            swiper,
            swiperSlide
            // Carousel3d,
            // Slide
        },
        props: {
            movies: {
                type: Array,
                required: true
            }
        },
        methods: {

        },
        computed: {
            swiper() {
                return this.$refs.mySwiper.swiper
            }
        },
        mounted() {
            console.log('this is current swiper instance object', this.swiper)
            this.swiper.slideTo(3, 1000, false)
        }
    }
</script>

<style>
    .swiper-inner {
    width: 100%;
    height: 200px;
    padding-top: 50px;
    padding-bottom: 50px;
  }
  .swiper-slide {
    background-position: center;
    background-size: cover;
    width: 500px;
    height: 500px;
  }
  .swiper-container {
  height: 800px;
  width: 100%;
}
</style>