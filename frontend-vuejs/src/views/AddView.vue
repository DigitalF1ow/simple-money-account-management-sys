<script>
import CustomButton from "../components/CustomButton.vue";
export default {
  name: "AddView",
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
      <h1>Add Account</h1>
      <p>Create a new type of Account.</p>
    </section>

    <form>
      <div class="mb-3">
        <label class="form-label" for="type-account">Account Type:</label>
        <select class="form-select" name="type-account" id="type-account">
          <option selected>Select Type</option>
          <option disabled>Savings</option>
          <option disabled>Goals</option>
          <option>Investments</option>
        </select>
      </div>

      <div class="mb-3">
        <label class="form-label">Amount To Add:</label>
        <input
          class="form-control"
          type="number"
          min="0"
          value="0"
          step=".01"
        />
      </div>

      <CustomButton btnTitle="Create" />
    </form>
  </section>
</template>
