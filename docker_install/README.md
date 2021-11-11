# Docker 

Samplix analysis tools docker image is available publicly on docker hub.
To pull and run this image as docker container, you need to have the
docker software installed and running from the following url.
<https://docs.docker.com/get-docker/>

# Samplix docker image

Samplix actively develop, build and push the following docker image to
the docker hub registery.  
**samplix/samplix_analysis_tools:latest**

This image is available at our public repository
<https://hub.docker.com/r/samplix/samplix_analysis_tools>

You can pull this image running the following command 
```
docker pull samplix/samplix_analysis_tools:latest
```

# Available tools

The docker image **samplix/samplix_analysis_tools** is based on
**debian:latest** docker image. Following is a non exhaustive list of
tools available in the image.

## Bioinformatics tools

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
|                                      |                     |                                                        |

## Pipelines

| **Pipeline**                | **Version** | **Description**                          |
|-----------------------------|-------------|------------------------------------------|
| /pipelines/basecall         | 2.0.0       | /pipelines/basecall                      |
| /pipelines/analysispipeline | 2.0.0       | Available at /pipelines/analysispipeline |

Basecalling and enrichment mapping pipleine's executables can be accessed within docker container by running the following commands
```
/pipelines/basecall -help
```
```
/pipelines/analysispipeline -help
```


## Web utility

| **Webserver**                | **Version** | **Description**              |
|------------------------------|-------------|------------------------------|
| /web-utility/pipelinewebtool | 1.0.0       | /web-utility/pipelinewebtool |

This webserver starts as docker container entry point command and starts serving on HTTP(8080) or HTTPS(4430) ports depending on the docker container command. (See below)


## Python utility scripts

| **Script**                              | **Description** |
|-----------------------------------------|-----------------|
| /web-utility/scripts/add_SAM_tag.py     | To add tags to alignment                |
| /web-utility/scripts/merge_scaffolds.py | To merge scaffolds                |
| /web-utility/scripts/prep_reference.py  | To prepare reference for enrichment mapping report pipeline                |


# Mount points

| **Mount point** | **Description**                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------|
| /refseq-data | Mount point for reference sequence data. Web server will look into this directory when searching and selecting for reference files, bed files and Karyoplot files through the web interface. Refrenece sequence and annotations will be downloaded in this directory. Merge scaffolds and prepare reference tools will be saving output to this directory.|
| /input-data | Mount point for input data. Web server will look into this directory when searching and selecting input files for enrichment mapping pipeline and basecalling pipeline. |


# Internal webserver ports

| **Port** | **Description**                                                                                  |
|----------|--------------------------------------------------------------------------------------------------|
| 8080     | Internal HTTP port. By default web server will start on this port                                |
| 4430     | Internal HTTPS port. When web server is started in secure mode it will start serving at this port. |

# Command to run the docker image

Pull latest docker image
```
docker pull samplix/samplix_analysis_tools:latest
```

### Run docker image with webserver

*HTTP Mode*
```
docker run -td -v [absolute path to input direcotry]:/input-data -v [absolute path to reference sequence directory]:/refseq-data -p [external port]:8080 samplix/samplix_analysis_tools:latest
```
*HTTPS Mode*
```
docker run -td -v [absolute path to input direcotry]:/input-data -v [absolute path to reference sequence directory]:/refseq-data -e SECURE=true -p [external port]:4430 samplix/samplix_analysis_tools:latest
```
### Run docker with GPU’s exposed to the container

\*\* In order for GPU’s to be available to docker container following is
required to be downloaded and installed on server

#### Nvidia CUDA version 11.xx 
-   <https://developer.nvidia.com/cuda-downloads>

#### Nvidia_container_runtime 
  -   <https://github.com/NVIDIA/nvidia-container-runtime>
  -   <https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html>

*HTTP mode with GPU's*

```
docker run -td –gpus all -v [absolut epath to input direcotry]:/input-data -v [absolute path to reference sequence directory]:/refseq-data -p [external port]:8080
samplix/samplix_analysis_tools:latest

```

*HTTPS mode with GPU's*

```
docker run -td –gpus all -v [absolute path to input direcotry]:/input-data -v [absolute path to reference sequence directory]:/refseq-data -e SECURE=true -p [external port]:4430
samplix/samplix_analysis_tools:latest

```

# Useful docker commands

Display all containers, both running and stopped
```
docker ps -a
```

Displays all local docker images
```
docker images
```

To access bash of currently running container
```
docker exec -it [Container id\] bash
```

To remove all stopped containers
```
docker container prune
```

To remove all images and containers from the server
```
docker system prune -a
```

To stop a running container
```
docker stop [container id]
```

To delete a docker image
```
docker rmi [image id]
```

