import React, { Component } from 'react';
import Navbar from 'react-bootstrap/Navbar';
//import logo from './logo.svg';
class Navvy extends Component {
    
    render() { 
        return ( 
            <div>
             <Navbar bg="light">

                <Navbar.Brand href="#home">
                <img
        src="./logo.svg"
        width="30"
        height="30"
        className="d-inline-block align-top"
        alt=""
      />
                
                NnN Encoder
                </Navbar.Brand>
            </Navbar>
                </div>

         );
    }
}
 
export default Navvy;