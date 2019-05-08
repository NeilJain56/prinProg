import React, { Component } from 'react';
import $ from 'jquery';
import axios from 'axios';
import Navvy from "./navbar";
import './requests.css';

class Requests extends Component {

    constructor(){
        super();
        this.state = {
            encryptedString: 'ff',
            requestValue: '',
            resultValue: ''
        }
        this.handleChange = this.handleChange.bind(this);
        this.getPythonHello = this.getPythonHello.bind(this);
}


handleChange(event) {
    this.setState({requestValue: event.target.value});
    this.getPythonHello();
    this.forceUpdate();
    
  }
   
    getPythonHello() {
        
        console.log("Function called this.state.requestValue ", this.state.requestValue)
        
        axios.get(this.props.value+this.state.requestValue)
            .then(response => this.setState({resultValue : response.data}))
            //.then(response => console.log(response.data))
            .catch(response => console.log("Can’t access  response. Blocked by browser?", response))

    //    $.ajax({
    //         url: "../pythonServer/try.py",
    //         success: function(response){
    //             console.log(response)
    //         }
    //    });
    console.log("Function called this.state.resultValue ", this.state.resultValue)
    console.log("Function called ENDED ")
    
    }

    

    render() { 
        
        return ( 
            <div>
                <div className="container" id="fonter">
            
                </div>
                    <div className = "col">
                        
                    <div className="bye">
                    <label className="hi" id="fonter">Enter Here</label>
                    </div>
                    <div className="">
                    <textarea className="form-control" id="transper" rows="7" value={this.state.requestValue} onChange={this.handleChange}></textarea> 
                    </div>  
                  </div>
                  <div className = "col">
                  <div className="bye">
                    <label className="hi" id="fonter">Output</label>
                    </div>
                    <textarea className="form-control" id="transper" rows="7" value={this.state.resultValue} ></textarea>   
                  </div>
                  </div>
         );
    }
}
 
export default Requests;