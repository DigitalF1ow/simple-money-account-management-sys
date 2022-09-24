<script>
import AccountItem from "../components/AccountItem.vue";
export default {
  name: "AccountView",
  props: {},
  components: {
    AccountItem,
  },
};
</script>

<template>
  <div class="container my-5">
    <section class="my-5">
      <h1>View Account Balance</h1>
      <p>Check your account types and details from here.</p>
    </section>
    <section class="row row-cols-1 row-cols-md-3 g-4">
      <div class="col">
        <AccountItem acctName="Savings Account" acctBalance="RM0.00" />
      </div>
      <div class="col">
        <AccountItem acctName="Goals Account" acctBalance="RM0.00" />
      </div>
      <div class="col">
        <AccountItem acctName="Investments Account" acctBalance="RM0.00" />
      </div>
    </section>
  </div>
</template>
