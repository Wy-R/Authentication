<template>
    <div id="app">
        <mu-appbar v-bind:title="Title">
          <mu-icon-button icon='menu' slot="left"/>
          <mu-icon-button icon='expand_more' slot="right"/>
        </mu-appbar>
        <router-view></router-view>
    </div>
</template>

<script>
export default {
    name: 'app',
    data(){
        return {
            Title: this.$route.name
        }
    },
    watch:{
        "$route"(){
            console.log(this.Title)
            this.Title = this.$route.name
        }
    }
}
</script>

<style>
#app {
    font-family: 'Microsoft yahei';
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
}
</style>
