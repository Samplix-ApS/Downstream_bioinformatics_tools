# docker.py

## Table of Contents
[User's guide](#uguide)
- [Getting started](#get_started)
- [Initiate the docker container](#start_docker)
- [Initiate the basecalling tools](#start_basecall)
- [Stop the docker container](#stop_docker)
- [Enter bash mode](#bash_docker)
- [Trouble shooting](#help_)
- [Authors](#authors_)

# <a name="uguide"></a> User's Guide
## <a name="get_started"></a> Getting started
The Samplix docker must be installed. See [**docker installation manual**](https://github.com/Samplix-ApS/Bioinformatics_tools/tree/main/docker_install).

1. Click on docker.py

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141150954-70c17528-f0f2-4f1a-96f3-3c6cf40f5d01.png">
</p>

2. In the top right, right click the _Raw_ button. Choose _Save link as..._.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141151777-79365920-f8ba-4ecd-9bbd-adaf41f0809c.png">
</p>

3. Save the file with the correct file extension, i.e. **_.py_**

# <a name="start_docker"></a> Initiate the docker container
When iniating the docker container the latest docker will be pulled and updated.

To initiate the container:
```
python3 docker.py -i INPUT-DATA -r REFSEQ-DATA <optional>
```

with the following parameters:

```
-i    Input-data path
-r    Refseq-data path
-p    Optional. Choose which port to use. Default is port 8089
-x    Set to true to use secure port 4430
```

# <a name="start_basecall"></a> Initiate the basecalling tools
To use the basecalling tools, GPUs must be activated.

To initiate the container:
```
python3 docker.py -i INPUT-DATA -b true <optional>
```

with the following parameters:

```
-i      Input-data path
-b      Set to true to load basecalling tools (e.g. activate gpus)
-p      Optional. Choose which port to use. Default is port 8089
-x      Set to true to use secure port 4430
```

# <a name="stop_docker"></a> Stop the docker container
The docker container can be stopped using the command below. If more than one container is activate, the user will presented with a choice of which container to stop.

To initiate the container:
```
python3 docker.py -s stop
```

with the following parameters:

```
-s      Set to 'stop' to stop the docker container.
```

# <a name="bash_docker"></a> Enter bash mode
The docker container has a bash mode allowing you to work within the docker. You will start in the input-data directory.

To initiate bash mode:
```
python3 docker.py --bash true
```

with the following parameters:

```
--bash      Set to true to enter bash mode. Type exit to exit bash.
```

To exit bash mode simply type:
```
exit
```


# <a name="help_"></a> Trouble shooting


# <a name="authors_"></a> Authors
CAJ
