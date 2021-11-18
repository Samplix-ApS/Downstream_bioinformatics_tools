<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141110306-3e1234ec-0ce5-47f1-9bd5-0d3ad7aa232a.png">
</p>


## Table of Contents
- [Getting started](#get_started)
  - [Test data](#test_data_) 
  - [Refseq database](#refseq_database_)
- [Basecalling tools](#basecall_tools)
  - [Basecalling](#basecalling_)
  - [Basecalling report](#basecalling_report)
- [Reference tools](#ref_tools)
  - [Download reference](#download_ref)
  - [Download annotations](#download_annot)
  - [Merge scaffolds](#merge_scaffold)
  - [Prepare reference](#prep_ref)
- [Analysis tools](#analysis_tools)
  - [Enrichment mapping report](#enrich_report)
  - [Add tags to alignment](#add_tags)
- [Other manuals](#manuals_)
- [Trouble shooting](#help_)
- [Authors](#authors_)



## <a name="get_started"></a> Getting started
<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141080729-e0cbf1b2-3092-45dc-9b20-10d144a499f5.png">
</p>


Basecalling tools, Reference tools and Analysis tools needed for handling ONT and ILMN data. 

1. Docker must be installed. See the [**docker installation manual**](https://github.com/Samplix-ApS/Bioinformatics_tools/tree/main/docker_install) for instruction on how to install the docker. 
2. Download the [**docker script**](https://github.com/Samplix-ApS/Bioinformatics_tools/tree/main/docker_script).
3. Initiate the docker session with the [**docker script**](https://github.com/Samplix-ApS/Bioinformatics_tools/tree/main/docker_script).
4.  In order to access the web-interface of a running docker session please access the public IP address of the server that the docker is running on and the external port used to start the docker session: http://IP-ADDRESS:8089 (_e.g. http://192.168.2.3:8089_).</br>
If the docker was initiated with a secure port use https://IP-ADDRESS:4430 instead. </br>
If you do not know your public IP address, please contact your local IT support.   

### <a name="test_data_"></a> Test data
Enriched TP53 test data can be downloaded from the [**test data set**](https://github.com/Samplix-ApS/Bioinformatics_tools/blob/main/test_data/README.md).
This can be used to test the different bioinformatics tools. It contains ONT fast5 files, ONT fastq and ILMN fastq files, as well as the generated reports. 

### <a name="refseq_database_"></a> Refseq database
There are some references ready and available for use in our [Refseq database](http://samplix-public-data.s3-website.eu-central-1.amazonaws.com/?prefix=public-data/Refseq/). The human genomes have already been indexed with bwa for use with Illumina reads. 

## <a name="basecall_tools"></a> Basecalling tools
<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141127343-b773440e-bc9c-4e85-8693-78ceff47a342.png">
</p>

The basecalling tools contains the tools for basecalling of ONT fast5 files incl. basecalling report and for making the basecalling report on already basecalled data, which requires the _sequencing_summary.txt_ file generated by the basecaller. 
<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138285922-2504c3d8-b996-4011-accf-ded52e7a53fd.png">
</p>




### <a name="basecalling_"></a> Basecalling
<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141127684-5ac442da-23b5-4eb0-aef7-19dbe2821e15.png">
</p>


The basecalling pipeline basecalls ONT fast5 files to fastq and generates a basecalling report in html-format using pycoQC.

To run the basecalling pipeline:
1. Click _basecalling_ under Basecalling tools

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/140943846-e6aa413f-5d1c-41b4-97a9-b600696393d5.png">
</p>


2. Fill out all the fields in the form and click _Next_. 

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/140944287-df16d75c-9d09-4d87-a0a8-2cab83ad3336.png" >


See description of fields here:

| Field	| Description |
| --- | --- |
|   **Report name** |   Name of the report, e.g. TP53 RD report 2021-10-20  |
|   **E-mail** |   E-mail to send the report to    |
|   **Input directory path**   |   Path to fast5 input directory to basecall on    |
|   **Save directory path** |   Path to save directory for output files |
|   **Sequencing kit** |   Sequencing kit used for library generation  |
|   **Barcode kit** |   Provide barcoding kit used for library generation. If no barcoding was performed, choose None   |
|   **Basecalling model**   |   HAC (high accuracy)  or SUP (super accuracy) model. SUP takes 3x as long as HAC. Usually HAC is sufficient. |

3. A config file has now been generated. Click _Run the pipeline_.  

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141100922-322a1456-77f3-43a9-8d4b-2f01cb830b9f.png" >
</p>



4. An e-mail will be sent to the provided e-mail address upon completion.
<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141101093-2bbe9142-113f-44f4-9350-67e3f497411a.png" >
</p>



### <a name="basecalling_report"></a> Basecalling report
<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141132543-b425f7fe-76c6-40b6-aefe-15c0d4a1a0ee.png" >
</p>




Generates a basecalling report in html-format on already basecalled data with pycoQC. 

1. Click _basecalling report_ under Basecalling tools.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/140946092-34c3bee4-b246-4650-8700-c041c9bf699e.png">
</p>


2. Fill out the form and click _Run_

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141108508-1786ef7e-31e6-4b44-bf92-9e65fe37b251.png" >
</p>

See description of fields here:

| Field	| Description |
| --- | --- |
|   **E-mail** |   E-mail to send the report to    |
|   **Sequencing summary file** |   Sequencing summary file generated during basecalling  |
|   **BAM file** |   Optional. Provide to also receive alignment data  |
|   **Output file name**   |   Optional. Change report name. Default is basecalling_report.html    |



3. It will run immediately. An email will be sent to the provided e-mail address upon completion.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141109988-c8d378d6-4bfe-4fdc-a364-bf2c5efc4f24.png" >
</p>



## <a name="ref_tools"></a> Reference tools
<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141127998-a5ccd1d1-a933-4d68-ad3f-07b889f7afcd.png">
</p>

Download reference and annotation, merge scaffold and prepare reference for use in enrichment mapping report pipeline. 

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138286021-90d46dd3-93f6-4eb3-81f2-fcc8ccc3c74a.png">
</p>

### <a name="download_ref"></a> Download reference
<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141128232-45c353a9-7a0c-40fd-9cec-7352c6164a3f.png">
</p>

If you do not already have a reference, you can use the download reference tool.

See the [download references manual](https://github.com/Samplix-ApS/Bioinformatics_tools/tree/main/download_reference_and_annotation#download_ref) on how to obtain refseq and genbank ftp links.

There are some references ready and available for use in our [Refseq database](http://samplix-public-data.s3-website.eu-central-1.amazonaws.com/?prefix=public-data/Refseq/)

1. Click _Download reference_ under Reference tools.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/140946916-79a2b2ad-7e1d-497d-8fca-8c0c686bd426.png">
</p>


2. Fill out the form and click _Download_

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/142181926-13486aab-670b-4999-9cd7-9da57718330e.png" >
</p>

See description of fields here:

| Field	| Description |
| --- | --- |
|   **Download link** |   ftp or http link pointing to reference file  |
|   **Save path** |   Main directory to save the downloaded reference in  |
|   **Subdirectory**   |   Generate new subdirectory in main directory   |

3. It will run immediately. 

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141086040-eeb94fcd-73ee-4265-bea4-9e3a6f39048c.png" >
</p>



### <a name="download_annot"></a> Download annotations

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141128337-550783b6-b2d9-4909-9187-8551d7040d31.png" >
</p>

If you need annotations for your reference and you do not already have them, then you can use the download annotation tool.

See the [**download annotation manual**](https://github.com/Samplix-ApS/Bioinformatics_tools/tree/main/download_reference_and_annotation#download_gff) on how to obtain refseq and genbank ftp links.
1. Click _Download annotation_ under Reference tools.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/140947894-9a9fe0c3-c2a9-48e9-b3f6-243ad25992bb.png" >
</p>


2. Fill out the form and click _Download_

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/142182046-f2755bd7-0854-44c5-a933-83b878d205bb.png">
</p>



See description of fields here:

| Field	| Description |
| --- | --- |
|   **Download link** |   ftp or http link pointing to annotation file  |
|   **Save path** |   Directory to save the downloaded annotation in  |


3. It will run immediately. 

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141086954-644a4237-fde0-46bc-8c88-45fa5c0c139d.png" >
</p>




### <a name="merge_scaffold"></a> Merge scaffolds

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141128434-741f5d2c-751d-426b-88d9-913cc623f7b7.png" >
</p>


Many genomes consist of the primary assembly and scaffolds, or entirely of scaffolds, i.e. the human genome consists of 24 sequences in the primary assembly and >600 scaffold (alternative references) sequences. It can quickly become meaningless to map to this many scaffolds, and therefore it is recommended to merge the scaffolds to avoid  ‘losing’ information by not including the them. However, be aware that inclusion of ALT contigs. ALT contigs are large variations with very long flanking sequences nearly identical to the primary human assembly. Most read mappers will give mapping quality zero to reads mapped in the flanking sequences. This will reduce the sensitivity of variant calling and many other analyses ([_Which human reference genome to use?_](http://lh3.github.io/2017/11/13/which-human-reference-genome-to-use)).
</br> It is necessary to use merge scaffolds if your assembly only contains scaffolds and contigs and exceeds 40 sequence records.
A bed-like file will be generated for the merged scaffolds, containing the position and name of the original scaffold as a feature. 

If your reference contains a primary assembly, create a list of these chromosome names. See [Primary assembly extraction](https://github.com/Samplix-ApS/Bioinformatics_tools/tree/main/download_reference_and_annotation#prim_). 

1. Click _Merge scaffolds_ under Reference tools.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/140949105-7c807896-a3bf-42f6-8074-8ba6953252a7.png" >
</p>



2. Fill out the form and click _Next_

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/142181436-659a9b45-8e3f-4ab6-b6ac-c4b767f94445.png" >
</p>



See description of fields here:

| Field	| Description |
| --- | --- |
|   **Reference file** |   Path to reference file (fasta format) |
|   **Save path** |   Main directory to save the downloaded reference in  |

3. Fill out the rest of the form and click _Run_

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/142181627-5cdb3500-7567-4771-a00e-f829c896c65e.png">
</p>


See description of fields here:

| Field	| Description |
| --- | --- |
|   **Change output file name** |   Optional. Change name of output file. Default is REFERENCE_scaffold_merged.fasta  |
|   **Extract primary assembly** |   Optional. Provide a list of the primary assembly to extract. See [**primary assembly extraction**](https://github.com/Samplix-ApS/Bioinformatics_tools/tree/main/download_reference_and_annotation#prim_)  |
|   **Change size limit** |   Default size limit is 2^29 (536970912) bp. Samtools cannot use bai index for sizes above this limit. |
                                                                                                                                     


4. It will run immediately. 

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141098182-7396659f-35d0-4dba-bb17-abee1c68f22f.png" >
</p>



5. Continue to prepare reference

### <a name="prep_ref"></a> Prepare reference

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141128557-f79edd33-c27d-459c-8353-4618ad02cb19.png" >
</p>

Prepare reference for use in enrichment mapping report generation.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138286223-6ac73071-f4b7-4d4b-8263-f93484b205aa.png" >
</p>

References must be properly prepared for use in the enrichment mapping report pipeline.
Generate the following files:
*	Can extract sequences from a list of chromosomes to create a filtered reference
*	Can extract sequences and rename them from a list of chromosome names and a list of replacement names
*	Checks the number of records present in reference:
    * If records exceed 50 in number, program is aborted.
*	Outputs bed files with 6 columns.
*	Indexes with bwa when set to true. Default is false
*	Indexes with samtools for use in IGV
*	Outputs genome file for karyoploteR.

1. Click _Prepare reference_ under Reference tools.


<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/140951522-3aa2ef17-f68a-4578-a635-79fa9e77d272.png" >
</p>


2. Fill out the form and click _Next_

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/142177696-6136f7ee-2ba0-426a-a791-607e60b109fb.png" >
</p>


See description of fields here:

| Field	| Description |
| --- | --- |
|   **Reference file** |   Path to reference file (fasta format) |
|   **Save path** |   Main directory to save the downloaded reference in  |

3. Fill out the rest of the form and click _Run_

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/142178084-8fa61956-1307-4439-a6d6-979a839093fe.png" >
</p>


See description of fields here:

| Field	| Description |
| --- | --- |
|   **Index reference for use in IGV** |   Optional. An indexed reference file is required for viewin in IGV. Is significantly faster than indexing locally. |
|   **Create BWA index for ILMN** |   Optional. BWA index is required when running the ILMN enrichment mapping report pipeline. This is time consuming  |
|   **Change size limit** |   Default size limit is 2^29 (536970912) bp. Samtools cannot use bai index for sizes above this limit. |
|   **Extract primary assembly** |   Optional. Provide a list of the primary assembly to extract. See [**primary assembly extraction**](https://github.com/Samplix-ApS/Bioinformatics_tools/tree/main/download_reference_and_annotation#prim_)  |
|   **Rename extracted assembly** |   Optional. Requires extraction of primary assembly. Provide a list of the new names to be used. See [**primary assembly extraction**](https://github.com/Samplix-ApS/Bioinformatics_tools/tree/main/download_reference_and_annotation#prim_)  |
|   **Keep merged scaffolds** |   Optional. Keep merged scaffolds without haveing to provide them in the lists  |
4. It will run immediately. 

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141089527-872d8c14-5d2c-4361-b0f1-2eabc301dfb3.png">
</p>

5. Continue to Enrichment mapping report

## <a name="analysis_tools"></a> Analysis tools
<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141128960-24312e54-87d3-434f-a8ee-f71f97517d2e.png" >
</p>

Analysis tools for generation of enrichment mapping report and adding tags to alignments for Oxford Nanopore® Technologies and Illumina® data.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138286397-c3b80ca1-e9f6-491f-9359-e161d059b903.png" >
</p>


### <a name="enrich_report"></a> Enrichment mapping report
<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141129164-115b76c6-2a1f-41e8-beab-12c7188af4d7.png" >
</p>



The enrichment mapping report pipeline can be performed on both ILMN and ONT fastq files. It generates a report containing read, mapping and enrichment stats. See [enrichment mapping report manual](https://github.com/Samplix-ApS/Bioinformatics_tools/blob/main/Emap_report_manual/) for further details.

1. Click _Enrichment mapping report_ under Analysis tools.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141082242-92800276-fff9-4aea-89e3-5fe0cdb87ffe.png" >
</p>


2. Click on Create ONT or ILMN config file or upload existing config file: 

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141082788-c53ea930-f7c6-4cc3-9b81-4f269ad0ae2d.png" >
</p>



3. Fill out the form and click _Create config file_.

* Report parameters:

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141092977-c34649bc-c068-4776-85ce-1513557fdb00.png">
</p>



   * File paths for ONT or ILMN

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/142179534-897f00bf-6e83-49bd-8fb7-32edbd751922.png">
</p>



   * Region of Interest:

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/142179768-1e489c16-92c2-4655-a94c-c74b68de3df2.png">
</p>


   * Other settings

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141502341-330cdf9b-5b35-4b8d-ac0d-f39251c47cb6.png" >
</p>




   * Advanced Settings for ONT or ILMN

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/142180005-a425be6e-d6ba-4fa8-b5a1-aa2d203dc5ff.png" >
</p>






See description of fields here:

| Field	| Description |
| --- | --- |
| **Name of report/project number** | Name of the report. |
| **Sample name** | Name of the sample sequenced. |
| **Genome name** | Name of the reference genome  |
| **Email** | Valid e-mail address to send report to  |
| **Input file path** | Input fastx file for ONT data |
| **First input file path** | First input fastx file for paired-end ILMN data |
| **Second input file path**  | Second input fastx file for paired-end ILMN data  |
| **Reference file path** | Path to reference fasta file  |
| **Bed file path** | Path to bedfile for chromosome of the region of interest  |
| **KaryoploteR genome file path**  | Path to custom genome file for KaryoploteR  |
| **ROI coordinates** | Start and end coordinates for region of interest. Size is auto-calculated  |
| **Validation sequence** | Start and end coordinates for validation sequence(s). Size is auto-calculated  |
| **Detection sequence**  | Start and end coordinates for detection sequence(s). Size is auto-calculated |
| **Custom region title** | Title for custom region. Default is 100, e.g. become 100 kb. Only integers  |
| **Custom region coordinates** | Start and end coordinates for custom region. Auto-calculated around first detection sequence coordinates |
| **Quality filtering** | Optional. Quality filtering of alignment. Default is 0  |
| **CPU threads** | Number of CPU threads to use. Default is 4  |
| **Skip mapping**  | Path to directory containing _output.sam_ in order to skip the mapping part.  |
| **minimap2 additional arguments** | Advanced. Provide additional mapping arguments to minimap2. |
| **BWA-MEM additional arguments**  | Advanced. Provide additional mapping arguments to bwa-mem |

4. Click _Create config file_ to create the config file needed to run the pipeline.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141096613-d8f3b23f-06ce-486b-ba40-64309a8f6460.png" >
</p>


5. Click _Run the pipeline_ to run the enrichment mapping report pipeline. An e-mail will be sent upon completion

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141504001-1d5cb577-16f8-4ed5-b961-53bd3d21fb6f.png" >
</p>



6. Generated output files can be found in _/input-data/ONT_Analysis_date_time_stamp_report-name_, e.g.: <br/> _/input-data/ONT_Analysis_2021_11_12_18_59_34.483883054_TP53_test_. <br/> See the [enrichment mapping report manual](https://github.com/Samplix-ApS/Bioinformatics_tools/blob/main/Emap_report_manual/README.md#output_) for an overview of the generated BAM files. 

### <a name="add_tags"></a> Add tags to alignment

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141129284-3ea802f6-22c5-454b-a2ed-fef4497eb555.png" >
</p>

Add tags to alignment (SAM/BAM) files to ease viewing in IGV. Especially useful when working with pseudogenes and inserts. See [**Add tags to alignment manual**](https://github.com/Samplix-ApS/Bioinformatics_tools/tree/main/viewing_bam_files_ind_IGV#add_tag).


1. Click _Add tags to alignment_ under Analysis tools.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141099272-14f5cdea-27f5-430e-bab8-fdcfb5960183.png" >
</p>


2. Fill out the form.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141100058-8de36202-672f-4fdd-b7ba-26b29069c21f.png" >
</p>


See description of fields here:

| Field	| Description |
| --- | --- |
| **BAM or SAM file** | Path to BAM or SAM file |
| **Read name tags** | Use read names as tags |
| **Aligned chromosome tags** | Use aligned chromosomes as tags |

# <a name="manuals_"></a> Other manuals
[Docker installation](https://github.com/Samplix-ApS/Bioinformatics_tools/tree/main/docker_install)

[Docker script](https://github.com/Samplix-ApS/Bioinformatics_tools/tree/main/docker_script)

[Download references and annotations](https://github.com/Samplix-ApS/Bioinformatics_tools/tree/main/download_reference_and_annotation)

[Obtain primary assembly](https://github.com/Samplix-ApS/Bioinformatics_tools/tree/main/download_reference_and_annotation#prim_)

# <a name="help_"></a> Trouble shooting
Contact bioinformatics@samplix.com

# <a name="authors_"></a> Authors
Camille Johnston (CAJ)

Qammar Abbas (QAB)

![image](https://user-images.githubusercontent.com/60882704/141129952-59dc1b46-cac6-41bc-a4b4-eb6cf9c49cb9.png)
