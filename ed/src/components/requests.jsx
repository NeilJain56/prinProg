import React, { Component } from 'react';
import $ from 'jquery';
import axios from 'axios';
import Navvy from "./navbar";

class Requests extends Component {

    constructor(){
        super();
        this.state = {
            encryptedString: 'ff',
            requestValue: '',
            resultValue: '',
        }
        this.handleChange = this.handleChange.bind(this);
        this.getPythonHello = this.getPythonHello.bind(this);
}


handleChange(event) {
    this.setState({requestValue: event.target.value});
    
  }
   
    getPythonHello() {
        console.log(this.props)
        console.log("Function called this.state.requestValue ", this.state.requestValue)
        console.log("Function called this.state.resultValue ", this.state.resultValue)
        axios.get('http://localhost:5000/encrypt?str='+this.state.requestValue)
            .then(response => this.setState({resultValue : response.data}))
            .then(response => console.log(response.data))
            .catch(response => console.log("Can’t access  response. Blocked by browser?", response))

    //    $.ajax({
    //         url: "../pythonServer/try.py",
    //         success: function(response){
    //             console.log(response)
    //         }
    //    });
    console.log("Function called ENDED ")
    }

    

    render() { 
        
        return ( 
            <div>
            <div>
                <button id="theButton" onClick={this.getPythonHello}>Submit</button>
                    <p> eNCRYPTED String is {this.state.encryptedString}</p>
            </div>
                    <div className = "col green-border-focus">
                    <label className="">Enter Here</label>
                    <textarea className="form-control" id="exampleTextarea" rows="7" value={this.state.requestValue} onChange={this.handleChange}></textarea>   
                  </div>
                  <div className = "col green-border-focus">
                    <label className="">Enter Here</label>
                    <textarea className="form-control" id="exampleTextarea" rows="7" value={this.state.resultValue} ></textarea>   
                  </div>
                  </div>
         );
    }
}
 
export default Requests;