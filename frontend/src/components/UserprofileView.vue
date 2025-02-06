<template>
  <div>
    <h1>User Profile</h1>
    <p v-if="loading">Loading user details...</p>
    <div v-if="!loading">
      <p><strong>Username:</strong> {{ user.username }}</p>
      <p><strong>Email:</strong> {{ user.email }}</p>
      <p><strong>Role:</strong> {{ user.role }}</p>
      <button @click="logout" class="logout-button">Logout</button>
    </div>
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
      // Fetch user details when the component is created
      const response = await axios.get("user/");
      this.user = response.data; // Set user data
      this.loading = false; // Set loading to false
    } catch (error) {
      this.errorMessage = "Failed to fetch user details.";
      console.error("Error fetching user details:", error);
      this.$router.push("/login"); // Redirect to login if unauthorized
    }
  },
  methods: {
    logout() {
      // Clear tokens and redirect to login
      localStorage.removeItem("token");
      localStorage.removeItem("refresh_token");
      this.$router.push("/login");
    },
  },
};
</script>

<style scoped>
.logout-button {
  background-color: #ff4d4d;
  color: white;
  border: none;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  border-radius: 5px;
}
.logout-button:hover {
  background-color: #ff0000;
}
</style>
