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
      <h5 class="card-title">{{ account.typename }} Account</h5>
      <p class="card-text">
        Account Balance <br />
        RM{{ account.balance }}
      </p>
      <CustomButton
        v-if="this.$route.path === '/close-accounts' && account.acct_type === 3"
        btnTitle="Close Account"
        @btn-click="$emit('close-account', account.id)"
      />
    </div>
  </div>
</template>
