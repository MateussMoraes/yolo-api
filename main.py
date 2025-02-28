from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return { "Mensagem": "Olá mundo"}


# Método Main

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port="8080",
        log_level="info"
    )