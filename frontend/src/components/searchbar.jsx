import React from 'react';

const SearchBar = ({ onSearch }) => {
  const handleSearch = (event) => {
    onSearch(event.target.value);
  };

  return (
    <div>
      <input 
        type="text" 
        placeholder="Search customers..." 
        onChange={handleSearch} 
        style={{ width: '100%', padding: '10px', marginBottom: '10px', boxSizing: 'border-box' }} 
      />
    </div>
  );
};

export default SearchBar;
