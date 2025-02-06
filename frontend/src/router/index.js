import { createRouter, createWebHistory } from "vue-router";

// Import Vue components
import LandingPage from "../components/LandingPage.vue";
import LoginView from "../components/LoginView.vue";
import RegisterView from "../components/RegisterView.vue";
import HomePage from "../components/HomePage.vue";
import PasswordResetView from "../components/PasswordResetView.vue";
import PasswordResetConfirmView from "../components/ResetPasswordForm.vue";
import PasswordResetSuccessView from "../components/PasswordResetSuccessView.vue";
import EmailConfirmedView from "../components/EmailConfirmedView.vue";
import UserProfile from "../components/UserProfileView.vue";
import Dashboard from "../components/DasboardView.vue";

const routes = [
  // Landing Page
  {
    path: "/",
    name: "LandingPage",
    component: LandingPage,
  },
  // Login Page
  {
    path: "/login",
    name: "Login",
    component: LoginView,
  },
  // Registration Page
  {
    path: "/register",
    name: "Register",
    component: RegisterView,
  },
  // Home Page
  {
    path: "/home",
    name: "Home",
    component: HomePage,
  },
  // Password Reset Request (Step 1)
  {
    path: "/password-reset",
    name: "PasswordReset",
    component: PasswordResetView, // Page for requesting a password reset
  },
  // Password Reset Confirmation (Step 2)
  {
    path: "/reset-password/:uid/:token",
    name: "PasswordResetConfirm",
    component: PasswordResetConfirmView, // Page for resetting the password
    props: true, // Pass `uid` and `token` from the URL to the component
  },
  // Password Reset Success (Step 3)
  {
    path: "/password-reset-success",
    name: "PasswordResetSuccess",
    component: PasswordResetSuccessView, // Page displayed after successful password reset
  },
  // Email Confirmation
  {
    path: "/email-confirmed",
    name: "EmailConfirmed",
    component: EmailConfirmedView,
    props: (route) => ({ confirmationKey: route.query.key }), // Pass query parameters as props
  },
  // User Profile Page
  {
    path: "/profile",
    name: "UserProfile",
    component: UserProfile,
  },
  // Dashboard Page
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
