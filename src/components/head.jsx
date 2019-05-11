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
        three: '3',
        name: 'Brutus: (Caesar Cypher)',
        name2: 'Anna: (Reverse Encryption)',
        name3: 'Phil: (Custom Encryption)',
        name4: 'Steve-o: (Special Encryption)',
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
            <Texter which = {this.state.two} name = {this.state.name3} />
            <Texter which = {this.state.three} name = {this.state.name4} />
            
            
            </div>

         );
    }
}
 
export default Complete;