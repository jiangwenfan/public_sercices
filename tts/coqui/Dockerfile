FROM python:3.9-buster
WORKDIR /coqui

RUN mkdir data

# install system dependency
RUN apt update && apt-get install espeak -y

# install python dependency
COPY ./requirements.txt /coqui/requirements.txt
RUN pip install -r /coqui/requirements.txt -i https://mirrors.cloud.tencent.com/pypi/simple

# download model
RUN tts --text "This is my text." --out_path a.wav

# copy code
COPY ./consumer /coqui/consumer

# arm 不可用
CMD ["/bin/bash","/coqui/consumer/start.sh"]
