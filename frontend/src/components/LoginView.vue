<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="handleLogin">
      <input type="text" v-model="username" placeholder="Username" required />
      <input type="password" v-model="password" placeholder="Password" required />
      <button type="submit">Login</button>
    </form>
    <p v-if="errorMessage">{{ errorMessage }}</p>
  </div>
</template>

<script>
import axiosInstance from '../axios.js';

export default {
  name: 'LoginForm',
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
        const response = await axios.post('/auth/login/', {
            username: this.username,
            password: this.password,
        });
        const token = response.data.token;

        // Stochează token-ul în localStorage
        localStorage.setItem('jwt_token', token);

        // Redirecționează utilizatorul către o pagină protejată
        this.$router.push('/protected');
    } catch (error) {
        this.errorMessage = error.response?.data?.error || 'An unexpected error occurred.';
    }
}


  },
};

</script>
