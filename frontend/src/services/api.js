import axios from 'axios';

const API_URL = 'http://localhost:5000'; // Adjust URL as necessary

export const getCustomers = async () => {
  return await axios.get(`${API_URL}/customers`);
};

export const addCustomer = async (customer) => {
  return await axios.post(`${API_URL}/customer`, customer);
};

export const updateCustomer = async (id, customer) => {
  return await axios.put(`${API_URL}/customer/${id}`, customer);
};

export const deleteCustomer = async (id) => {
  return await axios.delete(`${API_URL}/customer/${id}`);
};

// Add other CRUD operations as needed
