import React from 'react';
import { Switch, Route, Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import AddNote from './components/add-note';
import NotesList from './components/notes-list';
import Login from './components/login';
import Signup from './components/signup';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
function App() {
return (
<div className="App">
<Navbar bg="primary" variant="light">
<div className="container-fluid">
<Navbar.Brand>Notes App</Navbar.Brand>
<Nav className="me-auto">
<Nav.Link href="#home">Home</Nav.Link>
<Nav.Link href="#link">Link</Nav.Link>
</Nav>
</div>
</Navbar>
</div>
);
}
export default App;
