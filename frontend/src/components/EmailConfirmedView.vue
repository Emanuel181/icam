<template>
  <div>
    <h1 v-if="loading">Confirming Email...</h1>
    <h1 v-else-if="success">Email Confirmed!</h1>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    <router-link v-if="success" to="/login">
      <button>Go to Login</button>
    </router-link>
  </div>
</template>

<script>
import axios from "../axios";

export default {
  name: "EmailConfirmedView",
  data() {
    return {
      loading: true,
      success: false,
      errorMessage: "",
    };
  },
  async created() {
    const key = this.$route.query.key;
    if (!key) {
      this.errorMessage = "Invalid confirmation link.";
      this.loading = false;
      return;
    }
    try {
      await axios.post("registration/verify-email/", {key});
      this.success = true;
    } catch (error) {
      this.errorMessage =
          error.response?.data?.detail || "Email confirmation failed.";
    } finally {
      this.loading = false;
    }
  },
};
</script>

<style scoped>
.error {
  color: red;
}
</style>
