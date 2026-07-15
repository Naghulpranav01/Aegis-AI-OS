import {useState} from "react";
import api from "../services/api";

export default function VoicePanel(){
 const[text,setText]=useState("");
 const[result,setResult]=useState<any>(null);

 async function listen(){
   const r=await api.get("/voice/listen");
   setResult(r.data);
 }

 async function speak(){
   const r=await api.post("/voice/speak",{text});
   setResult(r.data);
 }

 return <div>
 <h2>Voice Assistant</h2>
 <button onClick={listen}>Listen (Placeholder)</button>
 <br/><br/>
 <input value={text} onChange={e=>setText(e.target.value)} placeholder="Text to speak"/>
 <button onClick={speak}>Speak</button>
 <pre>{JSON.stringify(result,null,2)}</pre>
 </div>;
}