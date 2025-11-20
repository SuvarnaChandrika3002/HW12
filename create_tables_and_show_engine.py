from importlib import import_module
import traceback
print("Running create_tables_and_show_engine.py")

try:
    try:
        mod = import_module("app.database")
        engine = getattr(mod, "engine")
        Base = getattr(mod, "Base", None)
        if Base is None:
            mod2 = import_module("app.models")
            Base = getattr(mod2, "Base")
        print("Using engine from app.database")
    except Exception:
        from app.database import engine
        from app.models import Base
        print("Fallback: imported engine from app.database and Base from app.models")

    print("Engine URL:", getattr(engine, "url", str(engine)))
    print("Creating tables (Base.metadata.create_all)...")
    Base.metadata.create_all(bind=engine)
    print("Done: created tables")
    from sqlalchemy import inspect
    inspector = inspect(engine)
    print("Tables now in DB:", inspector.get_table_names())

except Exception as e:
    print(">>> Exception occurred while creating tables:")
    traceback.print_exc()
    raise
