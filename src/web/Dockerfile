# syntax=docker/dockerfile:1
FROM python:3.7-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=karsts.settings.docker

RUN python -m pip install --upgrade pip

WORKDIR /opt/app/
COPY requirements.txt ./requirements.txt
RUN python -m pip install -r requirements.txt

COPY . .
