import {useState} from 'react';
import api from '../services/api';

export default function TerminalPanel(){
 const[cmd,setCmd]=useState('pwd');
 const[out,setOut]=useState('');
 async function run(){
   const r=await api.post('/terminal/',{command:cmd});
   setOut(JSON.stringify(r.data,null,2));
 }
 return (
 <div>
  <h2>Terminal Agent</h2>
  <select value={cmd} onChange={e=>setCmd(e.target.value)}>
    <option>pwd</option>
    <option>ls</option>
    <option>whoami</option>
    <option>date</option>
    <option>uptime</option>
  </select>
  <button onClick={run}>Run</button>
  <pre>{out}</pre>
 </div>);
}
