<script>
import CustomButton from "../components/CustomButton.vue";
export default {
  name: "TransferView",
  props: {},
  components: {
    CustomButton,
  },
  data() {
    return {
      accounts: [],
      alertShow: false,
      alertType: "",
      alertMsg: "",

      idFromAccount: "",
      typeFromAccount: "",
      validateFromAccount: true,

      idToAccount: "",
      typeToAccount: "",
      validateToAccount: true,

      amount: "0.00",
      validateAmount: true,
    };
  },
  /* Reminder to transfer into a reusable component */
  watch: {
    idFromAccount(value) {
      if (value !== "") {
        this.validateFromAccount = true;
        this.validateToAccount = true;
        this.idFromAccount = value;
        this.typeFromAccount = this.accounts.find(
          (account) => account.id === value
        ).type_name;
        console.log(this.typeFromAccount);
      }
    },
    idToAccount(value) {
      if (value !== "") {
        this.validateFromAccount = true;
        this.validateToAccount = true;
        this.idToAccount = value;
        this.typeToAccount = this.accounts.find(
          (account) => account.id === value
        ).type_name;
      }
    },
    amount(value) {
      let checkValidation = this.validatingAmount(value);
      if (checkValidation) {
        this.validateAmount = true;
        this.amount = value;
      } else {
        this.validateAmount = false;
      }
    },
  },
  methods: {
    async fetchAccounts() {
      const res = await fetch("api/accounts");
      const acctData = await res.json();
      return acctData;
    },
    async onSubmit(e) {
      e.preventDefault();

      //Final Validation before doing try catch
      if (
        this.idFromAccount !== "" &&
        this.idToAccount !== "" &&
        this.idFromAccount !== this.idToAccount
      ) {
        try {
          //Turn it into JSON Format Type
          const transferFromAccount = {
            transfer_type: "deduct",
            transfer_amount: this.amount,
          };

          const transferToAccount = {
            transfer_type: "add",
            transfer_amount: this.amount,
          };
          //Deduct from selected Account
          const deductRes = await fetch(`api/account/${this.idFromAccount}`, {
            method: "PATCH",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(transferFromAccount),
          });

          //Add into selected account
          const addRes = await fetch(`api/account/${this.idToAccount}`, {
            method: "PATCH",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(transferToAccount),
          });

          if (deductRes.status === 200 && addRes.status === 200) {
            this.alertMsg = `Successfully transferred from ${this.typeFromAccount} Account to ${this.typeToAccount} Account.`;
            this.alertShow = true;
            this.alertType = "alert-success";
            this.accounts = await this.fetchAccounts();
            // this.$router.push({
            //   path: "/view-accounts",
            //   query: { success: "true" },
            // });
          } else {
            throw new Error();
          }
        } catch (error) {
          this.alertMsg = "Sorry we encountered an error!";
          this.alertType = "alert-danger";
        }
      } else {
        this.validateFromAccount = false;
        this.validateToAccount = false;
      }
    },
    validatingAmount(amount) {
      if (!/^\d+\.{0,1}\d{0,2}$/.test(amount)) {
        return false;
      } else {
        return true;
      }
    },
  },
  async created() {
    this.accounts = await this.fetchAccounts();
  },
  computed: {
    isDisabled() {
      return (
        !this.validateFromAccount ||
        !this.validateToAccount ||
        !this.validateAmount
      );
    },
  },
};
</script>

<template>
  <section class="container my-5">
    <CustomButton :hasLink="true" btnLink="/" btnTitle="Back" />
    <section class="my-5">
      <h1>Transfer Money</h1>
      <p>Transfer your money from one account to another.</p>
      <div v-show="alertShow" :class="alertType" class="alert">
        {{ alertMsg }}
      </div>
    </section>

    <form @submit="onSubmit">
      <div class="mb-3">
        <label
          :class="[validateFromAccount ? '' : 'is-invalid', 'form-label']"
          class="form-label"
          >From Account:</label
        >
        <select
          class="form-select"
          name="from-account"
          id="fromAccount"
          v-model="idFromAccount"
          :class="[validateFromAccount ? '' : 'is-invalid', 'form-select']"
        >
          <option selected value="">Select Account</option>
          <option
            v-for="account in accounts"
            :key="account.id"
            :value="account.id"
          >
            {{ account.type_name }} - RM{{ account.balance }}
          </option>
        </select>
        <div class="invalid-feedback">
          Please do not select the same account to transfer
        </div>
      </div>

      <div class="mb-3">
        <label
          :class="[validateToAccount ? '' : 'is-invalid', 'form-label']"
          class="form-label"
          >To Account:</label
        >
        <select
          class="form-select"
          name="to-account"
          id="toAccount"
          v-model="idToAccount"
          :class="[validateToAccount ? '' : 'is-invalid', 'form-select']"
        >
          <option selected value="">Select Account</option>
          <option
            v-for="account in accounts"
            :key="account.id"
            :value="account.id"
          >
            {{ account.type_name }} - RM{{ account.balance }}
          </option>
        </select>
        <div class="invalid-feedback">
          Please do not select the same account to transfer
        </div>
      </div>

      <div class="mb-3">
        <label :class="[validateAmount ? '' : 'is-invalid', 'form-label']"
          >Amount To Transfer (RM):</label
        >
        <input
          :class="[validateAmount ? '' : 'is-invalid', 'form-control']"
          type="text"
          v-model="amount"
        />
        <div class="invalid-feedback">Please insert the correct amount.</div>
      </div>

      <CustomButton btnTitle="Transfer" :disabled="isDisabled" />
    </form>
  </section>
</template>
