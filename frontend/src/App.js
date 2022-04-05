import logo from './logo.svg';
import './App.css';
import {Routes, Route, BrowserRouter} from 'react-router-dom';
import { Products } from './components/Products';
import { Wrapper } from './components/Wrapper';
import { ProductCreate } from './components/ProductCreate';
import { Orders } from './components/Orders';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Products/>}/>
        <Route path="/create" element={<ProductCreate/>}/>
        <Route path="/orders" element={<Orders/>}/>
      </Routes>
      </BrowserRouter>
  );
}

export default App;
