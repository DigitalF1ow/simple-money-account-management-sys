<script>
export default {
  name: "PopUpModal",
  props: {
    title: {
      type: String,
      default: "Placeholder Modal Title",
    },
    content: {
      type: String,
      default: "Placeholder Content",
    },
    modalType: {
      type: String,
      default: "default",
    },
  },
  methods: {
    showModal() {},
  },
};
</script>

<template>
  <div ref="modalRef" class="modal show" tabindex="-1">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">{{ title }}</h5>
          <button type="button" class="btn-close"></button>
        </div>
        <div class="modal-body">
          <p>Modal body text goes here.</p>
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal"
          >
            Close
          </button>
          <button type="button" class="btn btn-primary">Save changes</button>
        </div>
      </div>
    </div>
  </div>
</template>
