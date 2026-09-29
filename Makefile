setup:
	python3.10 -m venv .venv      
	source .venv/bin/activate  
	pip install -r requirements.txt

login-db:
	psql -h localhost -p 5432 -U admin -d authentication

run:
	uvicorn main:app --reload   