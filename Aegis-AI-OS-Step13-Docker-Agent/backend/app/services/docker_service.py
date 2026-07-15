import subprocess

def docker_info():
    try:
        r=subprocess.run(["docker","info"],capture_output=True,text=True,timeout=15)
        return {"success":r.returncode==0,"output":r.stdout if r.returncode==0 else r.stderr}
    except Exception as e:
        return {"success":False,"error":str(e)}

def list_containers():
    try:
        r=subprocess.run(["docker","ps","-a"],capture_output=True,text=True,timeout=15)
        return {"containers":r.stdout}
    except Exception as e:
        return {"error":str(e)}
