import React, { Component } from 'react';
import Navvy from "./navbar";

import Requests from './requests';
import './input.css'


class Texter extends Component {
    constructor(props){
        super(props);
        this.state = {  
            value: '',
           encryptAPI: "https://safe-anchorage-46363.herokuapp.com/encrypt"+this.props.which+"?str=",
           decryptAPI: "https://safe-anchorage-46363.herokuapp.com/decrypt"+this.props.which+"?str="
    
    };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.encrypt = this.encrypt.bind(this);
    }
    handleChange(event) {
        this.setState({value: event.target.value});
        this.encrypt();
      }
    
      encrypt(){

      }
      handleSubmit(event) {
        alert('A name was submitted: ' + this.state.value);
        event.preventDefault();
      }

    render() { 
      const encryptAPI = 'http://localhost:5000/encrypt?str=';
      const decryptAPI ='http://localhost:5000/decrypt?str=';
        return ( 
        <div>
          

          <div className="centerr">
          <h1>{this.props.name}</h1>
          </div>

          <div className="container">
          
          <div className="row">
            <div className="col">
             <Requests value = {this.state.encryptAPI}/> 
             </div>

            <div className="col">
             <Requests value = {this.state.decryptAPI}/> 
             </div>
            </div>

             </div>
       {/* <Navvy />
        <div className="form-group ">
        <div className="row">
        <div className = "col green-border-focus">
    <label className="">Enter Here</label>
    <textarea className="form-control" id="exampleTextarea" rows="7" value={this.state.value} onChange={this.handleChange}></textarea>   
  </div>
       <Requests value = {this.state.value}/>     

  <div className = "col">
    <label className = "">Encrypted</label>
    <textarea className="form-control" id="exampleTextarea" rows="7" value={this.state.value} onChange={this.handleChange}></textarea>
  </div>
  </div>
  </div> */}
            
        </div>
         );
    }
}
 
export default Texter;