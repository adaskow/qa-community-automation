# qa-community-automation

## Preparations:
1. Give access to show windows run in Docker
    ```bash
    $ xhost +local:root
    ```

2. Build docker image
    ```bash
    $ docker build -t docker_tag .
    ```

3. Run docker image (fill your image id from build)
    ```bash
    $ docker run -it -v $PWD:/usr/src -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -t docker_tag bash
    ```
