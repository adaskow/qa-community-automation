# qa-community-automation

## Preparations:
1. Give access to show windows run in Docker
    ```bash
    $ xhost +local:root
    ```
2. Set bdd tag as
    ```bash
    $ LABEL=`date +%Y%m%d%H%m%S`
    ```

3. Build docker image
    ```bash
    $ docker build -t $LABEL .
    ```

4. Run docker image (fill your image id from build)
    ```bash
    $ docker run -it -v $PWD:/usr/src -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -t $LABEL bash
    ```
