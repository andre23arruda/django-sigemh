.ONESHELL:
SHELL=/bin/bash

ifeq ($(OS),Windows_NT)
    VENV_PATH := ./venv/Scripts
else
    VENV_PATH := ./venv/bin
endif

install:
	conda create --prefix ./venv python=3.10
	$(VENV_PATH)/pip install -r requirements.txt
	cp setup/config/env_example.py  setup/config/env.py
	@echo ">>> Add correct values to setup/config/env.py"

migrate:
	$(VENV_PATH)/python ./manage.py migrate

migrations:
	$(VENV_PATH)/python ./manage.py makemigrations

pip:
	$(VENV_PATH)/pip install $(package)
	$(VENV_PATH)/pip freeze | grep -i $(package) >> requirements.txt

run:
	$(VENV_PATH)/python ./manage.py runserver

superuser:
	$(VENV_PATH)/python ./manage.py createsuperuser