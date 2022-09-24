<script>
export default {
  name: "DashboardItem",
  props: {
    acctLink: {
      type: String,
      default: "/",
    },
    titleName: {
      type: String,
      default: "Placeholder Operation",
    },
  },
};
</script>

<template>
  <router-link :to="acctLink" class="cardLink">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">{{ titleName }}</h5>
      </div>
    </div>
  </router-link>
</template>

<style scoped>
.cardLink {
  text-decoration: none;
  color: black;
  transition: 0.3s;
}
.card {
  transition: 0.3s;
}
.card:hover {
  color: black;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.25);
}
</style>
