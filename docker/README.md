# Docker 

Samplix analysis tools docker image is available publicly on docker hub.
To pull and run this image as docker container, you need to have the
docker software installed and running from the following url.
<https://docs.docker.com/get-docker/>

# Samplix docker image

Samplix actively develop, build and push the following docker image to
the docker hub register.  
**samplix/samplix_analysis_tools:latest**

You can pull this image running the following command  
**docker pull samplix/samplix_analysis_tools:latest**

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

## Web utility

| **Webserver**                | **Version** | **Description**              |
|------------------------------|-------------|------------------------------|
| /web-utility/pipelinewebtool | 1.0.0       | /web-utility/pipelinewebtool |
|                              |             |                              |

## Python utility scripts

| **Script**                              | **Description** |
|-----------------------------------------|-----------------|
| /web-utility/scripts/add_SAM_tag.py     |                 |
| /web-utility/scripts/merge_scaffolds.py |                 |
| /web-utility/scripts/prep_reference.py  |                 |
|                                         |                 |
|                                         |                 |

# Mount points

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Mount point</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>/refseq-data/</td>
<td><p>Mount point for reference sequence data. Web server will look into this directory when searching and selecting for reference files through the web interface.</p>
<p>This will also serve as destination directory for downloading and saving the reference data.</p></td>
</tr>
<tr class="even">
<td>/input-data/</td>
<td>Mount point for input data. Web server will look into this directory when searching for input files, input folders and when choosing save path for out put files.</td>
</tr>
</tbody>
</table>

# Internal webserver ports

| **Port** | **Description**                                                                                  |
|----------|--------------------------------------------------------------------------------------------------|
| 8080     | Internal HTTP port. By default web server will start on this port                                |
| 4430     | Internal HTTPS port. When web server is started in secure mode it will b available at this port. |

# Command to run the docker image

Pull latest docker image

docker pull samplix/samplix_analysis_tools:latest

### Run docker image with webserver

*HTTP Mode*

docker run -td -v {absolutepath to input direcotry}:/input-data -v
{absolute path to reference sequence directory}:/refseq-data -p
{external port}:8080 samplix/samplix_analysis_tools:latest

*HTTPS Mode*

docker run -td -v {absolutepath to input direcotry}:/input-data -v
{absolute path to reference sequence directory}:/refseq-data -e
SECURE=true -p {external port}:4430
samplix/samplix_analysis_tools:latest

### Run docker with GPU’s exposed to the container

\*\* In order for GPU’s to be available to docker container following is
required to be installed on server

-   Nvidia CUDA version 11.xx

-   Nvidia_container_runtime

*HTTP Mode*

docker run -td –gpus all -v {absolutepath to input
direcotry}:/input-data -v {absolute path to reference sequence
directory}:/refseq-data -p {external port}:8080
samplix/samplix_analysis_tools:latest

*HTTPS Mode*

docker run -td –gpus all -v {absolutepath to input
direcotry}:/input-data -v {absolute path to reference sequence
directory}:/refseq-data -e SECURE=true -p {external port}:4430
samplix/samplix_analysis_tools:latest

# Useful docker commands

-   docker ps -a

-   docker images

-   docker exec -it \[container id\] bash

-   docker container prune

-   docker system prune -a

-   docker stop \[container id\]

-   docker rmi \[image id\]
