# Test data set

## Table of Contents
- [Description](#descript_)
- [FAST5](#fast5_)
- [FASTQ](#fastq_)
  - [ONT](#ont_fastq_)
  - [ILMN](#ilmn_fastq_)
- [Assay information](#assay_info)
- [Generated reports](#reports_)
  - [Basecalling report](#basecalling_report_) 
  - [FastQC reports](#fastqc_reports_)
  - [Enrichment mapping report](#enrichment_report_)
- [Troubleshooting](#help_)
- [Authors](#authors)

# <a name="descript_"></a> Description
Below you will find an enriched TP53 test data set you can use to test the pipeline. 

# <a name="fast5_"></a> FAST5
Library constructed with ligation sequencing kit (SQK-LSK109) and no barcodes.

Size: 9.9 GB

[**fast5.zip**](https://samplix-public-data.s3.amazonaws.com/public-data/test_data/fast5.zip)

# <a name="fastq_"></a> FASTQ
## <a name="ont_fastq_"></a> ONT
Size: 782 MB.

[**fastq_ont**](https://s3.amazonaws.com/samplix-public-data/public-data/test_data/fastq_ont)

## <a name="ilmn_fastq_"></a> ILMN
Library type: Paired-end.

Size: 1.4 gb.

[**fastq_ilmn.zip**](https://samplix-public-data.s3.amazonaws.com/public-data/test_data/fastq_ilmn.zip)

# <a name="assay_info"></a> Assay information

| |Info|
| --- | --- |
| **Target** | TP53 |
|	**Genome**	|	GRCh38.p13	|
|	**ROI chromosome**	|	Chr_17	|
|	**ROI start**	|	7668402	|
|	**ROI end**	|	7687550	|
|	**Detection sequence start**	|	7675778	|
|	**Detection sequence end**	|	7675939	|
|	**Validation sequence start**	|	7673906	|
|	**Validation sequence end**	|	7674109	|


# <a name="reports_"></a> Generated reports
## <a name="basecalling_report_"></a> Basecalling report
Basecalling report generated using pycoQC

[**basecalling_report.html**](https://samplix-public-data.s3.amazonaws.com/public-data/test_data/reports/basecalling_report.html)

## <a name="fastqc_reports_"></a> FastQC reports
FastQC report pre- and post-trim of ILMN fastq:

[**ILMN_fastqc_reports**](https://samplix-public-data.s3.amazonaws.com/public-data/test_data/reports/ILMN_fastqc_reports.zip)

## <a name="enrichment_report_"></a> Enrichment mapping report
### ONT: Enrichment mapping report

Size: 1.1 mb

[**emap_ONT_report.pdf**](https://samplix-public-data.s3.amazonaws.com/public-data/test_data/reports/emap_ONT_report.pdf)

### ILMN: Enrichment mapping report

Size: 959 kb

[**emap_ILMN_report.pdf**](https://samplix-public-data.s3.amazonaws.com/public-data/test_data/reports/emap_ILMN_report.pdf)


# <a name="help_"></a>Troubleshooting
Contact bioinformatics@samplix.com

# <a name="authors"></a>Authors
Camille Johnston

