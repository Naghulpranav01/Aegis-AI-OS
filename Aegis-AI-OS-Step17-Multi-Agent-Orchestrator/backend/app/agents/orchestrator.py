class Orchestrator:
    def __init__(self):
        self.agents={
            "linux":"Linux Agent",
            "files":"File Agent",
            "terminal":"Terminal Agent",
            "documents":"Document Agent",
            "browser":"Browser Agent",
            "docker":"Docker Agent",
            "voice":"Voice Agent",
            "vision":"Vision Agent",
            "memory":"Memory Agent"
        }

    def dispatch(self,task:str):
        t=task.lower()
        if "docker" in t: agent="docker"
        elif "file" in t or "folder" in t: agent="files"
        elif "terminal" in t or "command" in t: agent="terminal"
        elif "browser" in t or "website" in t: agent="browser"
        elif "document" in t or "pdf" in t: agent="documents"
        elif "voice" in t: agent="voice"
        elif "vision" in t or "image" in t: agent="vision"
        elif "memory" in t: agent="memory"
        else: agent="linux"
        return {
            "selected_agent":agent,
            "agent_name":self.agents[agent],
            "status":"ready",
            "message":"Routing complete. Integrate tool-calling in later milestone."
        }

orchestrator=Orchestrator()
