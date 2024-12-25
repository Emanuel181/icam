<template>
  <div class="protected-container">
    <h2>Welcome to the Protected Page</h2>
    <p>You are now logged in!</p>
  </div>
</template>

<script>
export default {
  name: "ProtectedPage",
};
</script>

<style scoped>
.protected-container {
  text-align: center;
  margin-top: 50px;
}
</style>
