from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

@app.cli.command("reset-db")
def reset_db():
    from app import db
    import os

    db_path = os.path.join(app.instance_path, "verification.db")
    if os.path.exists(db_path):
        os.remove(db_path)
        print("✅ Database deleted.")
    db.create_all()
    print("✅ Database recreated.")
