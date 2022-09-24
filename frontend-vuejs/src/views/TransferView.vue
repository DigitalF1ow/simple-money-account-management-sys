<script>
import CustomButton from "../components/CustomButton.vue";
export default {
  name: "TransferView",
  props: {},
  components: {
    CustomButton,
  },
};
</script>

<template>
  <section class="container my-5">
    <CustomButton :hasLink="true" btnLink="/" btnTitle="Back" />
    <section class="my-5">
      <h1>Transfer Money</h1>
      <p>Transfer your money from one account to another.</p>
    </section>

    <form>
      <div class="mb-3">
        <label class="form-label">From Account:</label>
        <select class="form-select" name="from-account" id="fromAccount">
          <option selected>Select Account</option>
          <option>Savings</option>
          <option>Goals</option>
          <option>Investments</option>
        </select>
      </div>

      <div class="mb-3">
        <label class="form-label">To Account:</label>
        <select class="form-select" name="to-account" id="toAccount">
          <option selected>Select Account</option>
          <option>Savings</option>
          <option>Goals</option>
          <option>Investments</option>
        </select>
      </div>

      <div class="mb-3">
        <label class="form-label">Amount To Transfer:</label>
        <input
          class="form-control"
          type="number"
          min="0"
          value="0"
          step=".01"
        />
      </div>
      <CustomButton btnTitle="Submit" />
    </form>
  </section>
</template>
