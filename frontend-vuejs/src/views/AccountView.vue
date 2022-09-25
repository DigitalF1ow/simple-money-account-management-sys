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
      accounts: [],
      successMsg: false,
    };
  },
  methods: {
    async fetchAccounts() {
      const res = await fetch("api/accounts");

      const acctData = await res.json();
      return acctData;
    },
  },
  async created() {
    this.successMsg = this.$route.query.success === "true";
    this.accounts = await this.fetchAccounts();
  },
};
</script>

<template>
  <div class="container my-5">
    <CustomButton :hasLink="true" btnLink="/" btnTitle="Back" />
    <section class="my-4">
      <font-awesome-icon class="py-2" icon="fa-solid fa-wallet" size="5x" />
      <h1>View Account Balance</h1>
      <p class="mb-5">Check your account types and details from here.</p>
    </section>
    <div v-show="successMsg" class="alert alert-success">
      New Account has successfully created.
    </div>
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
