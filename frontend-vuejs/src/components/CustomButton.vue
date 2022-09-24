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
    btnStyle: {
      type: String,
      default: "btn-primary",
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
    <button class="btn" :class="btnStyle">
      {{ btnTitle }}
    </button>
  </router-link>

  <button v-else class="btn" :class="btnStyle" @click="onClick()">
    {{ btnTitle }}
  </button>
</template>
