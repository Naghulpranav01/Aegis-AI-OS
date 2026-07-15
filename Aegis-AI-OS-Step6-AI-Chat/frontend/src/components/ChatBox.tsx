import {useState} from 'react';
import api from '../services/api';

export default function ChatBox(){
 const[msg,setMsg]=useState('');
 const[reply,setReply]=useState('');
 async function send(){
   const r=await api.post('/chat/',{message:msg});
   setReply(r.data.response);
 }
 return(<div>
 <textarea value={msg} onChange={e=>setMsg(e.target.value)}/>
 <button onClick={send}>Send</button>
 <pre>{reply}</pre>
 </div>);
}