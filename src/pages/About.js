import { useEffect, useState } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from 'remark-gfm'
import styles from "./markdown-styles.module.css";

const About = () => {
  const [content, setContent] = useState("");

  useEffect(() => {
    fetch("about.md")
      .then((res) => res.text())
      .then((text) => setContent(text));
  }, []);

  return (
    <div>
      <ReactMarkdown 
        className={styles.reactMarkDown}
        children={content} 
        remarkPlugins={[remarkGfm]}/>
    </div>
  );
};

export default About; 
