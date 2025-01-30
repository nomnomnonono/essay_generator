from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def generate_essay():
    return {"essay": "This is an essay."}
