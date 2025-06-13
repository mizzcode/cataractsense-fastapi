from fastapi import FastAPI
from app.db.database import engine
from app.routes.predict import router as predict_router
from app.routes.prediction_log import router as log_router
from app.models import models  # Ini hanya agar model terbaca
from app.routes import feedback
from app.routes import prediction_crud
from app.routes import auth
from app.routes.feedback_route import router as feedback_router
from app.routes.admin_route import router as admin_router


print("📦 Membuat database dan tabel...")
models.Base.metadata.create_all(bind=engine)
print("✅ Database & tabel siap.")

app = FastAPI()

# Include routers
app.include_router(predict_router)
app.include_router(log_router)
app.include_router(feedback.router)
app.include_router(prediction_crud.router)
app.include_router(auth.router)
app.include_router(feedback_router)
app.include_router(admin_router)

@app.get("/")
def root():
    return {"message": "API Backend CataractSense aktif"}
