import {useState} from 'react';
import api from '../services/api';

export default function FileExplorer(){
 const[path,setPath]=useState(".");
 const[data,setData]=useState<any>(null);

 async function load(){
   const r=await api.post('/files/list',{path});
   setData(r.data);
 }

 return <div>
 <h2>File Explorer</h2>
 <input value={path} onChange={e=>setPath(e.target.value)} />
 <button onClick={load}>Browse</button>
 <pre>{JSON.stringify(data,null,2)}</pre>
 </div>;
}
