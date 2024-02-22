from fastapi import FastAPI
from endpoints import test, func

app = FastAPI(
    title="Intern-Code-Test",
    description="API description",
    version="0.1.0",
    docs_url="/docs",
)

app.include_router(test.router, prefix="/test", tags = ["test"])
app.include_router(func.router, prefix="/func", tags = ["func"])
  