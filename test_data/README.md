# Test data set

## Table of Contents
- [Overview](#descript_)
- [Assay information](#assay_info)
- [Generated reports](#reports_)
  - [Basecalling report](#basecalling_report_) 
  - [FastQC reports](#fastqc_reports_)
  - [Enrichment mapping report](#enrichment_report_)
- [Troubleshooting](#help_)
- [Authors](#authors)

# <a name="descript_"></a> Overview
Below you will find an enriched TP53 test data set you can use to test the pipeline. 

All data can be found publically available on our S3 server:
[**test-data**](http://samplix-public-data.s3-website.eu-central-1.amazonaws.com/?prefix=public-data/test_data/)

| File name | Seq type | File format | Size | Note |
| --- | --- | --- | --- | --- |
| fast5.zip | ONT | fast5 | 9.9 GB | Library constructed with ligation sequencing kit (SQK-LSK109) </br> No barcodes.|
| fastq_ont.zip | ONT | fastq | 762 MB | |
| fastq_ilm.zip | ILMN | fastq | 1.4 GB | Paired-end. |



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

[**basecalling_report.html**](http://samplix-public-data.s3-eu-central-1.amazonaws.com/public-data/test_data/reports/basecalling_report.html)

## <a name="fastqc_reports_"></a> FastQC reports
FastQC report pre- and post-trim of ILMN fastq:

[**ILMN_fastqc_reports**](http://samplix-public-data.s3-eu-central-1.amazonaws.com/public-data/test_data/reports/ILMN_fastqc_reports.zip)

## <a name="enrichment_report_"></a> Enrichment mapping report
### ONT: Enrichment mapping report

Size: 1.1 mb

[**emap_ONT_report.pdf**](http://samplix-public-data.s3-eu-central-1.amazonaws.com/public-data/test_data/reports/emap_ONT_report.pdf)

### ILMN: Enrichment mapping report

Size: 959 kb

[**emap_ILMN_report.pdf**](http://samplix-public-data.s3-eu-central-1.amazonaws.com/public-data/test_data/reports/emap_ILMN_report.pdf)


# <a name="help_"></a>Troubleshooting
Contact bioinformatics@samplix.com

# <a name="authors"></a>Authors
Camille Johnston

