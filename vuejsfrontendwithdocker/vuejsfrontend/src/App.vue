<template>
  <OptionSelection></OptionSelection>
</template>

<script>
import OptionSelection from '@/components/OptionSelection.vue';


export default {
  name: 'App',
  components: {
    OptionSelection
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
