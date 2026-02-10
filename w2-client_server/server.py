from fastapi import FastAPI
import time

app = FastAPI()

items = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"]

# endpoint root
@app.get("/")
def home():
    return {"message": "Server aktif"}

# ambil semua item
@app.get("/items")
def get_items():
    return {"items": items}

# tmbah item
@app.post("/items/{name}")
def add_item(name: str):
    items.append(name)
    return {"message": f"Item '{name}' berhasil ditambahkan."}

# hapus item
@app.delete("/items/{idx}")
def delete_item(idx: int):
    if idx < len(items):
        deleted = items.pop(idx)
        return {"message": f"Item '{deleted}' berhasil dihapus."}
    return {"error": "Index tidak ada."}

# simulasi proses lama (untuk uji concurrency)
@app.get("/slow/{id}")
def slow_process(id: int):
    print(f"Client {id} mulai diproses.")
    time.sleep(3)
    print(f"Client {id} selesai.")
    return {"client": id, "status": f"Proses {id} selesai."}