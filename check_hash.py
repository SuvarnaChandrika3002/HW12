import inspect, importlib, sys

print("PYTHON EXE:", sys.executable)
try:
    import passlib, bcrypt
    print("passlib:", passlib.__version__)
    print("bcrypt:", bcrypt.__version__)
except Exception as e:
    print("error importing passlib/bcrypt:", e)

try:
    sec = importlib.import_module("app.security")
    print("\n--- app/security.py ---")
    print(inspect.getsource(sec))
except Exception as e:
    print("error importing app.security:", e)

try:
    crud = importlib.import_module("app.crud")
    print("\n--- app/crud.py ---")
    print(inspect.getsource(crud))
except Exception as e:
    print("error importing app.crud:", e)


try:
    print("\n--- hashing test ---")
    h = sec.hash_password('x'*200)
    print("hashed ok, len:", len(h))
    print("verify:", sec.verify_password('x'*200, h))
except Exception as e:
    import traceback
    print("hashing error:", type(e).__name__, e)
    traceback.print_exc()
