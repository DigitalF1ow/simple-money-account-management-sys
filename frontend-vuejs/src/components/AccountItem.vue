<script>
import CustomButton from "../components/CustomButton.vue";

export default {
  name: "AccountItem",
  props: {
    account: Object,
  },
  components: {
    CustomButton,
  },
};
</script>

<template>
  <div class="card">
    <div class="card-body">
      <h5 class="card-title">{{ account.acctType }}</h5>
      <p class="card-text">
        Account Balance <br />
        RM{{ account.balance }}
      </p>
      <CustomButton
        v-if="this.$route.path === '/close-accounts'"
        btnTitle="Delete"
      />
    </div>
  </div>
</template>
