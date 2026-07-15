import {useEffect,useState} from "react";
import api from "../services/api";
export default function PluginPanel(){
 const[data,setData]=useState<any[]>([]);
 useEffect(()=>{api.get("/plugins/").then(r=>setData(r.data.plugins));},[]);
 return <div>
 <h2>Plugin Manager</h2>
 <ul>{data.map((p:any,i:number)=><li key={i}>{p.name} - {p.version}</li>)}</ul>
 </div>;
}