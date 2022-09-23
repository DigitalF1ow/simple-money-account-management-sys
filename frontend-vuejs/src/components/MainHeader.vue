<script>
export default {
  name: "MainHeader",
  props: {
    title: {
      type: String,
      default: "Not Supposed To Happen",
    },
  },
};
</script>

<template>
  <header>
    <nav class="navbar navbar-expand-lg bg-light">
      <div class="container-fluid">
        <router-link class="navbar-brand" to="/">{{ title }}</router-link>
        <div class="collapse navbar-collapse">
          <ul class="navbar-nav">
            <li class="nav-item">
              <router-link class="nav-link" to="/">Home</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>
