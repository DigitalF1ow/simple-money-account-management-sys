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
    faIcon: {
      type: String,
      default: "",
    },
    customClass: {
      type: String,
      default: "",
    },
  },
};
</script>

<template>
  <router-link :to="acctLink" class="cardLink">
    <div class="card" :class="customClass">
      <div class="card-body m-2">
        <font-awesome-icon :icon="faIcon" class="mt-2" size="3x"/>
        <h5 class="card-title mt-2">{{ titleName }}</h5>
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
.bg-add{
  background-color: #3796d6;
}
.bg-wallet {
  background-color: #4cda7b;
}
.bg-transfer {
  background-color: #f39e3d;
}
.bg-close {
  background-color: #e95050;
}
.card {
  transition: 0.3s;
  height: 10em;
}
.card:hover {
  color: black;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.25);
}
</style>
