<script>
import DashboardItem from "../components/DashboardItem.vue";
export default {
  name: "HomePage",
  props: {},
  components: {
    DashboardItem,
  },
};
</script>

<template>
  <div class="container my-4">
    <section class="my-5">
      <h1>Welcome Back, User!</h1>
      <p>Select which operation you would like to do.</p>
    </section>

    <section class="row row-cols-1 row-cols-md-3 g-4">
      <div class="col">
        <DashboardItem titleName="View Accounts" acctLink="/accounts" />
      </div>
      <div class="col">
        <DashboardItem titleName="Transfer Money" acctLink="/transfer" />
      </div>
      <div class="col">
        <DashboardItem titleName="Delete Account" acctLink="/delete" />
      </div>
    </section>
  </div>
</template>
