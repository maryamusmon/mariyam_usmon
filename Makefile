mig:
	python3 manage.py makemigrations
	python3 manage.py migrate


admin:
	python3 manage.py createsuperuser --username admin --email admin@mail.com


run:
	python3 manage.py runserver