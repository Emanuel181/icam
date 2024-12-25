import { createRouter, createWebHistory } from "vue-router";
import LoginForm from "../components/LoginView.vue";
import ProtectedPage from "../components/ProtectedView.vue";

const routes = [
  {
    path: "/",
    name: "Login",
    component: LoginForm,
  },
  {
    path: "/protected",
    name: "ProtectedPage",
    component: ProtectedPage,
    beforeEnter: (to, from, next) => {
      // Check if the user is authenticated
      const token = localStorage.getItem("jwt_token");
      if (token) {
        next();
      } else {
        next("/");
      }
    },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
