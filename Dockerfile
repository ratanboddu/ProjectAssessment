FROM python:3

COPY . /myflask

WORKDIR /myflask

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

CMD [ "python", "./myflask.py" ]