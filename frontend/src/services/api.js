/**
 * frontend/src/services/api.js
 * 
 * Axios instance for communicating with the Python backend.
 */

import axios from 'axios';

const getBaseURL = () => {
  if (typeof process !== 'undefined' && process.env.REACT_APP_API_BASE_URL) {
    return process.env.REACT_APP_API_BASE_URL;
  }
  return 'http://localhost:8000';
};

const api = axios.create({
  baseURL: getBaseURL(),
});

// Request interceptor to add the session token to the Authorization header
api.interceptors.request.use(
  (config) => {
    // Better-Auth token stored in localStorage (see authClient.ts)
    const token = localStorage.getItem('bearer_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default api;
