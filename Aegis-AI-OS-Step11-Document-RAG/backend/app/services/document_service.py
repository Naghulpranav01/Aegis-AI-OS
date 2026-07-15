from pathlib import Path

def summarize(path:str):
    p=Path(path)
    if not p.exists():
        return {"error":"File not found"}
    text=p.read_text(errors="ignore")[:4000]
    return {"summary":"Placeholder summary. Integrate Qwen/RAG later.","preview":text[:500]}
