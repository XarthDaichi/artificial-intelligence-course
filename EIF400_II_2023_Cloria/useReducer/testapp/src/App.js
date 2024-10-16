import logo from './logo.svg';
import './App.css';
import Counter from './Counter.js';
import TypeAndSee from './TypeAndSee.js';
import TypeAndSeeReducer from './TypeAndSeeReducer.js';

function App() {
  return (
    <div className="App">
      <Counter init={666}/>
      <TypeAndSee initialText='......'/>
      <TypeAndSeeReducer initialText='----'/>
    </div>
  );
}

export default App;
