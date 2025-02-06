<template>
  <div>
    <h1>Register</h1>
    <form @submit.prevent="register" class="register-form">
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
        <label for="email">Email</label>
        <input
          id="email"
          v-model="email"
          placeholder="Enter your email"
          type="email"
          required
        />
      </div>
      <div class="form-group">
        <label for="password1">Password</label>
        <input
          id="password1"
          v-model="password1"
          placeholder="Enter your password"
          type="password"
          required
        />
      </div>
      <div class="form-group">
        <label for="password2">Confirm Password</label>
        <input
          id="password2"
          v-model="password2"
          placeholder="Confirm your password"
          type="password"
          required
        />
      </div>
      <button type="submit" class="register-button">Register</button>
    </form>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    <p v-if="successMessage" class="success">{{ successMessage }}</p>
  </div>
</template>

<script>
import axios from "../axios";

export default {
  name: "RegisterView",
  data() {
    return {
      username: "",
      email: "",
      password1: "",
      password2: "",
      errorMessage: "",
      successMessage: "",
    };
  },
  methods: {
    async register() {
      try {
        this.errorMessage = "";
        this.successMessage = "";

        const response = await axios.post("registration/", {
          username: this.username,
          email: this.email,
          password1: this.password1,
          password2: this.password2,
        });

        console.log("Registration successful:", response.data);

        // Display a success message
        this.successMessage =
          "Registration successful! Please check your email to verify your account.";

        // Clear the form
        this.username = "";
        this.email = "";
        this.password1 = "";
        this.password2 = "";

        // Redirect to the login page after a short delay
        setTimeout(() => {
          this.$router.push("/login");
        }, 3000);
      } catch (error) {
        console.error("Error during registration:", error);

        // Display error messages from the backend
        this.errorMessage =
          error.response?.data?.non_field_errors?.[0] ||
          error.response?.data?.detail ||
          error.response?.data?.password1?.[0] || // Handle specific field errors
          error.response?.data?.password2?.[0] ||
          error.response?.data?.email?.[0] ||
          "Registration failed. Please try again.";
      }
    },
  },
};
</script>

<style scoped>
.register-form {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  background-color: #fff;
}

h1 {
  text-align: center;
  margin-bottom: 20px;
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

.register-button {
  width: 100%;
  padding: 10px;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.register-button:hover {
  background-color: #218838;
}

.error {
  color: red;
  margin-top: 10px;
}

.success {
  color: green;
  margin-top: 10px;
}
</style>
