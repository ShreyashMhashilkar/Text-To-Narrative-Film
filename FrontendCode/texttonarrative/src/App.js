import './App.css';
import React, {useState} from 'react'
// import Axios from 'axios'

function App() {
  const [name,setName]=useState("")

  function sendData(){
    console.warn(name)
    let data={name}
    fetch("http://127.0.0.1:8000/send_text",{
      method:'POST',
      headers:{
        'Accept':'application/json',
        'Content-Type':'application/json'
      },
      body:JSON.stringify(data)
    }).then((result)=>{
      
      console.warn("result",result);

    })
  }

  // useEffect(()=>{
  //   sendData();

  // },[])

  return (
    <div className="App">

      <h1>TEXT TO NARRATIVE FILMS</h1><br/>
      
      <div class="input-group">
      <span class="input-group-text">Enter the sentences</span><br/><br/>
      <input type="text" value={name} onChange={(e)=>{setName(e.target.value)}} name="name" class="form-control"></input></div>
      <br/><br/>
      <button type="button" onClick={sendData} class="btn btn-warning">Submit</button>
      
    </div>
  );
}

export default App;
