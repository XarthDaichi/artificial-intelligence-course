import React, {useState, useEffect, useReducer} from 'react';

const TypeAndSeeReducer = ({initialText='...'}) => {
    
   
    const [TYPED, SHOW] = ["TYPED", "SHOW"];
    
    const initialState = {toShowText:initialText, typedText:''};
    
    const reducer = (state, {type, value}) => {
        const {toShowText, typedText} = state;
        switch (type){
            case TYPED: if (typedText == value) return state;
                        return {...state, typedText: value}
            case SHOW:  return {...state, toShowText: value}
            
            default: {console.log(`reducer default ${type.toString()}`); return state;}
        }
    };
    const [{toShowText, typedText}, dispatch] = useReducer(reducer, initialState);
    
    const onChangeHandler = ({target:{value} }) => {
        console.log(`onChangeHandler: ${value}`);
        dispatch({type:TYPED, value});
        dispatch({type:SHOW, value});
    };
    useEffect(() => {
        if (!typedText)
            dispatch({type:SHOW, value:initialText});
    }, [typedText]);
    
    const style = {marginLeft:'30%', width:'20%', backgroundColor:'lightblue'};
    return (
          <div style={style}>
            <h4 style={{color:"blue"}}>{toShowText}</h4>
            <input type="text" value={typedText} onChange={onChangeHandler}/>
          </div>
    );
};

export default TypeAndSeeReducer;