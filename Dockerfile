FROM node:18-bullseye-slim
COPY init_nodebb.py /

RUN apt update && \
    apt install git python3 -y
RUN cd / && git clone "https://github.com/NodeBB/NodeBB.git"
RUN cd /NodeBB && git checkout v1.19.7

WORKDIR /NodeBB
RUN cp install/package.json . && npm install

CMD python3 /init_nodebb.py && ./nodebb dev