# Viewing BAM files in IGV
## Table of Contents
[User's guide](#uguide)
- [Description](#descrip_)
  - [Dependencies](#depend_) 
- [IGV: View BAM](#view_bam)
- [IGV: Sort and index BAM file](#sort_index)
- [IGV: Adding a new reference](#add_ref)
- [IGV: Custom bed track](#custom_bed)
- [IGV: Add annotation file (GFF)](#add_annot)
  - [Load annotation file](#load_annot)
  - [Rename chromosomes in annotation file](#rename_chromo)
  - [Sort and index annotation file for IGV](#sort_index_anno)
  - [Bundle reference and annotations](#bundle_gff)
- [Add tags to alignment](#add_tag)  
  - [IGV: View tags](#add_tag_view)   
- [References](#refs)
- [Trouble shooting](#help_)
- [Authors](#authors_)

# <a name="uguide"></a> User's Guide
## <a name="descrip_"></a> IGV
IGV, integrative genomics viewer, is a high-performance, easy-to-use, interactive tool for the visual exploration of genomic data. It supports flexible integration of all the common types of genomic data and metadata, investigator-generated or publicly available, loaded from local or cloud sources.

BAM files can be viewed in IGV with associated annotation files. However, it can sometimes be necessary to process the bam and annotation file beforehand. 
### <a name="depend_"></a> Dependencies
* IGV installed locally

## <a name="view_bam"></a> IGV: View BAM file
Load the BAM in **File->Load** from file. It is not necessary to load the associated index, as IGV locates it automatically.
To view a BAM file it must be sorted and indexed using samtools (SAMtools sort and index).
Transfer the BAM file and its associated bai/csi index (_BAM.bai/BAM.csi_) from the server, or use IGV itself to sort and index. 


## <a name="sort_index"></a> IGV: Sort and index BAM file
To sort and index a BAM file in IGV:
1. navigate to Tools-> Run igv tools.
<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/129716605-97944763-af2e-48ad-900f-c5eba36b7f60.png">
</p>

2. In _command_ choose _Sort_ and select the BAM file as input file. Click run.
<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/129716688-b26d5774-171d-4e1e-b9b6-c13c2ec29a93.png">
</p>


3. To index, choose the newly made sorted file (not the same as the previous input file), select _Index_ in the command, and run. 
<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/129716766-78ada9b2-4b5c-44bb-9400-fc996eeb7537.png">
</p>


4. Now load the sorted BAM file into IGV, _File->Load from file_.

## <a name="add_ref"></a> IGV: Adding a new reference
To add a new reference genome to IGV navigate to Genomes -> Load genomes from file.
IGV automatically indexes a new reference sequence. This can take a good while if the reference is large. Until the reference is indexed, the chromosomes of the loaded genome will not be shown. It can seem as if the program is stalling or has crashed, but it is just indexing. It is possible to save time by indexing the reference yourself, using _samtools faidx_ on the server.
```
samtools faidx REFERENCE 
```
This outputs _REFERENCE.fai_. Transfer this file from the server into the same local location as the reference. 
## <a name="custom_bed"></a> IGV: Custom bed track
It is possible to add your own custom bed file track to IGV. IGV bed files use a zero-based index. The start and end positions are identified using a zero-based index, so the end position is excluded. For example, setting start-end to 1-2 describes exactly one base, the second base in the sequence. The first base would be 0-1.

1. The bed file must contain 4 tab-delimited columns: 
    1) name of chromosome
    2)  start position (zero-based position)
    3)  end position (zero-based)
    4)  name of region. 
2. creating two separate bed files, one containing the dPCR and qPCR coordinates, and one containing the region(s) of interest:
<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/129717223-0f85e5a2-8447-4336-9755-6228923460e1.png">
</p>


3. Load the bed files in File->Load from file

4. Once the bed files have been loaded, the colors can be changed by right clicking on the track and choosing ‘Change track color’.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/129717304-c0009ee7-6cb8-4771-9012-7295fe4bd2d9.png">
</p>

## <a name="add_annot"></a> IGV: Add annotation file (GFF)
### <a name="load_annot"></a>Load annotation file
See [download reference and annotations](https://github.com/Samplix-ApS/Bioinformatics_tools/tree/main/download_reference_and_annotation) in the repository to download to server.

1. In IGV navigate to _File->Load from file_ and load the annotation.gff.gz file. This can take a while depending on the size of the annotation file.
<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/135452336-925eeccf-d2a8-4a21-856e-23793ace0dc7.png">
</p>

### <a name="rename_chromo"></a>Rename chromosomes in annotation file
If the names of the primary assembly/chromosomes have been changed in the reference sequence, it is necessary to also change the names in the annotation file.

Use the following command:
```
python3 /webutility/scripts/gff_rename.py -i ANNOTATION_FILE -c chromosome_names -r replacement_name <optional>
```
It can be run with the following parameters:
```
-i      input annotation file in GFF format
-c      list of chromosome names present in the annotation file
-r      list of replacement names which will rename the chromosomes provided with -c
-o      output file name in .gff or .gff.gz
-d      desitination folder
```

### <a name="sort_index_anno"></a>Sort and index annotation file for IGV
If the annotation file is not gzipped (.gz) it can be necessary to sort and index it for use in IGV.
Follow the steps as above for sorting and indexing a BAM file, just use a .gff file instead.

### <a name="bundle_gff"></a>Bundle reference and annotations
It is possible to 'bundle' the reference genome and annotations together using IGV's _Create .genome File_ found in the _Genomes_ tab.
1. Click _Create .genome File_ and fill out the _Unique identifier_, _Descriptive name_ (what will be shown as the name in IGV), _FASTA file_ location, and _Gene file_ (annotation file)
<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/135479745-97379879-f948-4d8f-8688-37a3f0fc5a5b.png" width="500" height="250">
</p>

2. Click OK and save the file.
3. The genome file should be loaded into IGV. Depending on size, this can take a while. You can follow how much has been loaded in the lower right hand corner. 

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/135485752-5bbccf87-cb41-45ac-916a-8cc6c5f54940.png">
</p>

## <a name="add_tag"></a> Add tags to alignment
[Add tags to alignment](https://github.com/Samplix-ApS/Bioinformatics_tools#add_tags) (SAM/BAM) files to ease viewing in IGV. Especially useful when working with pseudogenes and inserts.
Two tags are currently possible: read name (RG) and all chromosomes which each read aligns to (RZ), e.g. if read A maps to chr_01, chr_05, and chr_08, the tag will be chr_01;chr_05;chr_08. This tag will be added to each instance of read A present in the S/BAM alignment file. 
Using these two tags, this allows for coloring by read name (enabling to see chimeric reads) and grouping alignments by chromosomes. This is highly useful when working with inserts. 

Coloring and grouping by readname (tag RG):

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138087564-41cc304d-cfd0-4429-adfc-8fd18a76dab7.png" width="300" height= "300">
</p>


Coloring and grouping by chromosome (tag RZ):

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138087564-41cc304d-cfd0-4429-adfc-8fd18a76dab7.png" width="300" height= "300">
</p>


Coloring by readname (tag RG) and grouping by chromosome (tag RZ): 

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138087564-41cc304d-cfd0-4429-adfc-8fd18a76dab7.png" width="300" height= "300">
</p>

Viewing reads mapped to insertion sequence and comparing to reads mapped to chromosome 18:

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/138087564-41cc304d-cfd0-4429-adfc-8fd18a76dab7.png" width="300" height= "300">
</p>

### <a name="add_tag_view"></a> IGV: View tags
In IGV it is recommended to color by tag RG (read name) and group by tag RZ (mapped chromosomes). Sometimes it is necessary to group by tag RG, color by tag RG, and then group by tag RZ to get correct colors out. 

To view two different sites in the alignment, it is recommended to save the IGV session, close it, and open two new seperate windows. It is necessary to save, as the colors change upon saving, however, grouping is not affected. 

## <a name="refs"></a> References
[IGV](http://software.broadinstitute.org/software/igv/UserGuide)

[SAMtools](http://www.htslib.org/doc/samtools.html)

## <a name="help_"></a> Trouble shooting
Contact CAJ

## <a name="authors_"></a> Authors
Camille Johnston (CAJ)
