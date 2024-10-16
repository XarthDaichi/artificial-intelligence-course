import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';
import TextArea from './components/TextArea';

function App() {
    
  const [showKeywords, setShowKeywords] = useState(false);
  const [keywords, setKeywords] = useState([]);
  const [selectedKeyword, setSelectedKeyword] = useState('');
  
  // Use server to populate the list of keywords
  // For demo purposes, a static list is used.
  const keyWordsList = ['for', 'while', 'if', 'try', 'from', 'forEach', 'then']
  
  const handleEscapePress = () => {
    setShowKeywords(true); // make ListOfKeywords visible
   
    setKeywords(keyWordsList);
  };

  const handleKeywordSelect = () => {
    setShowKeywords(false); // make ListOfKeywords invisible
  };

  return (
    <div className="App">
      <h1>Select Popup Demo</h1>
      <TextArea
        keywords={keywords}
        onEscapePress={handleEscapePress}
        onKeywordSelect={handleKeywordSelect}
      />
    </div>
  );
}

export default App;
