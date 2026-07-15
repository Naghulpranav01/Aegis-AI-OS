from app.database.memory_store import store

def save_memory(text:str):
    store.add(text)

def get_memories():
    return store.all()
