import { Routes, Route} from 'react-router-dom';
import Home from './components/Home';
import BlogPost from './components/BlogPost';

import Navbar from "./components/NavBar"
import Footer from "./components/Footer"
import data from './data.json';
import './App.css';
import About from "./pages/About";

function App() {
  return (
    <div className="App">
      <Navbar />
      <main>
        <Routes>
          <Route path="/" element={<Home data={data} />} />
          <Route path="/blogpost/:id" element={<BlogPost data={data} />} />
          <Route path="/about/" element={<About />} />
        </Routes>
      </main>
      <Footer />
    </div>
  );
}

export default App;
