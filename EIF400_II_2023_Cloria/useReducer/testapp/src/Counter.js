import React, {useState} from 'react';

const Counter = ({init}) => {
    const [counter, setCounter] = useState(init);
    
    const INCREASE = "Increase";
    const DECREASE = "Decrease";
    const [direction, setDirection] = useState(INCREASE);
    
    const clickHandler = () => {
        console.log(`clickHandler: Before ${counter}`);
        setCounter(counter + (direction == INCREASE ? 1 : -1) );
        console.log(`clickHandler: After ${counter}`);
    };
    const keyDownHandler = e => {
        if (e.key === "Escape"){
           setDirection(direction == INCREASE ? DECREASE : INCREASE)
        }
    };
    
    const divStyle = {backgroundColor:'lightgreen', 
                    width:'20%', 
                    marginLeft:'30%', 
                    borderRadius:'15px'
                    };
                    
    return   ( <div style={divStyle}>
                <h2>{counter}</h2>
                <button
                   onClick={clickHandler}
                   onKeyDown={keyDownHandler}
                   
                >
                {direction}
               </button>
              </div>);
}
export default Counter;