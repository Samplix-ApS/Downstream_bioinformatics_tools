# docker.py

## Table of Contents
[User's guide](#uguide)
- [Getting started](#get_started)
  - [Download docker.py locally](#download_local)
  - [Download docker.py to server](#download_server) 
- [Description](#descript_)
  - [Initiate the Reference and Analysis tools](#start_docker)
  - [Initiate the Basecalling tools](#start_basecall)
  - [Stop the docker container](#stop_docker)
  - [Enter bash mode](#bash_docker)
- [Trouble shooting](#help_)
- [Authors](#authors_)

# <a name="uguide"></a> User's Guide
## <a name="get_started"></a> Getting started
The Samplix docker must be installed. See [**docker installation manual**](https://github.com/Samplix-ApS/Bioinformatics_tools/tree/main/docker_install).

### <a name="download_local"></a> Download docker.py locally
1. Click on docker.py

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141150954-70c17528-f0f2-4f1a-96f3-3c6cf40f5d01.png">
</p>

2. In the top right, right click the _Raw_ button. Choose _Save link as..._.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141151777-79365920-f8ba-4ecd-9bbd-adaf41f0809c.png">
</p>

3. Save the file with the correct file extension, i.e. **_.py_**


### <a name="download_server"></a> Download docker.py to server
1. Click on docker.py

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141150954-70c17528-f0f2-4f1a-96f3-3c6cf40f5d01.png">
</p>

2. In the top right, right click the _Raw_ button. Choose _Copy link address..._.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141285983-595fa35e-078d-4fc4-b09e-5a950363b412.png">
</p>

 
 3. Download with wget to current directory:

```
wget LINK
```

# <a name="descript_"></a> Description
The docker container must be initiated to use the tools. There are two tool modes for the docker container: [_Reference and Analysis tools_](#start_docker) and [_Basecalling tools_](#start_basecall). The Reference and Analysis tools run using CPUs, whereas Basecalling tools requires GPUs. When initiating the docker container the latest docker will be pulled and updated.

After the docker container is up and running it is also possible to enter [_bash mode_](#bash_docker) or to [_stop_](#stop_docker) the docker.
Only one docker session can run per port. If a port is occupied please iniate the docker container with a different port using _-p_.

The following parameters are available for docker. See instruction below how to use them.

```
-i      Input-data path
-r      Reference-data path
-b      Set to true to load basecalling tools (e.g. activate gpus)
-p      Optional. Choose which port to use. Default is port 8089
-x      Set to true to use secure port 4430
-s      Set to 'stop' to stop the docker container.
--bash  Set to true to enter bash mode. Type exit to exit bash.
```



## <a name="start_docker"></a> Initiate the Reference and Analysis tools
To use the Reference and Analysis tools the docker container must be initiated. When iniating the docker container the latest docker will be pulled and updated.
Provide the directory to the sequencing data as INPUT-DATA and the reference data as REFSEQ-DATA. If both sequencing data and reference data is present in the same directory, please provide the directory twice (bot _-i_ and _-r_). The directory provided in _-i_ will appear as _/input-data/_ and the directory in _-r_ will appear as _/refseq-data/_.


To initiate the container:
```
python3 docker.py -i INPUT-DATA -r REFSEQ-DATA <optional>
```

e.g.

```
python3 docker.py -i /john/seq_data/ -r /john/reference_data/
```

with the following parameters:

```
-i    Input-data path
-r    Reference-data path
-p    Optional. Choose which port to use. Default is port 8089
-x    Set to true to use secure port 4430
```

## <a name="start_basecall"></a> Initiate the Basecalling tools
To use the Basecalling tools, GPUs must be activated when initiating the docker container. When iniating the docker container the latest docker will be pulled and updated.

Provide the directory to the sequencing data as INPUT-DATA. The directory provided in _-i_ will appear as _/input-data/_.

To initiate the container:
```
python3 docker.py -i INPUT-DATA -b true <optional>
```

e.g.

```
python3 docker.py -i /john/ont_data/ -b true
```

with the following parameters:

```
-i      Input-data path
-b      Set to true to load basecalling tools (e.g. activate gpus)
-p      Optional. Choose which port to use. Default is port 8089
-x      Set to true to use secure port 4430
```

## <a name="stop_docker"></a> Stop the docker container
The docker container can be stopped using the command below. If more than one container is activate, the user will be presented with a choice of which container to stop.

To stop the container:
```
python3 docker.py -s stop
```

with the following parameters:

```
-s      Set to 'stop' to stop the docker container.
```

## <a name="bash_docker"></a> Enter bash mode
The docker container has a bash mode allowing you to work within the docker. You will start in the _/input-data/_ directory. 
The docker container must first be up and running. 

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
Contact samplix.com

# <a name="authors_"></a> Authors
CAJ
