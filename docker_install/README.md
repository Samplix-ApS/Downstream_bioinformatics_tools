# Docker installation

## Table of Contents
- [Description](#descript_)
- [System recommendations](#system_rec)
- [Installation](#install_) 
  - [Linux](#linux_)
    - [Enable GPUs](#linux_gpu)
  - [Microsoft Windows](#windows_)
    - [Enable GPUs](#windows_gpu)
- [How to run the Samplix Docker image](#run_docker)
  - [Commands integrated into python Docker script](#python_docker)
    - [Pull latest image](#pull_docker)
    - [Run Reference and Analysis tools](#docker_web) 
    - [Run Basecalling tools (GPUs exposed)](#run_gpu)
    - [Other integrated commands](#docker_cmds)
  - [Other Docker commands](#other_cmds)
- [Mount points](#mount_points)
- [Internal webserver ports](#internal_web_ports)
- [Available tools](#avail_tools)
  - [Bioinformatics tools](#bioinfo_tools)
  - [Pipelines](#pipelines_) 
  - [Web utility](#web_utility_)
  - [Python utility scripts](#python_utility)
- [Trouble shooting](#help_)
- [Authors](#authors_)

# <a name="descript_"></a> Description
Samplix analysis tools Docker image is available publicly on Docker hub.
It contains tools for basecalling and basecalling report generation of Oxford Nanopore Technologies® reads, sequencing enrichment validation of enriched of samples in the form of an enrichment mapping report for both Oxford Nanopore Technologies® and Illumina® reads, as well as the necessary reference handling tools for report generation and tools for aiding with visualization of insertions. 
# <a name="system_rec"></a> System recommendations

| Type | CPU | RAM | GPU |
|------|-----|-----|-----|
|Small genomes <4GB |16 GB| 32 GB| - |
|Large genomes >4GB or De novo| 64 GB | 128 GB | - |
|Basecalling | 8 GB | 61 GB | Tesla V100 </br> 16 GB mem |


# <a name="install_"></a> Installation
## <a name="linux_"></a> Linux 
1. Download and install the [Docker for Linux](https://docs.docker.com/get-docker/).
2. Follow the [installation instructions](https://docs.docker.com/engine/install/) for your Linux distribution.

### <a name="linux_gpu"></a> Enable GPUs
If you wish to use the Basecalling tools the GPUs need to be available to the Docker container. 
1. Download and install [Nvidia CUDA version 11.xx](https://developer.nvidia.com/cuda-downloads)
2. Download and install [Nvidia_container_runtime](https://github.com/NVIDIA/nvidia-container-runtime). Follow the [installation guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)

## <a name="windows_"></a> Microsoft Windows
1. You must have Windows 10, version 1903 or higher, or Windows 11
2. [Enable WSL 2](https://docs.microsoft.com/en-us/windows/wsl/install) feature on Windows.
    * ``` wsl --install ```
    * ``` wsl.exe --set-default-version 2 ```
3. Download and install the [Linux kernel update package](https://docs.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package). Step 4.
4. Download the [Docker Desktop for Windows](https://docs.docker.com/get-docker/) and install.
5. Start Docker Desktop. Select **Settings>General**. Select the _Use the WSL 2 based engine_.
<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/143251421-cedb9d9e-334c-4ee3-8850-0d08cf00cb49.png">
</p>
6. Apply & Restart

### <a name="windows_gpu"></a> Enable GPUs

If you wish to use the Basecalling tools the GPUs need to be available to the Docker container.</br>
You will need:
* A machine with an NVIDIA GPU
* The latest Windows Insider version from the Dev Preview ring
  * [Register](https://insider.windows.com/en-us/getting-started#register) to the program
  * Make sure you choose the _Dev Channel_ when selecting Insider settings during setup. 
  * Check for updates in the Windows Update panel, and install any Insider updates.
* [Beta drivers](https://developer.nvidia.com/cuda/wsl) from NVIDIA supporting WSL 2 GPU Paravirtualization
* Update WSL 2 Linux kernel to the latest version using ``` wsl --update ``` from an elevated command prompt (run cmd as administrator)
* Make sure the WSL 2 backend is enabled in Docker Desktop
* Install a linux distribution, e.g. Ubuntu from the Microsoft Store.
* In Docker Desktop go to **Settings>Resources>WSL INTEGRATION** and _Enable integration with my default WSL distro_. Also _Enable integration with additional distros_ and tick off your Linux distribution, e.g. Ubuntu
<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/143260061-0b1715c5-e414-42eb-a941-24c140fe96dc.png">
</p>

* See the [best practices](https://docs.docker.com/desktop/windows/wsl/#best-practices) on how to get the best out of the file system performance when bind-mounting files.


# <a name="run_docker"></a> How to run the Samplix Docker image
Samplix actively develops, builds and pushes the following Docker image to the Docker hub registery: 

**samplix/samplix_analysis_tools:latest**

This image is available at our public repository:

<https://hub.docker.com/r/samplix/samplix_analysis_tools>


## <a name="python_docker"></a> Commands integrated into python Docker script
For ease in running the Docker image a python script has been provided ([**Docker script**](https://github.com/Samplix-ApS/Bioinformatics_tools/tree/main/docker_script)). Please use this script.

It automatically pulls the latest image when iniating the Docker in [Reference and Analysis tools mode](https://github.com/Samplix-ApS/Bioinformatics_tools/tree/main/docker_script#start_docker) or in [Basecalling tools mode](https://github.com/Samplix-ApS/Bioinformatics_tools/tree/main/docker_script#start_basecall) with GPUs exposed, both in _HTTP_ or _HTTPS_ mode. It also allows you to easily [stop](https://github.com/Samplix-ApS/Bioinformatics_tools/tree/main/docker_script#stop_docker) the active Docker container, as well as easily accessing [bash mode](https://github.com/Samplix-ApS/Bioinformatics_tools/tree/main/docker_script#bash_docker). 


### <a name="pull_docker"></a> Pull latest image
Pull latest Docker image:
```
docker pull samplix/samplix_analysis_tools:latest
```

### <a name="docker_web"></a> Run Reference and Analysis tools
Runs the docker image with webserver

_HTTP Mode_:
```
docker run -td -v [absolute path to input direcotry]:/input-data -v [absolute path to reference sequence directory]:/refseq-data -p [external port]:8080 samplix/samplix_analysis_tools:latest
```
_HTTPS Mode_:
```
docker run -td -v [absolute path to input direcotry]:/input-data -v [absolute path to reference sequence directory]:/refseq-data -e SECURE=true -p [external port]:4430 samplix/samplix_analysis_tools:latest
```
### <a name="run_gpu"></a> Run Basecalling tools (GPUs exposed)


_HTTP mode with GPUs_:

```
docker run -td –gpus all -v [absolut epath to input direcotry]:/input-data -p [external port]:8080
samplix/samplix_analysis_tools:latest

```

_HTTPS mode with GPUs_:

```
docker run -td –gpus all -v [absolute path to input direcotry]:/input-data -e SECURE=true -p [external port]:4430
samplix/samplix_analysis_tools:latest

```

### <a name="docker_cmds"></a> Other integrated commands

Display all containers, both running and stopped:
```
docker ps -a
```

To access bash of currently running container:
```
docker exec -it [Container id\] bash
```

To stop a running container:
```
docker stop [container id]
```

## <a name="other_cmds"></a> Other Docker commands

Displays all local docker images:
```
docker images
```

To remove all stopped containers:
```
docker container prune
```

To remove all images and containers from the server:
```
docker system prune -a
```



To delete a Docker image:
```
docker rmi [image id]
```
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

# <a name="avail_tools"></a> Available tools

The Docker image _**samplix/samplix_analysis_tools**_ is based on
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

Basecalling and enrichment mapping pipelines' executables can be accessed within Docker container by running the following commands:
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

This webserver starts as Docker container entry point command and starts serving on HTTP(8080) or HTTPS(4430) ports depending on the Docker container command. (See below)


## <a name="python_utility"></a> Python utility scripts

| **Script**                              | **Description** |
|-----------------------------------------|-----------------|
| /web-utility/scripts/add_SAM_tag.py     | To add tags to alignment                |
| /web-utility/scripts/merge_scaffolds.py | To merge scaffolds                |
| /web-utility/scripts/prep_reference.py  | To prepare reference for enrichment mapping report pipeline                |
|/web-utility/scripts/gff_rename.py | To rename chromosomes in annotation |


# <a name="help_"></a> Troubleshooting
Contact bioinformatics@samplix.com

# <a name="authors_"></a> Authors
Camille Johnston

Qammar Abbas
