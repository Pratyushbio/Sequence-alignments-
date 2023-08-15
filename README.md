# CBBI
#Run the main.exe file


# For dN/dS

## Significance of dN/dS
The dN/dS ratio is one of the most reliable measures of evolutionary pressures on protein-coding regions, and hence a key indicator of natural selection.

##Usage
Here we compare codon sequences of two organisms and calculate their dN/dS value.
We have included two files viz, Ec_Modified1.txt(to be uploaded first) and Se_Modified1.txt for two organisms. Their output file, output.csv is also included for reference.


# For Modified ti-tv Calculator

This software calculates the modified transition/transversion (ti-tv) values as described in the paper "Berua et al. 2023, Comparison between synonymous transition/transversion with non-synonymous transition/transversion reveals different purifying selection on coding sequences in Escherichia coli".

## Usage

1. **Upload Gene Alignment Files:**
   - From the main menu, click on the "ti-tv" tab and then select "ti-tv calculator".
   - Click the "Browse" button to upload one or more gene alignment files. The uploaded files should be in the multiple sequence alignment format of nucleic acids and have equal-length genes. You can refer to the provided "Sample_gene.txt" file in the folder as an example.

2. **Calculate Modified ti-tv Values:**
   - After uploading the gene alignment files, click on the "Calculate" button.
   - The software will calculate both the conventional ti-tv values and the modified ti-tv values for each individual gene.
   - Conventional ti-tv values are calculated from observed values of synonymous transition (Sti_o) or transversion (Stv_o), non-synonymous transition (Nti_o) or transversion (Ntv_o), and total transition (ti_o) or transversion (tv_o) ratios.
   - Modified ti-tv values (ti' and tv') are calculated using observed values and expected values (Sti_e, Stv_e, Nti_e, Ntv_e) as follows:
     - ti' / tv' = (ti_o / ti_e) / (tv_o / tv_e)
     - Sti' / Stv' = (Sti_o / Sti_e) / (Stv_o / Stv_e)
     - Nti' / Ntv' = (Nti_o / Nti_e) / (Ntv_o / Ntv_e)

3. **Clear Records:**
   - To clear all records and start over, click the "Clear" button.

## Supplementary Files
Three supplementary files will be created in Excel format in the same directory where the program is run:
- `result_data.xlsx`: Contains the calculated ti-tv values for each gene.
- `Supplementary_mutation_data.xlsx`: Supplementary mutation data.
- `Supplementary_observed_expected_values.xlsx`: Supplementary observed and expected values.
- `Supplementary_reference_seq.xlsx`: Supplementary reference sequences for each uploaded gene.

## Example Data
You can find an example gene alignment file named "Sample_gene.txt" in the folder, which you can use to test the calculator.

## Note
Make sure that all uploaded gene alignment files have equal-length genes to ensure accurate calculation of ti-tv values.

For any questions or issues, please refer to the paper or contact ssankar@tezu.ernet.in.