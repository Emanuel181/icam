<template>
  <div class="home-container">
    <div class="welcome-message">
      <h1>Welcome back, {{ user.username }}!</h1>
      <p>Role: <strong>{{ user.role }}</strong></p>
      <p>
        Start exploring projects, apply to exciting opportunities, or create a new project idea!
      </p>
    </div>
    <div class="actions">
      <router-link to="/profile">
        <button class="primary-button">Go to Profile</button>
      </router-link>
      <router-link to="/projects">
        <button class="secondary-button">View Projects</button>
      </router-link>
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
    };
  },
  async created() {
    try {
      const response = await axios.get("/user/");
      this.user = response.data;
    } catch (error) {
      this.$router.push("/login?message=Session expired. Please log in again.");
    } finally {
      this.loading = false;
    }
  },
};
</script>

<style scoped>
.home-container {
  padding: 20px;
  background-color: #f9f9f9;
  text-align: center;
}

.welcome-message h1 {
  font-size: 2rem;
  margin-bottom: 10px;
}

.actions {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-top: 20px;
}

.primary-button,
.secondary-button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  cursor: pointer;
}

.primary-button {
  background-color: #007bff;
  color: white;
}

.secondary-button {
  background-color: #6c757d;
  color: white;
}

.primary-button:hover,
.secondary-button:hover {
  opacity: 0.9;
}
</style>
