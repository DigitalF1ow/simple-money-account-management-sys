<script>
export default {
  name: "AccountItem",
  props: {
    acctName: {
      type: String,
      default: "Placeholder Account",
    },
    acctBalance: {
      type: String,
      default: "Placeholder Account",
    },
  },
};
</script>

<template>
  <div class="card">
    <div class="card-body">
      <h5 class="card-title">{{ acctName }}</h5>
      <p class="card-text">
        Account Balance <br />
        {{ acctBalance }}
      </p>
    </div>
  </div>
</template>
