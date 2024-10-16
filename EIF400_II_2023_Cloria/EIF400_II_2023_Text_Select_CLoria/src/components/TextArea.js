import React, { useState, useRef } from 'react';
import ListOfKeywords from './ListOfKeywords';

const TextArea = ({ keywords, onEscapePress, onKeywordSelect }) => {
    
  const [text, setText] = useState('');
  const [selectedText, setSelectedText] = useState('');
  const [shouldListAppear, setShouldListAppear] = useState(false);
  const textareaRef = useRef(null);

  const handleKeyDown = (e) => {
    if (e.key === 'Escape') {
      if (shouldListAppear) {
        // Close the list if it's already open and Escape is pressed again
        setSelectedText("");
        setShouldListAppear(false);
      } else {
        // Show the list and prevent default Escape behavior
        setShouldListAppear(true);
        const textArea = textareaRef.current;
        const start = textArea.selectionStart;
        const end = textArea.selectionEnd;
        setSelectedText(text.substring(start, end));
        console.log("handleKeyDown->", text.substring(start, end), selectedText);
        
        onEscapePress();
      }
    }
  };
  
  const handleKeywordSelect = (keyword) => {
    console.log("handleKeywordSelect: keyword", keyword);
    const textArea = textareaRef.current;
    const start = textArea.selectionStart;
    const end = textArea.selectionEnd;
    const newText = text.substring(0, start) + keyword + text.substring(end);
    console.log("handleKeywordSelect: newText", newText);
    setText(newText);
    setShouldListAppear(false);
    onKeywordSelect();
  };

  const handleFocus = () => {
    if (shouldListAppear) {
      setShouldListAppear(true);
    }
  };

  const candidateKeywords = keywords.filter(key => key.startsWith(selectedText)).toSorted();

  return (
    <div>
      <textarea
        ref={textareaRef}
        value={text}
        onChange={ e => setText(e.target.value)}
        onKeyDown={handleKeyDown}
        
      />
      {shouldListAppear && candidateKeywords.length > 0 && (
        <ListOfKeywords
          keywords={candidateKeywords}
          onSelect={handleKeywordSelect}
          onFocus={handleFocus}
        />
      )}
    </div>
  );
};

export default TextArea;