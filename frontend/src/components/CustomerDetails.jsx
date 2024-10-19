import React, { useState, useEffect } from 'react';

const CustomerDetails = ({ customer, onSave }) => {
  const [formData, setFormData] = useState(customer);

  useEffect(() => {
    setFormData(customer);
  }, [customer]);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSave(formData);
  };

  return (
    <div>
      <h2>Customer Details</h2>
      <form onSubmit={handleSubmit} className="customer-details-form">
        <div className="form-column">
          <div>
            <label>Last Name:</label>
            <input type="text" name="LAST_N" value={formData.LAST_N || ''} onChange={handleChange} />
          </div>
          <div>
            <label>First Name:</label>
            <input type="text" name="FIRST_N" value={formData.FIRST_N || ''} onChange={handleChange} />
          </div>
          <div>
            <label>Title:</label>
            <input type="text" name="TITLE" value={formData.TITLE || ''} onChange={handleChange} />
          </div>
          <div>
            <label>Street:</label>
            <input type="text" name="STREET" value={formData.STREET || ''} onChange={handleChange} />
          </div>
          <div>
            <label>City:</label>
            <input type="text" name="CITY" value={formData.CITY || ''} onChange={handleChange} />
          </div>
          <div>
            <label>Zip:</label>
            <input type="text" name="ZIP" value={formData.ZIP || ''} onChange={handleChange} />
          </div>
          <div>
            <label>Mailing Street:</label>
            <input type="text" name="M_STREET" value={formData.M_STREET || ''} onChange={handleChange} />
          </div>
          <div>
            <label>Mailing City:</label>
            <input type="text" name="M_CITY" value={formData.M_CITY || ''} onChange={handleChange} />
          </div>
          <div>
            <label>Mailing State:</label>
            <input type="text" name="M_STATE" value={formData.M_STATE || ''} onChange={handleChange} />
          </div>
          <div>
            <label>Mailing Zip:</label>
            <input type="text" name="M_ZIP" value={formData.M_ZIP || ''} onChange={handleChange} />
          </div>
        </div>
        <div className="form-column">
          <div>
            <label>Acreage:</label>
            <input type="text" name="ACREAGE" value={formData.ACREAGE || ''} onChange={handleChange} />
          </div>
          <div>
            <label>Assessment:</label>
            <input type="text" name="ASSESSMENT" value={formData.ASSESSMENT || ''} onChange={handleChange} />
          </div>
          <div>
            <label>ID No:</label>
            <input type="text" name="ID_NO" value={formData.ID_NO || ''} onChange={handleChange} />
          </div>
          <div>
            <label>PIN:</label>
            <input type="text" name="PIN" value={formData.PIN || ''} onChange={handleChange} />
          </div>
          <div>
            <label>Total Due:</label>
            <input type="text" name="TotalDue" value={formData.TotalDue || ''} onChange={handleChange} />
          </div>
          <div>
            <label>Fee:</label>
            <input type="text" name="FeePaid" value={formData.FeePaid || ''} onChange={handleChange} />
          </div>
          <div className="form-actions">
            <button type="submit">Save</button>
          </div>
        </div>
      </form>
    </div>
  );
};

export default CustomerDetails;
