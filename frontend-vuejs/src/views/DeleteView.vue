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
    async transferRemaining(account_id) {
      const getSavingsID = this.accounts.find(
        (account) => account.acct_type === 1
      ).id;
      const getClosingBalance = this.accounts.find(
        (account) => account.id === account_id
      ).balance;
      //Turn it into JSON Format Type
      const transferFromAccount = {
        transfer_type: "deduct",
        transfer_amount: getClosingBalance,
      };

      const transferToAccount = {
        transfer_type: "add",
        transfer_amount: getClosingBalance,
      };

      try {
        //Deduct from selected Account
        const deductRes = await fetch(`api/account/${account_id}`, {
          method: "PATCH",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(transferFromAccount),
        });

        //Add into selected account
        const addRes = await fetch(`api/account/${getSavingsID}`, {
          method: "PATCH",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(transferToAccount),
        });

        if (deductRes.status === 200 && addRes.status === 200) {
          return true;
        }
      } catch (error) {
        this.errorMsg =
          "Something went wrong while trying to transfer the money! We are sorry about that.";
        this.errorDelete = true;
        return error;
      }
    },
    async deleteAccount(account_id) {
      try {
        const transferRes = await this.transferRemaining(account_id);

        if (transferRes === true)
        {
          const res = await fetch(`api/account/${account_id}`, {
            method: "DELETE",
          });

          if (res.status === 200) {
            this.successDelete = true;
            this.accounts = await this.fetchAccounts();
          } else {
            throw new Error();
          }
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
        Account Successful Deleted. Check your savings account to see if your
        new balance.
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
