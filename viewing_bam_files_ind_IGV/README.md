# Viewing BAM files in IGV
## Table of Contents
[User's guide](#uguide)
- [Description](#descrip_)
- [IGV: Sort and index BAM file](#sort_index)
- [IGV: Adding a new reference](#add_ref)
- [IGV: Custom bed track](#custom_bed)
- [References](#refs)
- [Trouble shooting](#help_)
- [Authors](#authors_)

# <a name="uguide"></a> User's Guide
## <a name="descrip_"></a> IGV
IGV, integrative genomics viewer, is a high-performance, easy-to-use, interactive tool for the visual exploration of genomic data. It supports flexible integration of all the common types of genomic data and metadata, investigator-generated or publicly available, loaded from local or cloud sources.

To view a BAM file it must be sorted and indexed using samtools (SAMtools sort and index). Transfer the BAM file and its associated bai/csi index (_BAM.bai/BAM.csi_) from the server, or use IGV itself to sort and index. 
Load the BAM in **File->Load** from file. It is not necessary to load the associated index, as IGV locates it automatically.

## <a name="sort_index"></a> IGV: Sort and index BAM file
To sort and index a BAM file in IGV, navigate to Tools-> Run igv tools.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/129716605-97944763-af2e-48ad-900f-c5eba36b7f60.png">
</p>

In command choose sort and select the BAM file as input file. Click run.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/129716688-b26d5774-171d-4e1e-b9b6-c13c2ec29a93.png">
</p>

To index, choose the newly made sorted file (not the same as the previous input file), select index in the command, and run. 

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/129716766-78ada9b2-4b5c-44bb-9400-fc996eeb7537.png">
</p>

Now load the sorted BAM file into IGV, File->Load from file.

## <a name="add_ref"></a> IGV: Adding a new reference
To add a new reference genome to IGV navigate to Genomes -> Load genomes from file.
IGV automatically indexes a new reference sequence. This can take a good while if the reference is large. Until the reference is indexed, the chromosomes of the loaded genome will not be shown. It can seem as if the program is stalling or has crashed, but it is just indexing. It is possible to save time by indexing the reference yourself, using _samtools faidx_ on the server.
```
samtools faidx REFERENCE 
```
This outputs _REFERENCE.fai_. Transfer this file from the server into the same local location as the reference. 
## <a name="custom_bed"></a> IGV: Custom bed track
It is possible to add your own custom bed file track to IGV. IGV bed files use a zero-based index. The start and end positions are identified using a zero-based index, so the end position is excluded. For example, setting start-end to 1-2 describes exactly one base, the second base in the sequence. The first base would be 0-1.
The bed file must contain 4 tab-delimited columns:
1) name of chromosome, 2) start position (zero-based position), 3) end position (zero-based), 4) name of region.
E.g. creating two separate bed files, one containing the dPCR and qPCR coordinates, and one containing the region(s) of interest:

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/129717223-0f85e5a2-8447-4336-9755-6228923460e1.png">
</p>

Load the bed files in File->Load from file
Once the bed files have been loaded, the colors can be changed by right clicking on the track and choosing ‘Change track color’.

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/129717304-c0009ee7-6cb8-4771-9012-7295fe4bd2d9.png">
</p>

## <a name="refs"></a> References
IGV: [http://software.broadinstitute.org/software/igv/UserGuide](url)
## <a name="help_"></a> Trouble shooting
Contact CAJ

## <a name="authors_"></a> Authors
Camille Johnston (CAJ)
