<template>
  <div>
    <h1>Set New Password</h1>
    <form @submit.prevent="resetPassword">
      <input v-model="newPassword1" placeholder="Enter new password" type="password" required />
      <input v-model="newPassword2" placeholder="Confirm new password" type="password" required />
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
      newPassword1: "",
      newPassword2: "",
      successMessage: "",
      errorMessage: "",
    };
  },
  methods: {
    async resetPassword() {
      const uid = this.$route.params.uid; // Extract from route params
      const token = this.$route.params.token; // Extract from route params
      try {
        await axios.post("auth/password/reset/confirm/", {
          uid,
          token,
          new_password1: this.newPassword1,
          new_password2: this.newPassword2,
        });
        this.successMessage = "Password reset successfully!";
      } catch (error) {
        this.errorMessage = error.response?.data?.detail || "Failed to reset password.";
      }
    },
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
