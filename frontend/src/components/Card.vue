<template>
    <div class="card blue-grey darken-1 fixed-card-height">
        <div class="card-content white-text">
            <span class="card-title">{{ data.post.title }}</span>
        </div>
        <div class="card-action card-action-bottom">
            <a v-bind:href=" data.post.post_link " target='_blank'>source url</a>
        </div>
    </div>
    
</template>

<script>
    export default {
      name: 'Card',
      props: ['data']
    }
</script>

<style scoped>
    .fixed-card-height {
        height: 245px !important;
        max-height: 245px !important;
        min-height: 245px !important;
    }

    .card-action-bottom {
        position: absolute !important;
        width: 100% !important;
        bottom: 0;
    }
</style>