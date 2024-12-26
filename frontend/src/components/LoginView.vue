<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="handleLogin">
      <input type="text" v-model="username" placeholder="Username" required />
      <input type="password" v-model="password" placeholder="Password" required />
      <button type="submit">Login</button>
    </form>
    <p v-if="errorMessage" style="color: red;">{{ errorMessage }}</p>
  </div>
</template>

<script>
import axiosInstance from '../axios.js';

export default {
  data() {
    return {
      username: '',
      password: '',
      errorMessage: '',
    };
  },
  methods: {
async handleLogin() {
  try {
    // Retrieve the CSRF token from the cookies
    const csrftoken = document.cookie
      .split('; ')
      .find((row) => row.startsWith('csrftoken='))
      ?.split('=')[1];

    // Make the login request
    const response = await axiosInstance.post(
      '/auth/login/',
      {
        username: this.username,
        password: this.password,
      },
      {
        headers: {
          'X-CSRFToken': csrftoken, // Include CSRF token in the header
        },
      }
    );

    // Store the JWT token
    localStorage.setItem('jwt_token', response.data.token);

    // Redirect the user
    this.$router.push('/protected');
  } catch (error) {
    this.errorMessage =
      error.response?.data?.error || 'An unexpected error occurred.';
  }
}

  },
};
</script>
