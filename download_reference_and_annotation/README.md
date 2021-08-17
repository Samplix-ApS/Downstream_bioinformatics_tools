# Download references
## Table of Contents
[User's Guide](#uguide)
- [Download references](#download_ref)
  - [Genbank references](#genbank_ref)
    - [Obtaining primary chromosomes names](#obtain_names)
  - [Custom references](#custom_ref) 
- [Trouble shooting](#help_)
- [Authors](#authors_)
# <a name="uguide"></a> User's Guide
## <a name="download_ref"></a> Download references
### <a name="genbank_ref"></a> Genbank references
It is possible to download the desired reference sequence directly onto the server through ftp. Navigate to the desired reference.
For example the mouse (mus musculus) genome.
1. click on the “FTP directory to RefSeq assembly:

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/129695747-d108aa49-0d15-4961-b4ad-72915e8dbeb7.png">
</p>

2. Right click on the genomic.fna.gz file and copy the link:

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/129695933-4b1c182f-5969-459d-9f63-c053b34a67a9.png">
</p>

3. On the server navigate to the **Refseq/Standard** folder or **Refseq/Custom** folder:
```
cd /home/ec2-user/Refseq/Standard
```
 
4. Create a new folder for the reference genome: 
```
mkdir mouse_mus_musculus
```
 
5. Then download the reference genome into the newly created folder:
```
wget --recursive --no-host-directories --cut-dirs=6 ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/635/GCF_000001635.26_GRCm38.p6/GCF_000001635.26_GRCm38.p6_genomic.fna.gz -P /home/ec2-user/Refseq/mouse_mus_musculus
```

| Command | Description |
| --- | --- |
| _ftp:_ | download link |
| _-P_ | directory to download into |

To download a different genome make a new directory in the Refseq folder. Then replace the ftp file path with the appropriate link and change the directory to download into.

#### <a name="obtain_names"></a> Obtaining primary chromosome names
The chromosomes in the reference usually use the RefSeq sequence nomenclature. To obtain the names for the primary assembly:
1. Choose the primary assembly under the ‘_assembly unit name_’, and then click on the ‘_Download the full sequence report_’:

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/129696774-4a2838ce-6eb5-4859-9072-455f80fff891.png">
</p>

2. This gives you a txt file containing the records for the assembly. Highlight and copy the ‘assembled-molecule’ records and paste in excel:

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/129696950-f3cf0273-bcac-4116-b3b2-a89f36e1e80b.png">
</p>

4. If the pasted text is not column delimited, use the ‘_Text to columns_’ function in excel. Choose delimited, and the type of delimiter, such as tab and space. 

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/129697110-a256c03c-cc68-41b3-9c4b-6b95868a9b63.png">
</p>

5. The data now appears in separate columns. Copy the names of chromosomes in the primary assembly with the RefSeq nomenclature. When extracting and renaming chromosomes (Prepare reference for pipeline), also copy the simplified chromosome names, e.g. chr1, chr2, etc:

<p align="center">
<img src="https://user-images.githubusercontent.com/60882704/129697208-50503e86-2957-480a-b660-c1cc22f3b96d.png">
</p>

6. Make a chromosome name file:
```
cat > chromosome.names.txt
NC_000067.6
NC_000068.7
NC_000069.6
NC_000070.6
NC_000071.6
NC_000072.6
...
#ctrl-D to exit
```

7. Make a renaming file containing the simplified chromosome names:
```
cat > rename.txt
chr1
chr2
chr3
chr4
chr5
chr6
...
#ctrl-D to exit
```

### <a name="custom_ref"></a> Custom references
Create a new folder in the **Refseq/Standard** or **Refseq/Custom** directory and use WinSCP to upload your custom reference in _fastx_ format.
Once the reference genome has been uploaded it must be prepared for the pipeline. See Prepare reference for pipeline 

## <a name="help_"></a> Trouble shooting
Contact CAJ or QAB
## <a name="authors_"></a> Authors
Camille Johnston (CAJ)

Qammer Abbas (QAB)
