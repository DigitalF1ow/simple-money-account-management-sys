import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../views/HomePage.vue";
import AccountView from "../views/AccountView.vue";
import TransferView from "../views/TransferView.vue";
import DeleteView from "../views/DeleteView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomePage,
    },
    {
      path: "/view-accounts",
      name: "view-accounts",
      component: AccountView,
    },
    {
      path: "/transfer",
      name: "transfer-money",
      component: TransferView,
    },
    {
      path: "/delete-accounts",
      name: "delete-accounts",
      component: DeleteView,
    },
  ],
});

export default router;
