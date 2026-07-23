from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/ip")
def get_ip(request: Request):
    forwarded_for = request.headers.get("x-forwarded-for")
    client_ip = forwarded_for.split(",")[0].strip() if forwarded_for else request.client.host
    return {"ip": client_ip}
