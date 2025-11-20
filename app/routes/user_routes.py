@router.post("/register", response_model=UserRead)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(
        (User.username == user.username) |
        (User.email == user.email)
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Username or email already exists.")

    hashed = hash_password(user.password)

    db_user = User(
        username=user.username,
        email=user.email,
        password_hash=hashed,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
