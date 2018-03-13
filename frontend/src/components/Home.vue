<template>
    <div>
        <Header :subreddit="subreddit"/>
        <!--<div class="row row-heading">
            <div class="input-field col s9">
                <input placeholder="Search" id="first_name" type="text" class="validate input-search" v-model="keyword" v-on:keyup.enter="postSearch">
            </div>
            
            <div class="input-field col s3">
                <button class="btn waves-effect waves-light" type="submit" name="action" v-on:click="postSearch">Submit {{$store.state.keyword}}</button>
            </div>

            <div class="col s12 scrollable">
                <span v-for="sub in subreddit">
                    <a class="vbadge"  v-on:click="subredditSearch(sub)" v-bind:href="localhost">{{ sub }}</a>
                </span>
                
            </div>
        </div>-->

        <div v-if=" loadstatus === 'fetch' " class="div-loading">
            <Circle5></Circle5>
        </div>
        <div class="row" v-else>
            <div class="col m4 s12" v-for="post in posts">
                <Card :data="{ post }"/>
            </div>
        </div>

        <div class="row">
            <div class="col s12" v-show="loadstatus === 'finish'">
                <ul class="pagination pagination-container">
                    <li v-for="n in pagination" class="waves-effect pagination-border">
                        <a v-on:click="changePage(n)">{{ n }}</a>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>


<script>
    import Header from './Header'
    import Card from './Card'
    import axios from 'axios'
    import Circle5 from 'vue-loading-spinner/src/components/Circle5.vue'

    export default {
      name: 'Home',
      data () {
        return {
          loadstatus: 'finish',
          posts: [],
          keyword: '',
          subreddit: [],
          pagination: 0
        }
      },
      watch: {
        loadstatus: function () {
          console.log(this.posts)
        }
      },
      components: {
        Header,
        Card,
        Circle5
      },
      mounted () {
        const self = this
        this.$bus.$on('search', function (value) {
          self.loadstatus = 'fetch'
          self.subreddit = []
          self.pagination = 0
          axios.post(`http://localhost:8001/reddit/postsearch`, {
            keyword: value
          })
          .then(response => {
            self.loadstatus = 'finish'
            self.keyword = value
            self.posts = response.data.post
            self.subreddit = response.data.subreddit
            self.pagination = response.data.pagination
          })
          .catch(e => {
            self.errors.push(e)
          })
        })

        this.$bus.$on('subredditSearch', function (value) {
          self.loadstatus = 'fetch'
          self.subreddit = []
          axios.post(`http://localhost:8001/reddit/subreddit`, {
            subreddit_key: value
          })
          .then(response => {
            self.loadstatus = 'finish'
            self.posts = response.data.post
            self.subreddit = response.data.subreddit
            self.pagination = response.data.pagination
          })
          .catch(e => {
            self.errors.push(e)
          })
        })
      },
      methods: {
        changePage (page) {
          this.loadstatus = 'fetch'
          axios.post(`http://localhost:8001/reddit/postsearch`, {
            keyword: this.keyword,
            page: page
          })
          .then(response => {
            this.loadstatus = 'finish'
            this.posts = response.data.post
            this.subreddit = response.data.subreddit
            this.pagination = response.data.pagination
          })
          .catch(e => {
            this.errors.push(e)
          })
        }
      }
    }
</script>

<style scoped>
    .row {
        padding: 0px 100px;
    }
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

    .div-loading {
        width:100%;
        /* Firefox */
        display:-moz-box;
        -moz-box-pack:center;
        -moz-box-align:center;

        /* Safari and Chrome */
        display:-webkit-box;
        -webkit-box-pack:center;
        -webkit-box-align:center;

        /* W3C */
        display:box;
        box-pack:center;
        box-align:center;

        margin: 50px 0px;
    }

    .pagination-container {
        width:100%;
        /* Firefox */
        display:-moz-box;
        -moz-box-pack:center;
        -moz-box-align:center;

        /* Safari and Chrome */
        display:-webkit-box;
        -webkit-box-pack:center;
        -webkit-box-align:center;

        /* W3C */
        display:box;
        box-pack:center;
        box-align:center;
    }

    .pagination-border {
        margin: 0px 5px;
        background-color: #ffcdd2;
    }
</style>