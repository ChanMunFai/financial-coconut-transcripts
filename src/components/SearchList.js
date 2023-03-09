import React from 'react';
import Card from './Card';

function SearchList({ filteredCards }) {
  const filtered = filteredCards.map(post =>  <Card post={post}/>); 
  return (
    <div className='cards'>
      {filtered}
    </div>
  );
}

export default SearchList;