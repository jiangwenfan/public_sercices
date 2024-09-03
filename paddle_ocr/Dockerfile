FROM python:3.10-bullseye
WORKDIR /paddle

COPY ./img_en.jpg /paddle/image_en.jpg
COPY ./requirements.txt /paddle/requirements.txt

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN python3 -m pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
RUN pip install -r ./requirements.txt

RUN paddleocr --image_dir ./image_en.jpg --lang=en --use_gpu=False

# copy code
COPY ./consumer /paddle/consumer

# arm 不可用
CMD ["/bin/bash","/paddle/consumer/start.sh"]
