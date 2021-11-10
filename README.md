# Bioinformatics tools
<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/140942616-c6f2ee0f-3ed7-4113-bba7-39f3be87f787.png">
</p>


## Table of Contents
[User's guide](#uguide)
- [Getting started](#get_started)
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
<img src="https://user-images.githubusercontent.com/60882704/141080729-e0cbf1b2-3092-45dc-9b20-10d144a499f5.png">
</p>


Basecalling tools, Reference tools and Analysis tools needed for handling ONT and ILMN data. 

## <a name="get_started"></a> Getting started
To run the sequencing webtools the docker session must be active and running on the respective servers.

## <a name="basecall_tools"></a> Basecalling tools

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138285922-2504c3d8-b996-4011-accf-ded52e7a53fd.png">
</p>



The basecalling tools contains the tools for basecalling of ONT fast5 files incl. basecalling report and for making the basecalling report on already basecalled data, which requires the _sequencing_summary.txt_ file generated by the basecaller. 
<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/140943026-9a014190-0df2-401e-a6f1-1a975418d940.png">
</p>

### <a name="basecalling_"></a> Basecalling
The basecalling pipeline basecalls ONT fast5 files to fastq and generates a basecalling report in html-format using pycoQC.

To run the basecalling pipeline:
1. Click _basecalling_ under Basecalling tools

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/140943846-e6aa413f-5d1c-41b4-97a9-b600696393d5.png">
</p>


2. Fill out all the fields in the form and click _Next_. 

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/140944287-df16d75c-9d09-4d87-a0a8-2cab83ad3336.png" width="500" height="410">


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
<img src="https://user-images.githubusercontent.com/60882704/138087564-41cc304d-cfd0-4429-adfc-8fd18a76dab7.png" width="300" height="300">
</p>

4. An email will be sent to the provided e-mail address upon completion.

### <a name="basecalling_report"></a> Basecalling report
Generates a basecalling report in html-format on already basecalled data with pycoQC. 

1. Click _basecalling report_ under Basecalling tools.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/140946092-34c3bee4-b246-4650-8700-c041c9bf699e.png">
</p>


2. Fill out the form and click _Run_

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/140946285-9b2882c4-4bb2-4ed2-b34f-9164aeeca7fe.png" width="500" height="395">
</p>

3. An email will be sent to the provided e-mail address upon completion.


See description of fields here:

| Field	| Description |
| --- | --- |
|   **E-mail** |   E-mail to send the report to    |
|   **Sequencing summary file** |   Sequencing summary file generated during basecalling  |
|   **BAM file** |   Optional. Provide to also receive alignment data  |
|   **Output file name**   |   Optional. Change report name. Default is basecalling_report.html    |

3. It will run immediately. 

## <a name="ref_tools"></a> Reference tools
<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138286021-90d46dd3-93f6-4eb3-81f2-fcc8ccc3c74a.png">
</p>


Download reference and annotation, merge scaffold and prepare reference for use in enrichment mapping report pipeline. 
<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/140943381-a20c006f-fdc5-433c-88a0-0eef14e8b7ef.png">
</p>

### <a name="download_ref"></a> Download reference
See the download references manual on how to obtain refseq and genbank ftp links.

1. Click _Download reference_ under Reference tools.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/140946916-79a2b2ad-7e1d-497d-8fca-8c0c686bd426.png">
</p>


2. Fill out the form and click _Download_

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141085401-97dc55f6-6492-4048-8a25-cc28fb40c366.png" width="500" height="200">
</p>




See description of fields here:

| Field	| Description |
| --- | --- |
|   **Download link** |   ftp or http link pointing to reference file  |
|   **Save path** |   Main directory to save the downloaded reference in  |
|   **Subdirectory**   |   Generate new subdirectory in main directory   |

3. It will run immediately. 

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141086040-eeb94fcd-73ee-4265-bea4-9e3a6f39048c.png" width="500" height="200">
</p>



### <a name="download_annot"></a> Download annotations
1. Click _Download annotation_ under Reference tools.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/140947894-9a9fe0c3-c2a9-48e9-b3f6-243ad25992bb.png" >
</p>


2. Fill out the form and click _Download_

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141086252-25cb975d-891b-4ab1-a2a8-09ce9e4b49de.png" width="500" height="180" >
</p>



See description of fields here:

| Field	| Description |
| --- | --- |
|   **Download link** |   ftp or http link pointing to annotation file  |
|   **Save path** |   Directory to save the downloaded annotation in  |


3. It will run immediately. 

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141086954-644a4237-fde0-46bc-8c88-45fa5c0c139d.png" width="500" height="180" >
</p>




### <a name="merge_scaffold"></a> Merge scaffolds
Many genomes consist of the primary assembly and scaffolds, or entirely of scaffolds, i.e. the human genome consists of 24 sequences in the primary assembly and >600 scaffold (alternative references) sequences. It can quickly become meaningless to map to this many scaffolds, and therefore it is recommended to merge the scaffolds to avoid  ‘losing’ information by not including the them. It is also recommended to use merge scaffolds if your assembly only contains scaffolds and contigs.
A bed-like file will be generated for the merged scaffolds, containing the position and name of the original scaffold as a feature. 

If your reference contains a primary assembly, create a list of these chromosome names. 

1. Click _Merge scaffolds_ under Reference tools.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/140949105-7c807896-a3bf-42f6-8074-8ba6953252a7.png" >
</p>



2. Fill out the form and click _Next_

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141087105-a6fc3b0f-d6e2-4788-b9e1-c3e0cf00eb1f.png" width="500" height="180">
</p>



See description of fields here:

| Field	| Description |
| --- | --- |
|   **Reference file** |   Path to reference file  |
|   **Save path** |   Main directory to save the downloaded reference in  |

3. Fill out the rest of the form and click _Run_

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141087524-857df035-d897-4d42-ba3a-435259661b14.png" width="500" height="500" >
</p>


See description of fields here:

| Field	| Description |
| --- | --- |
|   **Change output file name** |   Optional. Change name of output file. Default is REFERENCE_scaffold_merged.fasta  |
|   **Extract primary assembly** |   Optional. Provide a list of the primary assembly to extract  |
|   **Change size limit** |   Default size limit is 2^29 (536970912) bp. Samtools cannot use bai index for sizes above this limit. |
                                                                                                                                     


4. It will run immediately. 

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141087811-187c1107-2806-4350-9375-b26e97118796.png" width="500" height="500" >
</p>


5. Continue to prepare reference

### <a name="prep_ref"></a> Prepare reference

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
<img src="https://user-images.githubusercontent.com/60882704/141087988-0c109442-9f17-4dcd-a8b5-19b55a574abc.png" width="500" height="180">
</p>


See description of fields here:

| Field	| Description |
| --- | --- |
|   **Reference file** |   Path to reference file  |
|   **Save path** |   Main directory to save the downloaded reference in  |

3. Fill out the rest of the form and click _Run_

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141088943-cab71032-e08d-4edb-85d1-0d42b5356bac.png" width="500" height="560">
</p>



See description of fields here:

| Field	| Description |
| --- | --- |
|   **Index reference for use in IGV** |   Optional. An indexed reference file is required for viewin in IGV. Is significantly faster than indexing locally. |
|   **Create BWA index for ILMN** |   Optional. BWA index is required when running the ILMN enrichment mapping report pipeline. This is time consuming  |
|   **Change size limit** |   Default size limit is 2^29 (536970912) bp. Samtools cannot use bai index for sizes above this limit. |
|   **Extract primary assembly** |   Optional. Provide a list of the primary assembly to extract  |
|   **Rename extracted assembly** |   Optional. Requires extraction of primary assembly. Provide a list of the new names to be used.  |
|   **Keep merged scaffolds** |   Optional. Keep merged scaffolds without haveing to provide them in the lists  |
4. It will run immediately. 

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141089527-872d8c14-5d2c-4361-b0f1-2eabc301dfb3.png" width="500" height="500">
</p>

5. Continue to Enrichment mapping report

## <a name="analysis_tools"></a> Analysis tools

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138286397-c3b80ca1-e9f6-491f-9359-e161d059b903.png" >
</p>

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/140943620-3b8f012d-b5ce-4a42-9dec-36e229c6276f.png" >
</p>


### <a name="enrich_report"></a> Enrichment mapping report
The enrichment mapping report pipeline can be performed on both ILMN and ONT fastq files. The majority of the pipeline is the same, however, there are some slight differences prior to mapping. FastQC is performed on ILMN fastq files before and after trimming with trimmomatic as a QC measure. The outputs are run reports in html format.

Mapping is performed with minimap2 and bwa-mem for ONT and ILMN data, respectively, with standard parameters and output in SAM format. After mapping, SAMtools is used to convert the SAM file into a compressed binary SAM format: BAM. The BAM file is subsequently manipulated in SAMtools. Read lengths are obtained for the different target regions (ROI, customizable region and 10 kb regions) using awk. Softclipped regions are obtained using our own python scripts. Genome coverage is obtained using Qualimap. BAM files and statistics obtained from SAMtools, together with sequence lengths and genome coverage are processed in R, utilizing our own Rscript. This generates the figures and table incorporated into the reports. The reports are generated using docx-tpl and soffice.

1. Click _Enrichment mapping report_ under Analysis tools.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141082242-92800276-fff9-4aea-89e3-5fe0cdb87ffe.png" >
</p>


2. Click on Create ONT or ILMN config file or upload existing config file: 

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141082788-c53ea930-f7c6-4cc3-9b81-4f269ad0ae2d.png" >
</p>



3. Fill out the form.

* Report parameters:

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141092977-c34649bc-c068-4776-85ce-1513557fdb00.png" width="500" height="200">
</p>



   * File paths for ONT or ILMN

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141093267-0a800060-8ed4-4447-983b-780a3f3611a9.png" width="1000" height="250">
</p>


   * Region of Interest:

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141093503-8d3cd64c-8ceb-4369-af6b-f4edf4b5437c.png" width="500" height="450">
</p>


   * Other settings

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141094855-55f1b332-eaae-4079-8fa5-02533531d46e.png" width="500" height="270">
</p>



   * Advanced Settings for ONT or ILMN

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141095942-fa5001e3-f01f-4979-8028-779bbe22cb4f.png" width="1000" height="300" >
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
| **Bed file path** | Path to bedfile for chromosome of interest  |
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

4. Click _Create config file_.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141096613-d8f3b23f-06ce-486b-ba40-64309a8f6460.png" width="500" height="560" >
</p>


5. Click _Run the pipeline_ to run the enrichment mapping report pipeline. An e-mail will be sent upon completion

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138112094-da2ddfd4-120b-4ded-947b-435f33d1a40f.png" >
</p>


### <a name="add_tags"></a> Add tags to alignment
Two tags are currently possible: read name (RG) and all chromosomes which each read aligns to (RZ), e.g. if read A maps to chr_01, chr_05, and chr_08, the tag will be chr_01;chr_05;chr_08. This tag will be added to each instance of read A present in the S/BAM alignment file. Using these two tags, this allows for coloring by read name (enabling to see chimeric reads) and grouping alignments by chromosomes. This is highly useful when working with inserts.

Coloring by readname (tag RG) and grouping by chromosome (tag RZ): 

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/129158273-87011e96-d639-4697-8f76-495424ccf022.png" >
</p>

Viewing reads mapped to insertion sequence and comparing to reads mapped to chromosome 18:

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/129162641-04091ff4-a106-4ee1-9b1e-4f3fc9c3a8d1.png" >
</p>


**To run the add tags to alignment:**

1. Click _Add tags to alignment_ under Analysis tools.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138288954-870c68ed-d570-4390-85ea-eb5de3d96eaa.png" >
</p>


2. Fill out the form.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138087564-41cc304d-cfd0-4429-adfc-8fd18a76dab7.png" >
</p>



See description of fields here:

| Field	| Description |
| --- | --- |
| **BAM or SAM file** | Path to BAM or SAM file |
| **Read name tags** | Use read names as tags |
| **Aligned chromosome tags** | Use aligned chromosomes as tags |


