from fastapi import FastAPI
import pkgutil
import importlib
import inspect
from app.database import engine, Base

app = FastAPI(title="Calc API (auto-discover routes)")

Base.metadata.create_all(bind=engine)

import app.routes as routes_pkg

for finder, name, ispkg in pkgutil.iter_modules(routes_pkg.__path__):
    module_name = f"{routes_pkg.__name__}.{name}"
    try:
        module = importlib.import_module(module_name)
    except Exception:
        raise
    router = getattr(module, "router", None)
    if router is not None:
        app.include_router(router)

@app.get("/")
def root():
    return {"ok": True}
