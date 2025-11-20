import traceback

created = False
errors = []
tries = [
    ("app.database", "engine, Base"),
    ("app.models", "Base (uses engine from app.database)"),
]

for modname, note in tries:
    try:
        print(f"Trying: {modname} -> {note}")
        if modname == "app.database":
            from app.database import engine, Base
            Base.metadata.create_all(bind=engine)
            print("Created tables using app.database.Base")
        else:
            from app.database import engine
            from app.models import Base
            Base.metadata.create_all(bind=engine)
            print("Created tables using app.models.Base (engine from app.database)")
        created = True
        break
    except Exception as e:
        errors.append((modname, traceback.format_exc()))
        print(f"Attempt {modname} failed, continuing...")

if not created:
    print("\nAll attempts failed. Errors:")
    for name, tb in errors:
        print("----", name, "----")
        print(tb)
    raise SystemExit("Failed to create tables automatically. Paste the above errors here and I'll give exact guidance.")
