import subprocess

ALLOWED={
    "pwd":"pwd",
    "ls":"ls -la",
    "whoami":"whoami",
    "date":"date",
    "uptime":"uptime"
}

def execute(alias:str):
    if alias not in ALLOWED:
        return {"error":"Command not allowed"}
    cmd=ALLOWED[alias]
    result=subprocess.run(cmd,shell=True,capture_output=True,text=True)
    return {
        "command":cmd,
        "stdout":result.stdout,
        "stderr":result.stderr,
        "returncode":result.returncode
    }
