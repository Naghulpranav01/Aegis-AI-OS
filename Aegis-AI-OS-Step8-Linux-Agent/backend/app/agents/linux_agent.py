import subprocess

SAFE_COMMANDS={
    "pwd":["pwd"],
    "ls":["ls","-la"],
    "whoami":["whoami"],
    "disk":["df","-h"],
    "memory":["free","-h"],
    "cpu":["lscpu"]
}

def execute(action:str):
    if action not in SAFE_COMMANDS:
        return {"error":"Unsupported action"}
    result=subprocess.run(SAFE_COMMANDS[action],capture_output=True,text=True)
    return {"command":" ".join(SAFE_COMMANDS[action]),"output":result.stdout,"returncode":result.returncode}
