FROM 1-git

RUN mkdir /volumeCode && cd /volumeCode && git clone --depth 1 https://github.com/pjsong/vending.git && rm -rf /var/lib/apt/lists/*
CMD ["bash"]
#VOLUME /volumeCode