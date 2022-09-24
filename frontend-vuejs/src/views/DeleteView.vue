<script>
import AccountItem from "../components/AccountItem.vue";
import CustomButton from "../components/CustomButton.vue";
export default {
  name: "DeleteView",
  props: {},
  components: {
    AccountItem,
    CustomButton,
  },
  data() {
    return {
      accounts: [
        {
          id: "1",
          acctType: "1",
          acctTypeName: "Savings",
          balance: "10,000.50",
        },
        {
          id: "2",
          acctType: "2",
          acctTypeName: "Goals",
          balance: "10,000.50",
        },
        {
          id: "3",
          acctType: "3",
          acctTypeName: "Investments",
          balance: "5,000.50",
        },
      ],
    };
  },
};
</script>

<template>
  <div class="container my-5">
    <CustomButton :hasLink="true" btnLink="/" btnTitle="Back" />
    <section class="my-5">
      <h1>Close Account</h1>
      <p>
        Close your account from here, if there is any available balance in the
        account, it will be transferred automatically to your savings account.
      </p>
    </section>
    <section class="row row-cols-1 row-cols-md-3 g-4">
      <div :key="account.id" v-for="account in accounts" class="col">
        <AccountItem :account="account" />
      </div>
    </section>
  </div>
</template>
