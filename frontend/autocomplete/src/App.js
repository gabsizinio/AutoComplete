import React from 'react';
import './App.css';
import Autocomplete from './components/Autocomplete';

function App() {
  return (
    <div className="App">
      <h1 className="titulo-buscador">Buscador Jurídico</h1>
      <p className="subtitle">Digite no campo abaixo para obter sugestões</p>
      <Autocomplete />
    </div>
  );
}

export default App;
