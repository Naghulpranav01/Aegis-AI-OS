from pathlib import Path

def list_directory(path:str="."):
    p=Path(path).expanduser().resolve()
    if not p.exists() or not p.is_dir():
        return {"error":"Directory not found"}
    items=[]
    for f in p.iterdir():
        items.append({
            "name":f.name,
            "type":"directory" if f.is_dir() else "file",
            "size":f.stat().st_size
        })
    return {"path":str(p),"items":items}

def read_text_file(path:str):
    p=Path(path).expanduser().resolve()
    if not p.exists() or not p.is_file():
        return {"error":"File not found"}
    try:
        return {"path":str(p),"content":p.read_text(errors="ignore")}
    except Exception as e:
        return {"error":str(e)}
