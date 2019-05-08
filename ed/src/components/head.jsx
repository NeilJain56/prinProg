import React, { Component } from 'react';
import Texter from "./Input";
import Navvy from "./navbar"
import {Scrollbars} from 'react-custom-scrollbars';
import LoadingScreen from 'react-loading-screen';

class Complete extends Component {
    state = { 
        which: '',
        none: '',
        one: '1',
        two: '2',
        name: 'Caesar Cypher',
        name2: 'Normal Encryption',
        bool: true,
        counter: 0
     }
     
     changeBool(){
         
         if(this.state.counter < 1){
        this.setState({bool: false});
         }
         else{
             this.setState({counter: 1});
         }
        
     }
     
    render() { 
        return ( 
            <div>
                
          
  
                <Navvy />
            <Texter which = {this.state.none} name = {this.state.name}/>
            <Texter which = {this.state.one} name = {this.state.name2} />
            
            </div>

         );
    }
}
 
export default Complete;