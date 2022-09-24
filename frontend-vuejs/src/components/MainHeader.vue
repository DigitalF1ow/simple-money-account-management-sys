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
    <nav class="navbar navbar-expand-lg bg-light">
      <div class="container-fluid">
        <router-link class="navbar-brand" to="/">{{ title }}</router-link>
        <button
          class="navbar-toggler"
          type="button"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
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
</style>
