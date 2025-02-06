<template>
  <div class="landing-container">
    <div class="hero-section">
      <h1>Welcome to ICAM Platform</h1>
      <p>
        Connecting innovators, professionals, and students to collaborate on innovative projects and ideas.
      </p>
      <div class="button-group">
        <router-link to="/login">
          <button class="primary-button">Login</button>
        </router-link>
        <router-link to="/register">
          <button class="secondary-button">Register</button>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LandingPage",
};
</script>

<style scoped>
.landing-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: linear-gradient(135deg, #5b86e5, #36d1dc);
  color: #fff;
  text-align: center;
  padding: 0 20px;
}

.hero-section h1 {
  font-size: 2.5rem;
  font-weight: bold;
  margin-bottom: 20px;
}

.hero-section p {
  font-size: 1.2rem;
  margin-bottom: 30px;
}

.button-group {
  display: flex;
  gap: 10px;
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
  background-color: transparent;
  border: 2px solid white;
  color: white;
}

.primary-button:hover,
.secondary-button:hover {
  opacity: 0.8;
}
</style>
