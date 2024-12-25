import axios from 'axios';

// Creează o instanță Axios
const axiosInstance = axios.create({
    baseURL: 'http://127.0.0.1:8000/api',
    headers: {
        'Content-Type': 'application/json',
    },
});

// Adaugă un interceptor pentru a include token-ul JWT în cereri
axiosInstance.interceptors.request.use((config) => {
    const token = localStorage.getItem('jwt_token'); // Ia token-ul din localStorage
    if (token) {
        config.headers.Authorization = `Bearer ${token}`; // Adaugă token-ul în antetul Authorization
    }
    return config;
}, (error) => {
    return Promise.reject(error);
});

// Adaugă un interceptor pentru răspunsuri
axiosInstance.interceptors.response.use(
    (response) => response,
    (error) => {
        if (error.response && error.response.status === 401) {
            // Șterge token-ul expirat
            localStorage.removeItem('jwt_token');
            // Redirect către pagina de login
            window.location.href = '/login';
        }
        return Promise.reject(error);
    }
);

export default axiosInstance;
