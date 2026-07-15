import {useState} from "react";
import api from "../services/api";
export default function BrowserPanel(){
 const[url,setUrl]=useState("https://example.com");
 const[result,setResult]=useState<any>(null);
 async function openSite(){
   const r=await api.post("/browser/open",{url});
   setResult(r.data);
 }
 return <div>
 <h2>Browser Agent</h2>
 <input value={url} onChange={e=>setUrl(e.target.value)} style={{width:"60%"}}/>
 <button onClick={openSite}>Open</button>
 <pre>{JSON.stringify(result,null,2)}</pre>
 </div>
}