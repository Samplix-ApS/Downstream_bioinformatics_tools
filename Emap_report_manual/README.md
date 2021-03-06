## Table of Contents
- [Introduction](#descript_)
- [Trimming with trimmomatic](#trim_)
- [Mapping to reference](#map_ref)
  - [Minimap2](#ont_minimap2)
  - [BWA MEM](#ilmn_bwa)
- [SAMtools](#samtools_)
- [Qualimap: Calling genome coverage](#quali_cov)
- [Generated files](#output_files_)
- [Generated table](#output_table_)
- [Definition of terms](#dict_terms_)
- [References](#ref_)
- [Trouble shooting](#help_)
- [Authors](#authors_)

# <a name="descript_"></a> Introduction
The analysis pipeline can be performed on both Illumina (ILMN) and Oxford Nanopore Technologies (ONT) fastq files ([Figure 1](#fig1)). The majority of the pipeline is the same, however, there are some slight differences prior to mapping. FastQC is performed on ILMN fastq files before and after trimming with trimmomatic as a QC measure. The outputs are run reports in html format which can be found in the output folder. 

Mapping is performed with [minimap2](https://github.com/lh3/minimap2) and [bwa-mem](http://bio-bwa.sourceforge.net/bwa.shtml) for ONT and ILMN data, respectively, with standard parameters and output in SAM format (See [SAMtools](http://www.htslib.org/doc/samtools.html)). After mapping, SAMtools is used to convert the SAM file into a compressed binary SAM format: BAM. The BAM file is subsequently manipulated in SAMtools. Genome coverage is obtained using [Qualimap](http://qualimap.conesalab.org/). BAM files are process in R. This generates the figures and table incorporated into the reports. The report are generated using docx-tpl and soffice. 

<a name="fig1"></a>
<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/141495039-59b71acd-c4d4-4686-a94b-af54fab9e490.png">
</p>

**Figure 1 – Flow-chart of Enrichment mapping report pipeline.**

# <a name="trim_"></a>Trimming with trimmomatic
The current analysis pipeline consists of first trimming the ILMN fastq files using Trimmomatic, supposing that the adaptor sequences have already been removed, with the following settings:
* Remove leading low quality or N bases (below quality 3)
* Remove trailing low quality or N bases (below quality 3)
* Scan the read with a 4-base wide sliding window, cutting when the average quality per base drops below 15
* Drop reads below 36 bases long


# <a name="map_ref"></a>Mapping to reference
## <a name="ont_minimap2"></a> Minimap2
The standard pipeline uses minimap2 to map ONT read to reference with standard settings. However, it is possible to change those setting using the parameter field.
See [minimap2 manual]((https://github.com/lh3/minimap2)) for parameters
The chimeric alignments are ‘stored’ as supplementary alignments.

## <a name="ilmn_bwa"></a> BWA MEM
The standard pipeline uses BWA MEM to map ILMN reads to reference with standard settings.
However, it is possible to change those settings using the parameter field.
See [BWA manual]((http://bio-bwa.sourceforge.net/bwa.shtml)) for parameters.
The chimeric reads are likely ‘thrown out’.


# <a name="samtools_"></a> SAMtools
The sequence Alignment/Map (SAM) is a file format to save alignment information of reads mapped against reference sequences. BAM is the binary format of SAM.
The SAM header ([Figure 2](#fig2)) for each read alignment has 11 mandatory fields for essential alignment information, such as read name, SAM flag, chromosome, position, MAPQ, CIGAR, name of mate, position of mate, template length, read sequence and read quality. A SAM flag of 0, 4 and 16 all indicate unpaired reads (this expected for ONT data), which map to the forward strand (0), reverse strand (16) or does not map (4). Reads that do not map will have an * in the chromosome field. Mapping quality (MAPQ) equals −10 log10 Pr{mapping position is wrong}, rounded to the nearest integer, and describes the uniqueness of the alignment. A value of 255 indicates that the mapping quality is not available. minimap2 and BWA-MEM both operate with a scale from 0-60. The CIGAR (Compact Idiosyncratic Gapped Alignment Report) string is how the SAM/BAM format represents spliced alignments.

<a name="fig2"></a>
<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/129384826-e6a52761-c89c-4f31-bbcc-4dc54a03f5ec.png">
</p>

**Figure 2 – SAM header after mapping with minimap2.**

# <a name="quali_cov"></a>Qualimap: Calling genome coverage
Qualimap is a platform-independent application written in Java and R. It provides fast analysis across the reference genome of mapping coverage. It gives similar results as BEDtools genomecov, however is tremendously faster. 

# <a name="output_files_"></a>Generated files
| File name | Description|
|---|---|
| output_forward_paired.fq.gz (ILMN) |	Trimmed fastq file containing only forward paired end reads | 
| output_reverse_paired.fq.gz (ILMN) |	Trimmed fastq file containing only reverse paired end reads |
| output.sort.bam  |	Sorted bam file containing all read mappings, including supplementary, secondary and unmapped reads |
| prim.map.Chr.sort.bam	| Sorted bam file containing primary reads for target chromosome |
| prim.map.ROI.bam	| Bam file containing primary reads for ROI |
| prim.map.RoT100.sort.bam |	Sorted bam file containing primary reads for customizable region |
| prim.map.RoT10.1.bam	| Bam file containing primary reads for 10 kb region around detection sequence |
| prim.sup.map.Chr.sort.bam |	Sorted bam file containing primary and supplementary reads for target chromosome |
| prim.sup.map.sort.bam |	Sorted bam file containing primary and supplementary reads |

# <a name="output_table_"></a>Generated table

| Title | Definition |
|---|---|
|Total bases sequenced (bp)| Sum of bases found in the provided input file |
|Total reads (reads) | Sum of reads found in the provided input file |
| Total mapped reads (reads) | Sum of reads that mapped primary to the provided reference |
| Total reads mapped to custom region (reads) | Sum of reads that mapped primary to the custom region  | 
| Total reads mapped to 10 kb region | Sum of reads that mapped primary to the 10 kb region | 
| Total reads mapped to ROI (reads) | Sum of reads taht mapped primary to the provided region of intereste (ROI) |
| Percentage mapped reads to reference (%) | Total mapped reads divided by total reads | 
| Percentage mapped reads to custom region (%) | Total reads mapped to custom region divided by total mapped reads | 
| Percentage mapped reads to 10 kb region(%) | Total reads mapped to 10 kb region divided by total mapped reads |
| Percentage mapped reads to ROI (%) | Total reads mapped to ROI divided by total mapped reads |
| Percentage of bases mapped primary (%) | Sum of bases in the aligned part of the reads which mapped primary (ergo, sum of bases in primary mapped reads without the sofclipped parts)
| Percentage of bases mapped primary incl. suppl. (%) | Sum of bases in the algined part of the reads which mapped primary or supplementary (ergo sum of bases in primary and supplementary reads without the softclipped parts)
| Enrichment custom region (fold) | Sequencing enrichment for the custom region |
| Enrichment 10 kb region (fold)  | Sequencing enrichment for the 10 kb region |
| Enrichment ROI (fold) | Sequencing enrichment for the ROI  |
| N50 mapped readlength (bp) | N50 for the  mapped primary reads |
| N50 custom region readlength (bp) | N50 for the custom (default 100 kb) region mapped primary reads  |
| N50 10 kb region readlength (bp) | N50 for the 10 kb region  |
| N50 ROI readlength (bp) | N50 for the ROI mapped primary reads |
| Median mapped readlength (bp) | Median readlength of the primary mapped reads to reference |

# <a name="dict_terms_"></a>Definition of terms

|Term | Definition |
|---|---|
|	10 kb region 	|	5 kb region to either side of the provided detection assay. Calculated for each provided detection assay		|
|	Aligning 	|	Mapping or alignment is the process of aligning reads to a reference genome. A mapper (e.g. minimap2), takes as input a reference genome and the reads. It aims to align each read to the reference genome, allowing for mismatches, indels and softclipping (at the beginning and end of the read). The mapper calculates an alignment score based on matches (usually the longer the stretch of matches, the better the score), and penalizes for introduction of mismatches and indels. The mapper also calculates a mapping score based on how confident it is that the read comes from the reported position. 		|
|	Alignment score 	|	Alignment is finding the exact diference between two sequences. The mapper calculates the alignment score bases on matches (usually the longer the stretch of matches, the better the score) and penalizes for the introduction of mismatches and indels. 		|
|	Custom region	|	Custom region provided by the user. Default is 50 kb to either side of the first provided detection assay		|
|	Mapper	|	Alignment or mapping software such as minimap2 (for long reads) and BWA (for short reads)		|
|	Mapping	|	See aligning 		|
|	Mapping score 	|	Mapping is finding the approximate origin of a sequence. The mapper assignes mapping scores based on the confindence it has in that the read comes from the reported position. Ergo multimapping reads will often have low mapping scores, as the mapper cannot determine the origin of the read  		|
|	N50	|	50% quartile of the cummulative sum of read lengths 		|
|	Primary alignment 	|	Usually the alignment with the best alignment and mapping score.  		|
|	Raw read 	|	A read for which there is no alignment or mapping information, ergo it is not known if the read aligns to a reference 		|
|	Read 	|	A read is an inferred sequence of bases corresponding to a DNA fragment obtained from a sequencing device. 		|
|	ROI	|	Region of interest as defined and provided by the user		|
|	Secondary alignment 	|	A read may align ambiguously to multiple locations in the reference. Only one of the multiple read alignments is considered primary, usually the one with the best alignment score and mapping score. All other alignments are considered secondary .  		|
|	Sequencing enrichment	|	Percentage of target mapped reads divided by the target size over the reference genome size		|
|	Softclipping 	|	Bases in the 5' and 3' of the reads which are not part of the alignment at the mapped position. For chimeric reads, the supplementary alignments are usally found in the softclipped parts of the primary alignments 		|
|	Supplementary alignment 	|	Supplementary alignments contain the chimeric alignments, which are represented as a set of linear alignment that do no have large overlaps. Typically one linear alignment is considered the representative alignment (usually the one with the highest alignments and mapping score), and is designated as the primary alignment, the remainder become supplementary alignments.  		|



# <a name="ref_"></a>References
Minimap2: https://lh3.github.io/minimap2/minimap2.html

BWA: http://bio-bwa.sourceforge.net/bwa.shtml

SAMtools: http://www.htslib.org/doc/samtools.html

Qualimap: http://qualimap.conesalab.org/



# <a name="help_"></a> Trouble shooting
Contact bioinformatics@samplix.com

# <a name="authors_"></a> Authors
Camille Johnston (CAJ)

Qammar Abbas (QAB)
