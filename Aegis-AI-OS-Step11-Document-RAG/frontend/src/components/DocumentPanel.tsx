import {useState} from "react";
import api from "../services/api";
export default function DocumentPanel(){
 const[path,setPath]=useState("");
 const[result,setResult]=useState<any>(null);
 async function run(){
  const r=await api.post("/documents/summarize",{path});
  setResult(r.data);
 }
 return <div>
 <h2>Document Intelligence</h2>
 <input value={path} onChange={e=>setPath(e.target.value)} placeholder="File path"/>
 <button onClick={run}>Summarize</button>
 <pre>{JSON.stringify(result,null,2)}</pre>
 </div>
}