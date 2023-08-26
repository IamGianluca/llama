format:
	usort format . && \
	black .

download_ml:
	git clone git@github.com:IamGianluca/ml.git blazingai

install_ml:
	rm -rf blazingai/ml.egg-info/ && \
	pip install -e blazingai/

test:
	mypy pipe/ --ignore-missing-imports

build:
	docker build -t llama .

start:
	docker run -d --name llama --env-file ./.env --ipc=host --gpus all -p 5000:5000 -p 8888:8888 --rm -v "/home/gianluca/git/llama:/workspace" -v "/data:/data" -t llama

attach:
	docker exec -it llama /bin/bash

stop:
	docker kill llama

clean:
	docker system prune -a && \
	# docker stop $(docker ps -aq) && \
	# docker rm $(docker ps -a -q) && \
	# docker rmi $(docker images -aq) -f && \
	docker image prune && \
	# docker volume rm $(docker volume ls -q) && \
	docker volume prune

jupyter:
	jupyter lab --ip 0.0.0.0 --no-browser --allow-root

install_nvim:
	git clone https://github.com/IamGianluca/dotfiles.git .dotfiles && cd .dotfiles && ./install
