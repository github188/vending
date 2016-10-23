FROM 0-ubuntu-updated
ENV TZ=Asia/Shanghai
RUN echo ${TZ} | tee /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata
RUN apt-get install -y git && if [ -e /volumeCode ] ;then rm -rf /volumeCode ;fi \
&& mkdir /volumeCode && cd /volumeCode && git clone --branch prd --depth 1 https://github.com/pjsong/vending.git \
&& rm -rf /var/lib/apt/lists/* /volumeCode/.git

CMD ["/bin/bash"]
#VOLUME /volumeCode