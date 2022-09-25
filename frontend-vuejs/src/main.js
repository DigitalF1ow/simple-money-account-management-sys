//Import BootStrap
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.js";

//Import FontAwesome
import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import {
  faWallet,
  faMoneyBillTransfer,
  faUser,
  faTrash,
  faCirclePlus,
} from "@fortawesome/free-solid-svg-icons";

import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

import "./assets/main.css";

const app = createApp(App);

/* add icons to the library */
library.add(faWallet, faMoneyBillTransfer, faUser, faTrash, faCirclePlus);

app.use(router);

app.component("font-awesome-icon", FontAwesomeIcon).mount("#app");
