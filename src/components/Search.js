import React, { useState } from 'react';
import SearchList from './SearchList';
import './Search.css'

function Search({ details }) {

  const [searchField, setSearchField] = useState("");
  // Iteration 1: filter cards whose titles and summary are within search input 
  // Final iteration: search through all content 

  const filteredPosts = details.filter(
    post => {
      return (
        post
        .title
        .toLowerCase()
        .includes(searchField.toLowerCase()) ||
        post
        .content
        .toLowerCase()
        .includes(searchField.toLowerCase())
      );
    }
  );

  const handleChange = e => {
    setSearchField(e.target.value);
  };

  function searchList() {
    return (
      <SearchList filteredCards={filteredPosts} />
    );
  }

  return (
    <div>
      <div className='search-bar-container'>
        <input 
          className="search-bar"
          type = "search" 
          placeholder = "Search Financial Coconut" 
          onChange = {handleChange}
        />
      </div>
      {searchList()}
    </div>
  );
}

export default Search;