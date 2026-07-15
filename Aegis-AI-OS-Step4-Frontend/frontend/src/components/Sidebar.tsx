import {Link} from 'react-router-dom';
export default function Sidebar(){
return(<aside style={{width:220,padding:20,borderRight:'1px solid #333',height:'100vh'}}>
<h2>Aegis AI</h2>
<nav style={{display:'flex',flexDirection:'column',gap:10}}>
<Link to='/'>Dashboard</Link>
<Link to='/chat'>AI Chat</Link>
<Link to='/settings'>Settings</Link>
</nav>
</aside>);
}