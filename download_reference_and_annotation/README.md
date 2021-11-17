# Download references and annotations
## Table of Contents
[User's Guide](#uguide)
- [Download references](#download_ref)
- [Download annotations (GFF)](#download_gff)
- [Primary assembly extraction and renaming](#prim_)
- [Troubleshooting](#help_)
- [Authors](#authors_)
# <a name="uguide"></a> User's Guide
## <a name="download_ref"></a> Download reference
If you do not already have a reference, you can use the [download reference tool](https://github.com/Samplix-ApS/Bioinformatics_tools#download_ref).

It is possible to download the desired reference sequence directly onto the server through ftp. Navigate to the desired reference.
For example the human genome build 38 patch 13 (GRCh38.p13 also known as hg38) on NCBI.
1. click on the “FTP directory to RefSeq assembly:

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141118095-3c53cfcc-fec9-41d5-b9b2-1aedd4e523c0.png">
</p>


2. Right click on the genomic.fna.gz file and copy the link:

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141118154-39fd1eb5-20d2-4a22-aeb1-479f2d485e1b.png">
</p>



3. In docker follow the [**download reference instructions**](https://github.com/Samplix-ApS/Bioinformatics_tools#download_ref)

## <a name="download_gff"></a> Download annotation
If you need annotations for your reference and you do not already have them, then you can use the [download annotation tool](https://github.com/Samplix-ApS/Bioinformatics_tools#download_annot).

It is possible to download the desired reference annotation directly onto the server through ftp. Navigate to the desired reference.
For example the human genome build 38 patch 13 (GRCh38.p13 also known as hg38) on NCBI.
1. click on the “FTP directory to RefSeq assembly:

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141118095-3c53cfcc-fec9-41d5-b9b2-1aedd4e523c0.png">
</p>


2. Right click on the genomic.gff.gz file and copy the link:

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141123419-8aad4251-6c78-409b-b066-984c509248ff.png">
</p>




3. In docker follow the [**download annotation instructions**](https://github.com/Samplix-ApS/Bioinformatics_tools#download_annot)

## <a name="prim_"></a> Primary assembly extraction and renaming
If you wish to extract or change the names of the primary assembly in your reference while using [merge scaffolds](https://github.com/Samplix-ApS/Bioinformatics_tools#merge_scaffold) or [prepare reference](https://github.com/Samplix-ApS/Bioinformatics_tools#prep_ref) follow the instructions below.

The chromosomes in the reference usually use the RefSeq sequence nomenclature. To obtain the names for the primary assembly:
1. Click on the “FTP directory to RefSeq assembly:

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141118095-3c53cfcc-fec9-41d5-b9b2-1aedd4e523c0.png">
</p>


2. Click on the assembly_report:
<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141118793-246eef0a-3c84-471e-8cb1-73a399e8363b.png">
</p>


3. Copy the _assembled-molecule_ records and paste in a text editing program or excel.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141120784-dbf21cdd-f344-4ab9-a91f-b5d18dfb1385.png">
</p>

4. Copy and paste/save the primary assembly RefSeq names to use for extraction of primary assembly in [**prepare reference**](https://github.com/Samplix-ApS/Bioinformatics_tools#prep_ref) or [**merge scaffolds**](https://github.com/Samplix-ApS/Bioinformatics_tools#merge_scaffold):

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141122522-d69a9c89-6017-4ee4-ad59-9a36c8c27167.png">
</p>


5. Copy and paste/save the UCSC style names to rename the primary assembly in [**prepare reference**](https://github.com/Samplix-ApS/Bioinformatics_tools#prep_ref):

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141122611-af97ad21-8905-4233-bd22-97b0f56965ed.png">
</p>

## <a name="help_"></a> Troubleshooting
Contact bioinformatics@samplix.com

## <a name="authors_"></a> Authors
Camille Johnston (CAJ)

Qammer Abbas (QAB)
