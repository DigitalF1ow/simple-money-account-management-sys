import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../views/HomePage.vue";
import AccountView from "../views/AccountView.vue";
import TransferView from "../views/TransferView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomePage,
    },
    {
      path: "/accounts",
      name: "accounts",
      component: AccountView,
    },
    {
      path: "/transfer",
      name: "transfer-money",
      component: TransferView,
    },
  ],
});

export default router;
