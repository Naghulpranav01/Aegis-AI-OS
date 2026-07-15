from fastapi import FastAPI
app=FastAPI(title="Aegis AI OS")
@app.get("/")
def root():
    return {"message":"Foundation ready"}
