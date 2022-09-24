<script>
export default {
  name: "HeaderLink",
  props: {
    title: {
      type: String,
      default: "Placeholder Title",
    },
    navLink: {
      type: String,
      default: "/",
    },
  },
};
</script>

<template>
  <li class="nav-item">
    <router-link class="nav-link" :to="navLink">{{ title }}</router-link>
  </li>
</template>
