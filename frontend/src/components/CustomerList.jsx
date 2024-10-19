import React, { useState, useEffect } from 'react';
import SearchBar from './searchbar';

const CustomerList = ({ customers, onSelectCustomer, selectedCustomerID, setFilteredCustomers }) => {
  const [searchTerm, setSearchTerm] = useState('');

  const handleSearch = (term) => {
    setSearchTerm(term);
  };

  const filteredCustomers = customers.filter((customer) =>
    `${customer.FIRST_N.toLowerCase()} ${customer.LAST_N.toLowerCase()}`.includes(searchTerm.toLowerCase())
  );

  useEffect(() => {
    setFilteredCustomers(filteredCustomers);
  }, [filteredCustomers, setFilteredCustomers]);

  return (
    <div>
      <SearchBar onSearch={handleSearch} />
      <h2>Customer List</h2>
      <ul className="customer-list">
        {filteredCustomers.map((customer) => (
          <li
            key={customer.ID_NO}
            onClick={() => onSelectCustomer(customer.ID_NO)}
            className={customer.ID_NO === selectedCustomerID ? 'selected' : ''}
          >
            {customer.FIRST_N} {customer.LAST_N}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CustomerList;