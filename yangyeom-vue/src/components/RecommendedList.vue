<template>
    <div v-if="user.paid" class="container flex-nowrap justify-content-center text-center shadow text-shadow my-5 py-5">
        <h1 style="color: white">추천 목록</h1>
        <div v-if="cnt !== 0" class="row">
            <div v-for="recom in recommended" :key="recom.id" class="col-3 flex-nowrap shadow">
                <RecommendedListItem :recom="recom"/>
            </div>
        </div>
        <div v-else>
            <h3 style="color: white">영화를 정말 좋아하시는군요!! 추천드릴 영화가 없어요!</h3>
        </div>
    </div>
</template>

<script>
import RecommendedListItem from '@/components/RecommendedListItem.vue'
import { mapGetters } from 'vuex'

export default {
    name: 'RecommendedList',
    data() {
        return {
            
        }
    },
    components: {
        RecommendedListItem
    },
    props: {
        recommended: {
            type: Array,
            required: true
        }
    },
    computed: {
        cnt() {
            return this.recommended.length
        },
        ...mapGetters([
        'options',
        'user'
        ]),
    }
}
</script>

<style>

</style>