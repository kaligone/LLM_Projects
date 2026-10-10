import uvicorn
from fastapi import FastAPI

app = FastAPI(title='Fast api demo')

@app.get("/")
def test():
    return {"status":"green"}

def main():
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    main()
