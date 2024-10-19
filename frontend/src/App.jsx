import React, { useState, useEffect } from 'react';
import CustomerList from './components/CustomerList';
import CustomerDetails from './components/CustomerDetails';
import { getCustomers, updateCustomer, deleteCustomer } from './services/api';
import './styles/main.css';

const App = () => {
  const [customers, setCustomers] = useState([]);
  const [selectedCustomerID, setSelectedCustomerID] = useState(null);
  const [filteredCustomers, setFilteredCustomers] = useState([]);
  const [error, setError] = useState(null);
  const [successMessage, setSuccessMessage] = useState(null);

  const fetchCustomers = async () => {
    try {
      const response = await getCustomers();
      setCustomers(response.data);
      setError(null);
    } catch (error) {
      console.error('Error fetching customers:', error);
      setError('Failed to fetch customers. Please try again.');
    }
  };

  useEffect(() => {
    fetchCustomers();
  }, []);

  const handleSelectCustomer = (id) => {
    setSelectedCustomerID(id);
  };

  const handleSaveCustomer = async (updatedCustomer) => {
    try {
      await updateCustomer(updatedCustomer.ID_NO, updatedCustomer);
      const updatedCustomers = customers.map(customer => 
        customer.ID_NO === updatedCustomer.ID_NO ? updatedCustomer : customer
      );
      setCustomers(updatedCustomers);
      setSuccessMessage('Customer updated successfully');
      setTimeout(() => setSuccessMessage(null), 3000);
    } catch (error) {
      console.error('Error updating customer:', error);
      setError('Failed to update customer. Please try again.');
    }
  };

  const handleDeleteCustomer = async () => {
    if (selectedCustomerID === null) {
      setError('No customer selected to delete.');
      return;
    }
    try {
      await deleteCustomer(selectedCustomerID);
      const updatedCustomers = customers.filter(customer => customer.ID_NO !== selectedCustomerID);
      setCustomers(updatedCustomers);
      setSelectedCustomerID(null);
      setSuccessMessage('Customer deleted successfully');
      setTimeout(() => setSuccessMessage(null), 3000);
    } catch (error) {
      console.error('Error deleting customer:', error);
      setError('Failed to delete customer. Please try again.');
    }
  };

  const handleNextCustomer = () => {
    const currentIndex = filteredCustomers.findIndex(customer => customer.ID_NO === selectedCustomerID);
    if (currentIndex < filteredCustomers.length - 1) {
      const nextCustomer = filteredCustomers[currentIndex + 1];
      setSelectedCustomerID(nextCustomer.ID_NO);
    }
  };

  const handlePreviousCustomer = () => {
    const currentIndex = filteredCustomers.findIndex(customer => customer.ID_NO === selectedCustomerID);
    if (currentIndex > 0) {
      const previousCustomer = filteredCustomers[currentIndex - 1];
      setSelectedCustomerID(previousCustomer.ID_NO);
    }
  };

  const selectedCustomer = customers.find(customer => customer.ID_NO === selectedCustomerID);

  return (
    <div className="container">
      <h1>Customer Billing System</h1>
      {error && <div className="error-message">{error}</div>}
      {successMessage && <div className="success-message">{successMessage}</div>}
      <div className="main-content">
        <div className="list-container">
          <CustomerList
            customers={customers}
            onSelectCustomer={handleSelectCustomer}
            selectedCustomerID={selectedCustomerID}
            setFilteredCustomers={setFilteredCustomers}
          />
        </div>
        {selectedCustomer && (
          <div className="details-container">
            <CustomerDetails customer={selectedCustomer} onSave={handleSaveCustomer} />
            <div className="navigation-buttons">
              <button onClick={handlePreviousCustomer} disabled={filteredCustomers.findIndex(customer => customer.ID_NO === selectedCustomerID) === 0}>Previous</button>
              <button onClick={handleNextCustomer} disabled={filteredCustomers.findIndex(customer => customer.ID_NO === selectedCustomerID) === filteredCustomers.length - 1}>Next</button>
              <button onClick={handleDeleteCustomer} style={{backgroundColor: 'red'}}>Delete</button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default App;