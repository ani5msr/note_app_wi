import React from 'react';
import { Switch, Route, Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import AddNote from './components/add-note';
import NotesList from './components/notes-list';
import Login from './components/login';
import Signup from './components/signup';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Container from 'react-bootstrap/Navbar';
function App() {
const [user, setUser] = React.useState(null);
const [token, setToken] = React.useState(null);
const [error, setError] = React.useState('');
async function login(user = null){ // default user to null
setUser(user);
}
async function logout(){
setUser(null);
}
async function signup(user = null){ // default user to null
setUser(user);
}
return (
<div className="App">
<Navbar bg="primary" variant="light">
<div className="container-fluid">
<Navbar.Brand>Notes App</Navbar.Brand>
<Nav className="me-auto">
<Container>
<Link class="nav-link" to={"/notes"}>Notes</Link>
{ true ? (
<Link class="nav-link">Logout </Link>
) : (
<>
<Link class="nav-link" to={"/login"}>Login</Link>
<Link class="nav-link" to={"/signup"}>Sign Up</Link>
</>
)}
</Container>
</Nav>
</div>
</Navbar>
<div className="container mt-4">
<Switch>
<Route exact path={["/", "/notes"]} render={(props) =>
<NotesList {...props} token={token} />
}>
</Route>
<Route path="/notes/create" render={(props)=>
<AddNote {...props} token={token} />
}>
</Route>
<Route path="/notes/:id/" render={(props)=>
<AddNote {...props} token={token} />
}>
</Route>
<Route path="/login" render={(props)=>
<Login {...props} login={login} />
}>
</Route>
<Route path="/signup" render={(props)=>
<Signup {...props} signup={signup} />
}>
</Route>
</Switch>
</div>
</div>
);
}
export default App;
