# az webapp config set --resource-group rgtest --name rlapp13 --startup-file app.py
uvicorn --bind=0.0.0.0 --timeout 600 --port 8080 app.main:app
