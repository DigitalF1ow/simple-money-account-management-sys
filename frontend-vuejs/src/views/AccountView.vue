<script>
import AccountItem from "../components/AccountItem.vue";
import CustomButton from "../components/CustomButton.vue";
export default {
  name: "AccountView",
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
          acctType: "Savings",
          balance: "10,000.50",
        },
        {
          id: "2",
          acctType: "Goals",
          balance: "20,000.50",
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
      <h1>View Account Balance</h1>
      <p>Check your account types and details from here.</p>
    </section>
    <!-- <section>
      <CustomButton :hasLink="true" btnLink="/" btnTitle="Back" />
      <CustomButton :hasLink="true" btnLink="/" btnTitle="Back" />
      <CustomButton :hasLink="true" btnLink="/" btnTitle="Back" />
    </section> -->
    <section class="row row-cols-1 row-cols-md-3 g-4">
      <div :key="account.id" v-for="account in accounts" class="col">
        <AccountItem :account="account" />
      </div>
    </section>
  </div>
</template>
