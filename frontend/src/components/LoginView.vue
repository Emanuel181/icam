<template>
  <div>
    <h1>Login</h1>
    <p v-if="infoMessage" class="info">{{ infoMessage }}</p>
    <form @submit.prevent="login" class="login-form">
      <div class="form-group">
        <label for="username">Username</label>
        <input
          id="username"
          v-model="username"
          placeholder="Enter your username"
          type="text"
          required
        />
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input
          id="password"
          v-model="password"
          placeholder="Enter your password"
          type="password"
          required
        />
            <router-link to="/password-reset" class="forgot-password">
      Forgot your password?
    </router-link>
      </div>
      <button type="submit" class="login-button">Login</button>
    </form>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
  </div>
</template>

<script>
import axios from "../axios";

export default {
  name: "LoginView",
  data() {
    return {
      username: "",
      password: "",
      errorMessage: "",
      infoMessage: "",
    };
  },
  created() {
    // Display any info message passed in the query string (e.g., "Session expired")
    const message = this.$route.query.message;
    if (message) {
      this.infoMessage = message;
    }
  },
  methods: {
    async login() {
      try {
        this.errorMessage = ""; // Clear any previous error message
        const response = await axios.post("login/", {
          username: this.username,
          password: this.password,
        });
        console.log("Login successful:", response.data);

        // Save the authentication token
        localStorage.setItem("authToken", response.data.key);

        // Redirect to the dashboard or a specified route
        this.$router.push("/dashboard");
      } catch (error) {
        console.error("Error during login:", error);
        // Handle specific backend error messages
        this.errorMessage =
          error.response?.data?.non_field_errors?.[0] ||
          error.response?.data?.detail ||
          "Login failed. Please check your credentials.";
      }
    },
  },
};
</script>

<style scoped>
.info {
  color: green;
  margin-bottom: 10px;
}

.error {
  color: red;
  margin-top: 10px;
}

.login-form {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
}

input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.login-button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.login-button:hover {
  background-color: #0056b3;
}
.forgot-password {
  display: block;
  margin-top: 10px;
  color: #007bff;
  text-decoration: underline;
  cursor: pointer;
}
.forgot-password:hover {
  color: #0056b3;
}
</style>
