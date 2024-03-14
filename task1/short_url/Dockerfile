FROM python:3.11
ENV PYTHONUNBUFFERED 1
RUN mkdir /short_url
WORKDIR /short_url
COPY requirements.txt /short_url
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /short_url 