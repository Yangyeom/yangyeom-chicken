<template>
    <div class="container flex-nowrap justify-content-center text-center bg-dark text-light shadow text-shadow">
        <h1>영화 목록</h1>
        <div class="row">
            <div v-for="movie in movies" :key="movie.id" class="col-4 flex-nowrap shadow">
                <a href="#">
                    <img style="height:100%;width:100%" src="http://image.tmdb.org/t/p/w500/12utMjX8qV3n5htofYbTK7fVlZN.jpg" alt="">
                </a>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'MovieList',
    props: {
        movies: {
            type: Array,
            required: true
        }
    }
}
</script>

<style>

</style>