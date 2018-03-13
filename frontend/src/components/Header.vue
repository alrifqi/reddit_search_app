<template>
    <div class="row row-heading">
        <div class="input-field col s9">
            <input placeholder="Search" id="first_name" type="text" class="validate input-search" v-model="keyword" v-on:keyup.enter="searchHeader">
        </div>
        
        <div class="input-field col s3">
            <button class="btn waves-effect waves-light" type="submit" name="action" v-on:click="searchHeader">Submit</button>
        </div>

        <div class="col s12 scrollable">
            <span v-for="sub in subreddit">
                <a class="vbadge"  v-on:click="subredditSearch(sub)">{{ sub }}</a>
            </span>
            
        </div>
    </div>
</template>


<script>
    export default {
      name: 'Header',
      props: ['subreddit'],
      data () {
        return {
          keyword: ''
        }
      },
      methods: {
        searchHeader () {
          this.$bus.$emit('search', this.keyword)
        },
        subredditSearch (subreddit) {
          this.$bus.$emit('subredditSearch', subreddit)
        }
      }
    }
</script>

<style scoped>
    .row-heading {
        background-color: #fafafa;
        border-bottom: 1px solid #ebebeb;
        padding-bottom: 20px;
    }

    .vbadge {
        display: inline-block;
        padding: .25em .4em;
        line-height: 1;
        color: #fff;
        text-align: center;
        white-space: nowrap;
        vertical-align: baseline;
        border-radius: .25rem;
        padding-right: .6em;
        padding-left: .6em;
        border-radius: 10rem;
        background-color: #28a745;
        margin: 0px 5px;
    }

    .scrollable {
        height: 10% !important;
        max-height: 10% !important;
        width: 90% !important;
        max-width: 90% !important;
        overflow: scroll;
        overflow-x: hidden;
    }

    .scrollable > span {
        display: inline-block;
        text-align: center;
    }
</style>