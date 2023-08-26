FROM nvcr.io/nvidia/pytorch:23.06-py3

# set environment variables
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV TERM screen-256color
ENV PYTHONBREAKPOINT=ipdb.set_trace
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TOKENIZERS_PARALLELISM=false

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y
COPY requirements.txt /workspace/requirements.txt

# install extra python packages
RUN python -m pip install --upgrade pip
RUN pip install -r /workspace/requirements.txt
# RUN jupyter nbextension enable --py widgetsnbextension

# install personal ml package
COPY blazingai /workspace/blazingai
RUN pip install -e /workspace/blazingai

########################################
## dependencies for dev environment
## TODO: move to devcontainer
########################################
RUN apt-get install -y npm
RUN apt-get install -y nodejs

RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:neovim-ppa/unstable
RUN apt-get update
RUN apt-get install -y neovim 
RUN pip install pynvim

RUN apt install zsh -y
RUN sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"

########################################
########################################
 
# make sure libjpeg-turbo is installed properly
RUN python -c "from PIL import features; print(features.check_feature('libjpeg_turbo'))"
