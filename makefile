python:
	python3 -B main.py

docker:
	docker build -t wrd .

rd:
	docker run -it --rm wrd