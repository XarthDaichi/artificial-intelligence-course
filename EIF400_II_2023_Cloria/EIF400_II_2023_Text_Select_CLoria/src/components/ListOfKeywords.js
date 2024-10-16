import React from 'react';

const ListOfKeywords = ({ keywords, onSelect }) => {
  console.log("ListOfKeywords", keywords.toString())
  keywords = ["Select", ...keywords];
  return (
    <select 
       value={keywords[0]}
       onChange={e => {console.log("ListOfKeywords onchange", e.target.value);return onSelect(e.target.value)}}
    >
      {keywords.map(keyword => (
        <option key={keyword} value={keyword}>
          {keyword}
        </option>
      ))}
    </select>
  );
};

export default ListOfKeywords;
