import React, { Component } from 'react';
import $ from 'jquery';
import axios from 'axios';

class Requests extends Component {

    constructor(){
        super();
        this.state = {
            encryptedString: 'ff'
        }
        this.getPythonHello = this.getPythonHello.bind(this);
}
   
    getPythonHello() {
        console.log("Function called ")
        axios.get('http://localhost:5000/encrypt?str=ENCRYPT-ME33CORS')
            .then(response => this.setState({encryptedString : response.data}))
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
                <button id="theButton" onClick={this.getPythonHello}>Submit</button>
                    <p> eNCRYPTED String is {this.state.encryptedString}</p>
            </div>
         );
    }
}
 
export default Requests;