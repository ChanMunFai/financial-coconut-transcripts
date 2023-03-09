import { Link, useMatch, useResolvedPath } from "react-router-dom"
import "./NavBar.css";
import logo from './logo.png';

export default function Navbar() {
  return (
    <nav className="NavBar">
      <div className = "TitleContainer">
        <img src={logo} alt="logo" className="Logo"></img>
        <Link to="/" className="HomeButton">
          Financial Coconut Transcripts
        </Link>
      </div>
      <span className = "AboutContainer">
        <CustomLink className="AboutButton" to="/about" >About</CustomLink>
      </span>
    </nav>
  )
}

function CustomLink({ to, children, ...props }) {
  const resolvedPath = useResolvedPath(to)
  const isActive = useMatch({ path: resolvedPath.pathname, end: true })

  return (
    <li className={isActive ? "active" : ""} style={{color: "black"}}>
      <Link to={to} {...props}>
        {children}
      </Link>
    </li>
  )
}