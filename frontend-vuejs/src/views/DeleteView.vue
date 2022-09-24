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
