import React, { useState } from 'react';
import YouTube from 'react-youtube';
import { useParams } from 'react-router';
import "./BlogPost.css";

function formatTime(seconds) {
  const minutes = Math.floor(seconds / 60);
  const secondsRemaining = Math.floor(seconds % 60);
  const minutesFormatted = minutes.toString().padStart(2, '0');
  const secondsFormatted = secondsRemaining.toString().padStart(2, '0');
  return `${minutesFormatted}:${secondsFormatted}`;
}

function DisplayTranscript(props) {
  const { post, onTimestampClick } = props;
  const keys = Object.keys(post.transcript);

  return (
    <div>
      {keys.map((key) => (
        <div key={key}>
          <p className='blog-p'>
            <a href="/#" 
              onClick={(e) => {
                e.preventDefault();
                onTimestampClick(parseFloat(key));
              }}
            >
              {formatTime(parseFloat(key))}
            </a> &nbsp; {post.transcript[key]}
          </p>
        </div>
      ))}
    </div>
  );
}

function BlogPost({ data }) {
  const [player, setPlayer] = useState(null);

  const params = useParams();
  const post = data.posts.find((dataItem) => dataItem.id === params.id);
  const youtubeID = post.url.split('v=')[1];

  const onReady = (e) => {
    setPlayer(e.target);
  };
  const onPlayHandler = () => {
    player.playVideo();
  };
  const onPauseHandler = () => {
    player.pauseVideo();
  };
  const onTimestampClick = (timestamp) => {
    if (player) {
      player.seekTo(timestamp);
      player.playVideo();
    }
  };

  return (
    <div className="blog">
      <h3 className='blog-h3'>{post.title}</h3>
      <p className='blog-p'>{post.content}</p>
      <div className="player-wrapper">
        <YouTube 
          videoId={youtubeID}
          onReady={onReady}
        />
      </div>
      <div className='btn-wrapper'>
        <button onClick={onPlayHandler} className="btn">
          Play
        </button>
        <button onClick={onPauseHandler} className="btn">
          Pause
        </button>
      </div>
      <h2 className='blog-h2'>Transcripts</h2>
      <DisplayTranscript post={post} onTimestampClick={onTimestampClick}/>
    </div>
  );
}

export default BlogPost; 

