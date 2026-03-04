from fastapi import FastAPI, Request
import httpx

app = FastAPI(title="API Gateway")

AUTH_SERVICE = "http://auth-service:8001"
TASK_SERVICE = "http://task-service:8002"

@app.api_route("/auth/{path:path}", methods=["GET","POST"])
async def auth_proxy(path: str, request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.request(
            request.method,
            f"{AUTH_SERVICE}/{path}",
            content=await request.body(),
            headers=request.headers
        )
        return response.json()

@app.api_route("/tasks/{path:path}", methods=["GET","POST"])
async def task_proxy(path: str, request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.request(
            request.method,
            f"{TASK_SERVICE}/{path}",
            content=await request.body(),
            headers=request.headers
        )
        return response.json()
