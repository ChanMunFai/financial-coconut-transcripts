import React from 'react';
import Search from './Search.js'
import "./Home.css";

export default function Home({ data }) {
  return (
    <div className='HomeContainer'> 
      <div className='cards'>
        <Search details={data.posts}/>
      </div> 
    </div>
  );
}
