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
      accounts: [],
      successDelete: false,
      errorDelete: false,
      errorMsg: "",
    };
  },
  methods: {
    async fetchAccounts() {
      const res = await fetch("api/accounts");

      const acctData = await res.json();
      return acctData;
    },
    async transferAccount() {},
    async deleteAccount(account_id) {
      try {
        const res = await fetch(`api/account/${account_id}`, {
          method: "DELETE",
        });

        if (res.status === 200) {
          this.successDelete = true;
          this.accounts = await this.fetchAccounts();
        } else {
          throw new Error();
        }
      } catch (error) {
        this.errorMsg = "Something went wrong! We are sorry about that.";
        this.errorDelete = true;
      }
    },
  },
  async created() {
    this.accounts = await this.fetchAccounts();
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
      <div v-show="successDelete" class="alert alert-success">
        Account Successful Deleted.
      </div>
      <div v-show="errorDelete" class="alert alert-danger">
        {{ errorMsg }}
      </div>
    </section>
    <section class="row row-cols-1 row-cols-md-3 g-4">
      <div :key="account.id" v-for="account in accounts" class="col">
        <AccountItem :account="account" @close-account="deleteAccount" />
      </div>
    </section>
  </div>
</template>
