FROM evans2jiang/whisper-base:latest

WORKDIR /whisper
# install python dependency
COPY ./requirments.txt /whisper/requirments.txt
RUN pip install -r requirments.txt  -i https://mirrors.cloud.tencent.com/pypi/simple

# copy code
COPY ./consumer /whisper/consumer

CMD ["/bin/bash","/whisper/consumer/start.sh"]
