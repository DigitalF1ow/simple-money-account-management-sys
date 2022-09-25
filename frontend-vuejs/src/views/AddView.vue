<script>
import CustomButton from "../components/CustomButton.vue";
export default {
  name: "AddView",
  props: {},
  components: {
    CustomButton,
  },
  data() {
    return {
      account: {
        accountType: "",
        amount: "0.00",
      },
      validationAccountType: true,
      validationAmount: true,
    };
  },
  watch: {
    "account.amount"(value) {
      let checkValidation = this.validateAmount(value);
      if (checkValidation) {
        this.validationAmount = true;
        this.account.amount = value;
      } else {
        this.validationAmount = false;
      }
    },
    "account.accountType"(value) {
      if (value !== "") {
        this.validationAccountType = true;
        this.account.validationAccountType = value;
      }
    },
  },
  methods: {
    validateAmount(amount) {
      if (!/^\d+\.{0,1}\d{0,2}$/.test(amount)) {
        return false;
      } else {
        return true;
      }
    },
    /* Make sure to get this working! */
    async onSubmit(e) {
      e.preventDefault();
      if (this.account.accountType !== "") {
        //Turn it into JSON Format Type
        try {
          const newAccount = {
            user_id: 1,
            acct_type: this.account.accountType,
            balance: this.account.amount,
          };

          // eslint-disable-next-line no-unused-vars
          const res = await fetch("api/accounts", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(newAccount),
          });

          // eslint-disable-next-line no-constant-condition
          if (res.status === 201) {
            this.$router.push({
              path: "/view-accounts",
              query: { success: "true" },
            });
          }

        } catch (error) {
          console.log(error);
        }
      } else {
        this.validationAccountType = false;
      }
    },
  },
  computed: {
    isDisabled() {
      return !this.validationAccountType || !this.validationAmount;
    },
  },
};
</script>

<template>
  <section class="container my-5">
    <CustomButton :hasLink="true" btnLink="/" btnTitle="Back" />
    <section class="my-5">
      <h1>Add Account</h1>
      <p>Create a new type of Account.</p>
    </section>

    <form @submit="onSubmit">
      <div class="mb-3">
        <label
          :class="[validationAccountType ? '' : 'is-invalid', 'form-label']"
          for="type-account"
          >Account Type:</label
        >
        <select
          :class="[validationAccountType ? '' : 'is-invalid', 'form-select']"
          name="type-account"
          id="type-account"
          v-model="account.accountType"
        >
          <option selected value="">Select Type</option>
          <option disabled value="1">Savings</option>
          <option disabled value="2">Goals</option>
          <option value="3">Investments</option>
        </select>
        <div class="invalid-feedback">Please select an account type.</div>
      </div>

      <div class="mb-3">
        <label :class="[validationAmount ? '' : 'is-invalid', 'form-label']"
          >Amount To Add (RM):</label
        >
        <input
          :class="[validationAmount ? '' : 'is-invalid', 'form-control']"
          type="text"
          v-model="account.amount"
        />
        <div class="invalid-feedback">Please insert the correct amount.</div>
      </div>

      <CustomButton btnTitle="Create" :disabled="isDisabled" />
    </form>
  </section>
</template>
