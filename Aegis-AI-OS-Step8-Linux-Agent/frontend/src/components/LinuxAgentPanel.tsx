import {useState} from 'react';
import api from '../services/api';

export default function LinuxAgentPanel(){
 const[action,setAction]=useState('pwd');
 const[out,setOut]=useState('');
 async function run(){
   const r=await api.post('/linux/',{action});
   setOut(JSON.stringify(r.data,null,2));
 }
 return <div>
 <h2>Linux Agent</h2>
 <select value={action} onChange={e=>setAction(e.target.value)}>
 <option>pwd</option>
 <option>ls</option>
 <option>whoami</option>
 <option>disk</option>
 <option>memory</option>
 <option>cpu</option>
 </select>
 <button onClick={run}>Execute</button>
 <pre>{out}</pre>
 </div>
}
