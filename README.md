# Sequencing webtools
## Table of Contents
[User's guide](#uguide)
- [Getting started](#get_started)
  - [Website](#website_)
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
- [Trouble shooting](#help_)
- [Authors](#authors_)

# <a name="uguide"></a> User's Guide
<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138066166-20b61ed3-6cdb-45b8-933c-2477a926d8cb.png">
</p>

## <a name="get_started"></a> Getting started
To run the sequencing webtools the docker session must be active and running on the respective servers.

### <a name="website_"></a> Website

| Website	| Web address |
| --- | --- |
| RD Analysis server |	http://3.121.193.167:8089/ |
| RD DeNovo	| http://18.185.163.29:8089/ |
| RD Basecalling	| http://54.93.42.32:8089/ |
| Services Analysis Server	| http://52.57.88.220:8089/ |
| Services DeNovo	| http://3.64.167.61:8089/ |
| Services Basecalling	| http://18.157.144.14:8089/ |

## <a name="basecall_tools"></a> Basecalling tools
The basecalling tools contains the tools for basecalling of ONT fast5 files incl. basecalling report and for making the basecalling report on already basecalled data. 
### <a name="basecalling_"></a> Basecalling
The basecalling pipeline basecalls ONT fast5 files to fastq and generates a basecalling report in html-format using pycoQC.

To run the basecalling pipeline:
1. Click _basecalling_ under Basecalling tools

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138068474-7c075f06-7e8f-438c-a5d1-bf85b040d12c.png">
</p>

2. Fill out all the fields in the form and click _Next_. 

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138076322-74f5283d-5490-4036-b86c-0716914c261d.png" width="300" height="510">
</p>

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

3. A config file has now been generated. It is possible to run the basecalling pipeline manually or to click _Run the pipeline_.  

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138076017-fbc2a41a-8e06-434b-9604-09c983800cb0.png" width="510" height="300">
</p>

4. An email will be sent to the provided e-mail address upon completion.

### <a name="basecalling_report"></a> Basecalling report
Generates a basecalling report in html-format on already basecalled data with pycoQC. 

1. Click _basecalling report_ under Basecalling tools.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138086622-c873da54-c47c-4191-9abf-7cd26dc18cd5.png">
</p>

2. Fill out the form and click _Run_

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138083709-804e7a64-3c8f-4dfe-b353-264a5b942e63.png" width="300" height="510">
</p>

See description of fields here:

| Field	| Description |
| --- | --- |
|   **Sequencing summary file** |   Sequencing summary file generated during basecalling  |
|   **BAM file** |   Optional. Provide to also receive alignment data  |
|   **Output file name**   |   Optional. Change report name. Default is basecalling_report.html    |

3. It will run immediately. 

## <a name="ref_tools"></a> Reference tools
Download reference and annotation, merge scaffold and prepare reference for use in enrichment mapping report pipeline. 

### <a name="download_ref"></a> Download reference
1. Click _Download reference_ under Reference tools.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138087564-41cc304d-cfd0-4429-adfc-8fd18a76dab7.png">
</p>

2. Fill out the form and click _Download_

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138086228-34d6b01d-cd5f-42d7-9d39-ffa1cb786eef.png" width="500" height="416">
</p>

See description of fields here:

| Field	| Description |
| --- | --- |
|   **Download link** |   ftp or http link pointing to reference file  |
|   **Save path** |   Main directory to save the downloaded reference in  |
|   **Subdirectory**   |   Generate new subdirectory in main directory   |

3. It will run immediately. 


### <a name="download_annot"></a> Download annotations
1. Click _Download annotation_ under Reference tools.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138087742-266d65a7-9ed1-466c-80d2-3bb59d1a5496.png" >
</p>


2. Fill out the form and click _Download_

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138087564-41cc304d-cfd0-4429-adfc-8fd18a76dab7.png" >
</p>



See description of fields here:

| Field	| Description |
| --- | --- |
|   **Download link** |   ftp or http link pointing to annotation file  |
|   **Save path** |   Directory to save the downloaded annotation in  |


3. It will run immediately. 

### <a name="merge_scaffold"></a> Merge scaffolds
Many genomes consist of the primary assembly and scaffolds, or entirely of scaffolds, i.e. the human genome consists of 24 sequences in the primary assembly and >600 scaffold (alternative references) sequences. It can quickly become meaningless to map to this many scaffolds, and therefore it is recommended to map to the primary assembly only. However, if you are worried about ‘losing’ information by not including the scaffolds, or if your assembly only consists of scaffolds, it is possible to merge these scaffolds together.

If merging alternative references, obtain the primary assembly first and create a list of these. 

1. Click _Merge scaffolds_ under Reference tools.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138088631-cb0655c5-dbfc-4067-b236-19ed3c6a6066.png" >
</p>


2. Fill out the form and click _Next_

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138087564-41cc304d-cfd0-4429-adfc-8fd18a76dab7.png" >
</p>

See description of fields here:

| Field	| Description |
| --- | --- |
|   **Reference file** |   Path to reference file  |
|   **Save path** |   Main directory to save the downloaded reference in  |

3. Fill out the rest of the form and click _Run_

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138087564-41cc304d-cfd0-4429-adfc-8fd18a76dab7.png" >
</p>

See description of fields here:

| Field	| Description |
| --- | --- |
|   **Change output file name** |   Optional. Change name of output file. Default is REFERENCE_scaffold_merged.fasta  |
|   **Extract primary assembly** |   Optional. Provide a list of the primary assembly to extract  |
|   **Change size limit** |   Default size limit is 2^29 (536970912) bp. Samtools cannot use bai index for sizes above this limit. |

4. It will run immediately. 


### <a name="prep_ref"></a> Prepare reference
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
<img src="https://user-images.githubusercontent.com/60882704/138087564-41cc304d-cfd0-4429-adfc-8fd18a76dab7.png" >
</p>


2. Fill out the form and click _Next_

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138087564-41cc304d-cfd0-4429-adfc-8fd18a76dab7.png" >
</p>

See description of fields here:

| Field	| Description |
| --- | --- |
|   **Reference file** |   Path to reference file  |
|   **Save path** |   Main directory to save the downloaded reference in  |

3. Fill out the rest of the form and click _Run_

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138087564-41cc304d-cfd0-4429-adfc-8fd18a76dab7.png" >
</p>

See description of fields here:

| Field	| Description |
| --- | --- |
|   **Index reference for use in IGV** |   Optional. An indexed reference file is required for viewin in IGV. Is significantly faster than indexing locally. |
|   **Create BWA index for ILMN** |   Optional. BWA index is required when running the ILMN enrichment mapping report pipeline. This is time consuming  |
|   **Change size limit** |   Default size limit is 2^29 (536970912) bp. Samtools cannot use bai index for sizes above this limit. |
|   **Extract primary assembly** |   Optional. Provide a list of the primary assembly to extract  |
|   **Rename extracted assembly** |   Optional. Requires extraction of primary assembly. Provide a list of the new names to be used. |

4. It will run immediately. 

## <a name="analysis_tools"></a> Analysis tools

### <a name="enrich_report"></a> Enrichment mapping report
The enrichment mapping report pipeline can be performed on both ILMN and ONT fastq files. The majority of the pipeline is the same, however, there are some slight differences prior to mapping. FastQC is performed on ILMN fastq files before and after trimming with trimmomatic as a QC measure. The outputs are run reports in html format.

Mapping is performed with minimap2 and bwa-mem for ONT and ILMN data, respectively, with standard parameters and output in SAM format. After mapping, SAMtools is used to convert the SAM file into a compressed binary SAM format: BAM. The BAM file is subsequently manipulated in SAMtools. Read lengths are obtained for the different target regions (ROI, customizable region and 10 kb regions) using awk. Softclipped regions are obtained using our own python scripts. Genome coverage is obtained using Qualimap. BAM files and statistics obtained from SAMtools, together with sequence lengths and genome coverage are processed in R, utilizing our own Rscript. This generates the figures and table incorporated into the reports. The reports are generated using docx-tpl and soffice.

1. Click _Enrichment mapping report_ under Analysis tools.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138098832-26bef526-5be3-48c7-9853-aa5275dffbab.png" >
</p>


2. Choose between ONT and ILMN. Click on create a config file or upload an existing config file. 

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138101108-af9b94d3-5bfc-4b2c-b43a-c4d6d3326c31.png" >
</p>


3. Fill out the form.

* Report parameters:

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138105942-b446f219-77ee-4f07-aecd-717d28f986fd.png" width="300" height="320">
</p>

   * File paths for ONT or ILMN

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138106292-5292bdc9-f759-4da2-8417-53a29a925980.png" width="600" height="300">
</p>

   * Region of Interest:

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138106654-6dcc8151-6ca2-41e0-a157-f92a45797872.png" width="500" height="465">
</p>

   * Other settings

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138106848-fa63499e-8d90-48f3-a1e9-f3296be6ea06.png" width="320" height="300">
</p>


   * Advanced Settings for ONT or ILMN

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138087564-41cc304d-cfd0-4429-adfc-8fd18a76dab7.png" >
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
| **Reference file path** | Path to reference file  |
| **Bed file path** | Path to bedfile for chromosome of interest  |
| **KaryoploteR genome file path**  | Path to custom genome file for KaryoploteR  |
| **ROI coordinates** | Start and end coordinates for region of interest  |
| **Validation sequence** | Start and end coordinates for validation sequence(s)  |
| **Detection sequence**  | Start and end coordinates for detection sequence(s) |
| **Custom region title** | Title for custom region. Default is 100, e.g. become 100 kb. Only integers  |
| **Custom region coordinates** | Start and end coordinates for custom region. Autocalculated around first detection sequence coordinates |
| **Quality filtering** | Optional. Quality filtering of alignment. Default is 0  |
| **CPU threads** | Number of CPU threads to use. Default is 4  |
| **Skip mapping**  | Path to directory containing _output.sam_ in order to skip the mapping part.  |
| **minimap2 additional arguments** | Advanced. Provide additional mapping arguments to minimap2. |
| **BWA-MEM additional arguments**  | Advanced. Provide additional mapping arguments to bwa-mem |

4. Click _Create config file_.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138087564-41cc304d-cfd0-4429-adfc-8fd18a76dab7.png" >
</p>

5. Click _Run the pipeline_ to run the enrichment mapping report pipeline. An e-mail will be sent upon completion

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138112094-da2ddfd4-120b-4ded-947b-435f33d1a40f.png" >
</p>





### <a name="add_tags"></a> Add tags to alignment
Two tags are currently possible: read name (RG) and all chromosomes which each read aligns to (RZ), e.g. if read A maps to chr_01, chr_05, and chr_08, the tag will be chr_01;chr_05;chr_08. This tag will be added to each instance of read A present in the S/BAM alignment file. Using these two tags, this allows for coloring by read name (enabling to see chimeric reads) and grouping alignments by chromosomes. This is highly useful when working with inserts.
