<script>
export default {
  name: "CustomButton",
  props: {
    hasLink: {
      type: Boolean,
      default: false,
    },
    btnLink: String,
    btnTitle: {
      type: String,
      default: "Placeholder",
    },
    btnType: {
      type: String,
      default: "normal",
    },
  },
  methods: {
    onClick() {
      this.$emit("btn-click");
    },
  },
};
</script>

<template>
  <router-link v-if="hasLink" :to="btnLink">
    <button class="btn btn-primary">
      {{ btnTitle }}
    </button>
  </router-link>

  <button v-else class="btn btn-primary" @click="onClick()">
    {{ btnTitle }}
  </button>
</template>
