# VENV 
Activate with: .venv\Scripts\activate

# install libraries
uv pip install fastapi pydentic uvicorn

# requirements.txt
uv pip freeze > requirements.txt


# Add config for system independent execution
In project folder --> uv add <libraries>