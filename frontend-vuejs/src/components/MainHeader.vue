<script>
import HeaderLink from "./HeaderLink.vue";
export default {
  name: "MainHeader",
  props: {
    title: {
      type: String,
      default: "Placeholder Title",
    },
  },
  components: {
    HeaderLink,
  },
};
</script>

<template>
  <header>
    <nav class="navbar navbar-expand-lg bg-header">
      <div class="container-fluid">
        <router-link class="navbar-brand" to="/">{{ title }}</router-link>
        <div class="collapse navbar-collapse alignNavItemsRight">
          <ul class="navbar-nav">
            <HeaderLink title="Home" navLink="/" />
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<style scoped>
.alignNavItemsRight {
  flex-grow: 0;
}
.bg-header {
  background-color: #4cda7b;
}
</style>
