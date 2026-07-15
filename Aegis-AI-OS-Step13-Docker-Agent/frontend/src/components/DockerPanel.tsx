import {useState} from "react";
import api from "../services/api";

export default function DockerPanel(){
 const[out,setOut]=useState<any>(null);
 async function info(){const r=await api.get("/docker/info");setOut(r.data);}
 async function containers(){const r=await api.get("/docker/containers");setOut(r.data);}
 return <div>
 <h2>Docker Agent</h2>
 <button onClick={info}>Docker Info</button>
 <button onClick={containers}>Containers</button>
 <pre>{JSON.stringify(out,null,2)}</pre>
 </div>;
}