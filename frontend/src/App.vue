<script setup>
import { RouterLink, RouterView } from "vue-router";
import HelloWorld from "./components/HelloWorld.vue";
import PeopleView from "./views/PeopleView.vue";
</script>

<template>
  <div class="app">
      <div class="content">
        <PeopleView></PeopleView>
      </div>
  </div>
</template>