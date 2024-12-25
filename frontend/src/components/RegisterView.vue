<template>
  <div>
    <h1>Register</h1>
    <form @submit.prevent="handleRegister">
      <input type="text" v-model="username" placeholder="Username" required />
      <input type="password" v-model="password" placeholder="Password" required />
      <select v-model="role">
        <option value="student">Student</option>
        <option value="mentor">Mentor</option>
        <option value="initiator">Initiator</option>
      </select>
      <button type="submit">Register</button>
    </form>
    <p v-if="errorMessage">{{ errorMessage }}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      username: "",
      password: "",
      role: "student",
      errorMessage: "",
    };
  },
  methods: {
    async handleRegister() {
      try {
        await axios.post("http://127.0.0.1:8000/api/auth/register/", {
          username: this.username,
          password: this.password,
          role: this.role,
        });
        this.$router.push("/login");
      } catch (error) {
        this.errorMessage = "Registration failed. Try again.";
      }
    },
  },
};
</script>
