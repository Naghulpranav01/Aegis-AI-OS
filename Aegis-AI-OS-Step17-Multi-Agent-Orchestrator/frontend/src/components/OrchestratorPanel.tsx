import {useState} from "react";
import api from "../services/api";
export default function OrchestratorPanel(){
 const[task,setTask]=useState("");
 const[result,setResult]=useState<any>(null);
 async function dispatch(){
   const r=await api.post("/orchestrator/dispatch",{task});
   setResult(r.data);
 }
 return <div>
 <h2>Multi-Agent Orchestrator</h2>
 <input value={task} onChange={e=>setTask(e.target.value)} placeholder="e.g. Open Docker logs"/>
 <button onClick={dispatch}>Route Task</button>
 <pre>{JSON.stringify(result,null,2)}</pre>
 </div>;
}