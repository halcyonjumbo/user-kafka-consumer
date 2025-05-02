from fastapi import FastAPI
from controller.api_log_controller import router as api_log_router
import uvicorn
app = FastAPI()

app.include_router(api_log_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)