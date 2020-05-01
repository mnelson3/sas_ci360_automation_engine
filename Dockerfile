FROM mnelson3/circus:rhel7_p36_build
LABEL maintainer="mnelson3@mail.depaul.edu"

ENV PYTHONUNBUFFERED=1

EXPOSE 8000:8000
EXPOSE 8080:8080
EXPOSE 443:443

RUN pip install --upgrade pip
#RUN pip install -e .

#WORKDIR /venv/Lib/site-packages

COPY setup.py /tmp/setup.py

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

#COPY requirements_win.txt requirements_win.txt
#RUN pip3 install -r requirements_win.txt

#COPY requirements_win_test.txt requirements_win_test.txt
#RUN pip3 install -r requirements_win_test.txt

COPY requirements_unix.txt /tmp/requirements_unix.txt
RUN pip3 install -r /tmp/requirements_unix.txt

COPY requirements_unix_test.txt /tmp/requirements_unix_test.txt
RUN pip3 install -r /tmp/requirements_unix_test.txt

COPY . /opt/app-root/lib/python3.6/site-packages

CMD "pytest"
ENV PYTHONDONTWRITEBYTECODE=true
