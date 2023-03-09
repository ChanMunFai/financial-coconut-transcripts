import React from 'react';
import { Link } from 'react-router-dom';
import "./Home.css";

export default function Home({ data }) {
  return (
    <div className='HomeContainer'> 
      <div className="cards">
        {data.posts.map((post) => (
          <div className="card" key={post.id}>
            <div className="img-wrapper">
              <img
                src={`https://ytimg.googleusercontent.com/vi/${
                  post.url.split('v=')[1]
                }/sddefault.jpg`}
                alt={post.title}
              ></img>
            </div>
            <div>
              <h3>{post.title}</h3>
              <p>{post.content.slice(0, 200) + '...'}</p>
              <Link to={`/blogpost/${post.id}`}>Learn more...</Link>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
