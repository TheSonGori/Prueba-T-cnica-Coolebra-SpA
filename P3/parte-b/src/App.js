// APP.JS //

import React, { useState, useEffect } from 'react';
import './App.css';

const App = () => {
  const data = [
    {
      ean: 'EAN1',
      nombre_producto: 'Producto 1',
      sku: 'SKU1',
      market: 'Market1, Market2',
      rango_precios: '100.0 - 120.0',
    },
    {
      ean: 'EAN2',
      nombre_producto: 'Producto 2',
      sku: 'SKU2',
      market: 'Market2',
      rango_precios: '130.0 - 150.0',
    },
    {
      ean: 'EAN3',
      nombre_producto: 'Producto 3',
      sku: 'SKU3',
      market: 'Market3',
      rango_precios: '90.0 - 110.0',
    },
  ];

  const [filteredData, setFilteredData] = useState(data);
  const [visibleIndex, setVisibleIndex] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setVisibleIndex((prevIndex) => (prevIndex < filteredData.length - 1 ? prevIndex + 1 : 0));
    }, 1000);

    return () => clearInterval(interval);
  }, [filteredData]);

  // FILTRAR POR NOMBRE DE PRODUCTO //
  const handleFilterChange = (filterTerm) => {
    const filteredProducts = data.filter((item) =>
      item.nombre_producto.toLowerCase().includes(filterTerm.toLowerCase())
    );

    setFilteredData(filteredProducts);
    setVisibleIndex(0);
  };

  return (
    <div className="container">
      <img src="Coolebra.png" alt="Coolebra" className="logo" />

      <input
        type="text"
        placeholder="Filtrar por nombre"
        onChange={(e) => handleFilterChange(e.target.value)}
      />

      {filteredData.map((item, index) => (
        <div key={item.ean} className="product" style={{ display: index === visibleIndex ? 'block' : 'none' }}>
          <p className="product-name" style={{ color: '#653AAC' }}>{item.nombre_producto}</p>
          <p className="price-range" style={{ color: '#AD2B88' }}>{item.rango_precios}</p>
          <p className="market" style={{ color: '#F22571' }}>{`En ${item.market}`}</p>
        </div>
      ))}
    </div>
  );
};

export default App;
