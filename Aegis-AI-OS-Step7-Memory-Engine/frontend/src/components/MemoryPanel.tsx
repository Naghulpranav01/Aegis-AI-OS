import {useEffect,useState} from "react";
import api from "../services/api";

export default function MemoryPanel(){
 const[mem,setMem]=useState<any[]>([]);
 const[text,setText]=useState("");
 async function load(){const r=await api.get("/memory/");setMem(r.data.memories);}
 async function save(){await api.post("/memory/",{text});setText("");load();}
 useEffect(()=>{load();},[]);
 return <div>
 <h2>Memory</h2>
 <input value={text} onChange={e=>setText(e.target.value)} />
 <button onClick={save}>Save</button>
 <ul>{mem.map((m,i)=><li key={i}>{m.text}</li>)}</ul>
 </div>
}