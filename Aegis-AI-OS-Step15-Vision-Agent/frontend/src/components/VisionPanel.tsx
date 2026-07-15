import {useState} from "react";
import api from "../services/api";

export default function VisionPanel(){
 const[path,setPath]=useState("");
 const[result,setResult]=useState<any>(null);
 async function run(){
   const r=await api.post("/vision/analyze",{path});
   setResult(r.data);
 }
 return <div>
 <h2>Vision Agent</h2>
 <input value={path} onChange={e=>setPath(e.target.value)} placeholder="Image path"/>
 <button onClick={run}>Analyze</button>
 <pre>{JSON.stringify(result,null,2)}</pre>
 </div>;
}