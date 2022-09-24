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

    <section class="row row-cols-2 row-cols-md-4 g-2 g-md-4">
      <div class="col">
        <DashboardItem titleName="Add Account" acctLink="/add" />
      </div>
      <div class="col">
        <DashboardItem titleName="View Accounts" acctLink="/view-accounts" />
      </div>
      <div class="col">
        <DashboardItem titleName="Transfer Money" acctLink="/transfer" />
      </div>
      <div class="col">
        <DashboardItem titleName="Close Account" acctLink="/delete-accounts" />
      </div>
    </section>
  </div>
</template>
