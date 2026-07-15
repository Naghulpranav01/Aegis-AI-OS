import {Routes,Route} from 'react-router-dom';
import Sidebar from './components/Sidebar';
import Dashboard from './pages/Dashboard';
import Chat from './pages/Chat';
import Settings from './pages/Settings';
export default function App(){
return(<div style={{display:'flex'}}>
<Sidebar/>
<div style={{padding:'20px',flex:1}}>
<Routes>
<Route path='/' element={<Dashboard/>}/>
<Route path='/chat' element={<Chat/>}/>
<Route path='/settings' element={<Settings/>}/>
</Routes>
</div>
</div>);
}