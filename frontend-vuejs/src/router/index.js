import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../views/HomePage.vue";
import AddView from "../views/AddView.vue";
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
      path: "/add-account",
      name: "add-account",
      component: AddView,
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
      path: "/close-accounts",
      name: "close-accounts",
      component: DeleteView,
    },
  ],
});

export default router;
