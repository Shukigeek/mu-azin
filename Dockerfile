FROM ubuntu:latest
LABEL authors="shuki"

ENTRYPOINT ["top", "-b"]