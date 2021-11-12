# Docker installation

## Table of Contents
- [Description](#descript_)
- [Samplix docker image](#samplix_docker_image)
- [Available tools](#avail_tools)
  - [Bioinformatics tools](#bioinfo_tools)
  - [Pipelines](#pipelines_) 
  - [Web utility](#web_utility_)
  - [Python utility scripts](#python_utility)
- [Mount points](#mount_points)
- [Internal webserver ports](#internal_web_ports)
- [Commands to run the docker image](#run_docker)
  - [Python docker script](#python_docker)
  - [Pull latest image](#pull_docker)
  - [Run Reference and Analysis tools](#docker_web) 
  - [Run Basecalling tools (GPUs exposed)](run_gpu)
- [Useful docker commands](#docker_cmds)
- [Trouble shooting](#help_)
- [Authors](#authors_)

# <a name="descript_"></a> Description
Samplix analysis tools docker image is available publicly on docker hub.
To pull and run this image as docker container, you need to have the
docker software installed and running from the following url:

<https://docs.docker.com/get-docker/>

# <a name="samplix_docker_image"></a> Samplix docker image

Samplix actively develop, build and push the following docker image to
the docker hub registery: 

**samplix/samplix_analysis_tools:latest**

This image is available at our public repository:

<https://hub.docker.com/r/samplix/samplix_analysis_tools>

You can pull this image running the following command: 
```
docker pull samplix/samplix_analysis_tools:latest
```

# <a name="avail_tools"></a> Available tools

The docker image _**samplix/samplix_analysis_tools**_ is based on
_**debian:latest**_ docker image. Following is a non exhaustive list of
tools available in the image.

## <a name="bioinfo_tools"></a> Bioinformatics tools

| **Tool**                             | **Version**         | **Description**                                        |
|--------------------------------------|---------------------|--------------------------------------------------------|
| R                                    | 4.1.1               |                                                        |
| python3                              | 3.9.5               |                                                        |
| /ont-guppy/bin/guppy_basecaller      | 5.0.15              | Available at path /ont-guppy/bin/guppy_basecaller      |
| nvidia cuda                          | 11.4.2              |                                                        |
| bedtools                             | 2.30.0              |                                                        |
| samtools                             | 1.13                |                                                        |
| minimap2                             | 2.17-r941           |                                                        |
| fastqc                               | 0.11.9              |                                                        |
| /usr/share/java/trimmomatic-0.39.jar | 0.39                | Available at path /usr/share/java/trimmomatic-0.39.jar |
| bwa                                  | 0.7.17-r1188        |                                                        |
| soffice                              | 7.2.1.2 20(Build:2) | Libreoffice                                            |
| golang-go                            |                     |                                                        |
| conda                                | 4.10.3              |                                                        |
| pip                                  | 21.1.3              |                                                        |
| pycoQC                               | 2.5.2               |                                                        |
| bioawk                               | 20110810            |                                                        |
| qualimap                             | 2.2.2-dev           |                                                        |
| java                                 | 11.0.1              |                                                        |
| seqkit                               | 2.0.0               |                                                        |

## <a name="pipelines_"></a> Pipelines

| **Pipeline**                | **Version** | **Description**                          |
|-----------------------------|-------------|------------------------------------------|
| /pipelines/basecall         | 2.0.0       | /pipelines/basecall                      |
| /pipelines/analysispipeline | 2.0.0       | Available at /pipelines/analysispipeline |

Basecalling and enrichment mapping pipleine's executables can be accessed within docker container by running the following commands:
```
/pipelines/basecall -help
```
```
/pipelines/analysispipeline -help
```


## <a name="web_utility_"></a> Web utility

| **Webserver**                | **Version** | **Description**              |
|------------------------------|-------------|------------------------------|
| /web-utility/pipelinewebtool | 1.0.0       | /web-utility/pipelinewebtool |

This webserver starts as docker container entry point command and starts serving on HTTP(8080) or HTTPS(4430) ports depending on the docker container command. (See below)


## <a name="python_utility"></a> Python utility scripts

| **Script**                              | **Description** |
|-----------------------------------------|-----------------|
| /web-utility/scripts/add_SAM_tag.py     | To add tags to alignment                |
| /web-utility/scripts/merge_scaffolds.py | To merge scaffolds                |
| /web-utility/scripts/prep_reference.py  | To prepare reference for enrichment mapping report pipeline                |
|/web-utility/scripts/gff_rename.py | To rename chromosomes in annotation |


# <a name="mount_points"></a> Mount points

| **Mount point** | **Description**                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------|
| /refseq-data | Mount point for reference sequence data. Web server will look into this directory when searching and selecting for reference files, bed files and Karyoplot files through the web interface. Refrenece sequence and annotations will be downloaded in this directory. Merge scaffolds and prepare reference tools will be saving output to this directory.|
| /input-data | Mount point for input data. Web server will look into this directory when searching and selecting input files for enrichment mapping pipeline and basecalling pipeline. |


# <a name="internal_web_ports"></a> Internal webserver ports

| **Port** | **Description**                                                                                  |
|----------|--------------------------------------------------------------------------------------------------|
| 8080     | Internal HTTP port. By default web server will start on this port                                |
| 4430     | Internal HTTPS port. When web server is started in secure mode it will start serving at this port. |

# <a name="run_docker"></a> Commands to run the docker image
## <a name="python_docker"></a> Python docker script
For ease in running the docker image a python script has been provided ([**docker script**](https://github.com/Samplix-ApS/Bioinformatics_tools/tree/main/docker_script)). 

It automatically pulls the latest image when iniating the docker in [Reference and Analysis tools mode](https://github.com/Samplix-ApS/Bioinformatics_tools/tree/main/docker_script#start_docker) or in [Basecalling tools mode](https://github.com/Samplix-ApS/Bioinformatics_tools/tree/main/docker_script#start_basecall) with GPUs exposed, both in _HTTP_ or _HTTPS_ mode. It also allows you to easily [stop](https://github.com/Samplix-ApS/Bioinformatics_tools/tree/main/docker_script#stop_docker) the active docker container, as well as easily accessing [bash mode](https://github.com/Samplix-ApS/Bioinformatics_tools/tree/main/docker_script#bash_docker). 


## <a name="pull_docker"></a> Pull latest image
Pull latest docker image:
```
docker pull samplix/samplix_analysis_tools:latest
```

## <a name="docker_web"></a> Run Reference and Analysis tools
Runs the docker image with webserver

_HTTP Mode_:
```
docker run -td -v [absolute path to input direcotry]:/input-data -v [absolute path to reference sequence directory]:/refseq-data -p [external port]:8080 samplix/samplix_analysis_tools:latest
```
_HTTPS Mode_:
```
docker run -td -v [absolute path to input direcotry]:/input-data -v [absolute path to reference sequence directory]:/refseq-data -e SECURE=true -p [external port]:4430 samplix/samplix_analysis_tools:latest
```
## <a name="run_gpu"></a> Run Basecalling tools (GPUs exposed)

\*\* In order for GPU’s to be available to docker container following is
required to be downloaded and installed on server:

**Nvidia CUDA version 11.xx**
-   <https://developer.nvidia.com/cuda-downloads>

**Nvidia_container_runtime**
  -   <https://github.com/NVIDIA/nvidia-container-runtime>
  -   <https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html>

_HTTP mode with GPUs_:

```
docker run -td –gpus all -v [absolut epath to input direcotry]:/input-data -v [absolute path to reference sequence directory]:/refseq-data -p [external port]:8080
samplix/samplix_analysis_tools:latest

```

_HTTPS mode with GPUs_:

```
docker run -td –gpus all -v [absolute path to input direcotry]:/input-data -v [absolute path to reference sequence directory]:/refseq-data -e SECURE=true -p [external port]:4430
samplix/samplix_analysis_tools:latest

```

# <a name="docker_cmds"></a> Useful docker commands

Display all containers, both running and stopped:
```
docker ps -a
```

Displays all local docker images:
```
docker images
```

To access bash of currently running container:
```
docker exec -it [Container id\] bash
```

To remove all stopped containers:
```
docker container prune
```

To remove all images and containers from the server:
```
docker system prune -a
```

To stop a running container:
```
docker stop [container id]
```

To delete a docker image:
```
docker rmi [image id]
```

# <a name="help_"></a> Troubleshooting
Contact bioinformatics@samplix.com

# <a name="authors_"></a> Authors
Qammar Abbas
