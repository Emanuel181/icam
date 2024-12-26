import { createRouter, createWebHistory } from "vue-router";
import LoginForm from "../components/LoginView.vue";
import ProtectedPage from "../components/RegisterView.vue";

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
            const token = localStorage.getItem("jwt_token");
            if (token) {
                next();  // Permite accesul
            } else {
                next("/");  // Redirecționează la pagina de login
            }
        },
    },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
