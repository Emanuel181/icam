<template>
  <div>
    <h1>Reset Password</h1>
    <form @submit.prevent="resetPassword">
      <input v-model="email" placeholder="Enter your email" type="email" required />
      <button type="submit">Submit</button>
    </form>
    <p v-if="successMessage" class="success">{{ successMessage }}</p>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
  </div>
</template>

<script>
import axios from "../axios";

export default {
  data() {
    return {
      email: "",
      successMessage: "",
      errorMessage: "",
    };
  },
  methods: {
async resetPassword() {
  try {
    await axios.post("auth/password/reset/", { email: this.email });
    this.successMessage = "Password reset email sent!";
  } catch (error) {
    this.errorMessage = error.response?.data?.detail || "Failed to send reset email.";
  }
}


  },
};
</script>

<style scoped>
.success {
  color: green;
}
.error {
  color: red;
}
</style>
