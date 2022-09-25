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
      <font-awesome-icon class="p-2" icon="fa-solid fa-user" size="5x" />
      <h1>Welcome Back, User!</h1>
      <p>Select which operation you would like to do.</p>
    </section>

    <section class="row row-cols-2 row-cols-md-4 g-2 g-md-4">
      <div class="col">
        <DashboardItem
          titleName="Add Account"
          acctLink="/add-account"
          faIcon="fa-solid fa-circle-plus"
          customClass="bg-add"
        />
      </div>
      <div class="col">
        <DashboardItem
          titleName="View Accounts"
          acctLink="/view-accounts"
          faIcon="fa-solid fa-wallet"
          customClass="bg-wallet"
        />
      </div>
      <div class="col">
        <DashboardItem
          titleName="Transfer Money"
          acctLink="/transfer"
          faIcon="fa-solid fa-money-bill-transfer"
          customClass="bg-transfer"
        />
      </div>
      <div class="col">
        <DashboardItem
          titleName="Close Account"
          acctLink="/close-accounts"
          faIcon="fa-solid fa-trash"
          customClass="bg-close"
        />
      </div>
    </section>
  </div>
</template>
