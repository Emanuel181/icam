import axios from "axios";
import Cookies from "js-cookie";

// Create an Axios instance
const instance = axios.create({
  baseURL: "http://127.0.0.1:8000/api/", // General base URL
  withCredentials: true, // Send cookies with requests
});

// Set CSRF token from cookies
instance.defaults.headers.common["X-CSRFToken"] = Cookies.get("csrftoken");

// Add an interceptor to include the Authorization header for authenticated requests
instance.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("authToken"); // Retrieve token from localStorage
    if (token) {
      config.headers.Authorization = `Token ${token}`; // Use 'Bearer' for JWTs
    }

    // Ensure correct headers for file uploads
    if ((config.method === "post" || config.method === "put") && config.data instanceof FormData) {
      config.headers["Content-Type"] = "multipart/form-data";
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Handle 401 errors globally (optional)
instance.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      const errorDetail = error.response?.data?.detail;
      if (errorDetail === "Invalid token" || errorDetail === "Authentication credentials were not provided.") {
        localStorage.removeItem("authToken");
        window.location.href = "/login?message=Session expired. Please log in again.";
      } else {
        console.error("Unauthorized access:", error.response?.data);
      }
    }
    return Promise.reject(error);
  }
);

export default instance;
