import React, {useState, useEffect} from 'react';

const TypeAndSee = ({initialText='...'}) => {
    
    const [toShowText, setText] = useState(initialText);
    const [typedText, setTypedText] = useState('');
    
    const onChangeHandler = ({target:{value} }) => {
        setText(value);
        setTypedText(value);
    };
    useEffect(() => {
        if (!typedText)
            setText(initialText);
    }, [typedText]);
    
    const style = {marginLeft:'30%', width:'20%', backgroundColor:'lightblue'};
    return (
          <div style={style}>
            <h4 style={{color:"red"}}>{toShowText}</h4>
            <input type="text" value={typedText} onChange={onChangeHandler}/>
          </div>
    );
};

export default TypeAndSee;