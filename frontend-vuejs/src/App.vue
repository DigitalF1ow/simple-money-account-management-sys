<script>
//import { RouterLink, RouterView } from "vue-router";
import MainHeader from "./components/MainHeader.vue";

export default {
  name: "App",
  components: {
    MainHeader,
  },
};
</script>

<template>
  <div>
    <MainHeader title="Money Account Management System" />
  </div>
</template>
