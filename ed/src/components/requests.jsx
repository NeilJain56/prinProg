import React, { Component } from 'react';
import $ from 'jquery';
class Requests extends Component {

    constructor(){
        super();
       
}
   
    getPythonHello() {

       $.ajax({
            url: "../pythonServer/try.py",
            success: function(response){
                console.log(response)
            }
       });
   
    }

    

    render() { 
        
        return ( 

            <div>
                <button id="theButton" onClick={this.getPythonHello}>Submit</button>


            </div>
         );
    }
}
 
export default Requests;