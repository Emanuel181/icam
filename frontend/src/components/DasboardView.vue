<template>
  <div>
    <h1>Dashboard</h1>
    <p v-if="loading">Loading user details...</p>
    <div v-if="!loading && user">
      <p><strong>Welcome,</strong> {{ user.username }}!</p>
      <p>Your role: {{ user.role }}</p>
      <div class="actions">
        <router-link v-if="user.role === 'student'" to="/projects">View Projects</router-link>
        <router-link v-if="user.role === 'mentor'" to="/mentor">Mentor Dashboard</router-link>
        <router-link v-if="user.role === 'initiator'" to="/initiatives">Manage Initiatives</router-link>
        <router-link to="/profile">Go to Profile</router-link>
      </div>
    </div>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
  </div>
</template>

<script>
import axios from "../axios";

export default {
  data() {
    return {
      user: null,
      loading: true,
      errorMessage: "",
    };
  },
  async created() {
    try {
      const response = await axios.get("user/");
      this.user = response.data;
    } catch (error) {
      this.errorMessage =
        error.response?.data?.detail ||
        "Failed to fetch user details. Please log in again.";
      console.error("Error fetching user details:", error);
      this.$router.push("/login");
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
.actions {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
</style>
