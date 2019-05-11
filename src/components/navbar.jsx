import React, { Component } from 'react';
import Navbar from 'react-bootstrap/Navbar';
//import logo from './logo.svg';
import './navbar.css';

const navStyle = {
    backgroundColor: 'rgba(52,52,52,.5)'
} 

class Navvy extends Component {
    
    render() { 
        return ( 
            <div>
               
             <nav className="navbar navbar-expand-lg navbar-dark" style={navStyle}>

            <a className="navbar-brand" href="#"> 
            <img src='./shield.svg' width="30" height="30" class="d-inline-block align-top" alt=""></img>
    
             N_n_N   </a>
            </nav>
            </div>
                

         );
    }
}
 
export default Navvy;