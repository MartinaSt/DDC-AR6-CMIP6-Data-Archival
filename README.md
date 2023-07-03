[![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.xxx.svg)](https://doi.org/10.5281/zenodo.xxx)

# DDC-AR6-CMIP6-Data-Archival

This github repository documents the CMIP6 input dataset archival process at the IPCC DDC Partner DKRZ. This documentation is part of the enhanced transparency implemented as IPCC FAIR Guidelines into the AR6 (Pirani et al., 2022, https://doi.org/10.5281/zenodo.6504468). WGI AR6 TSU provided the CMIP6 input dataset lists provided by the WGI AR6 chapters, which is available at https://drive.google.com/drive/u/0/folders/1oq_MdqGTOId-oMn8_2WzmZrloEYsF-sk. These lists are known to be incomplete. Therefore these TSU lists were merged with the datasets requested by WGI authors at the start of the Sixth Assessment Cycle (https://goo.gl/tVaGko) to obtain the final list of CMIP6 datasets that was added as DDC AR6 Reference Data Archive. The WGI-requested variable list was also used as source for the definition of the CMIP6 data subset disseminated as part of Copernicus CDS (https://cds.climate.copernicus.eu/cdsapp#!/dataset/projections-cmip6).

The CMIP6 input dataset lists provided by the TSU WGI contain abbreviated information on figure usage, which was used to add references/links to to the figure/final datasets or the figure webpage of the IPCC WGI AR6 to the metadata. 

## Processing steps for the CMIP6 input dataset list

**1. Tidy up the received chapter lists turning it into a valid json and harmonizing usage of several missing values:**
   - usage `./tidy.py <input dir>`
   - input directory containing downloaded JSON chapter files: input_20220125
   - output directory containing the tidied JSON chapter files: input_20220125_tidy

**2. Correct obvious DRS errors for CMIP6 datasets lists:**
   - usage `./CMIP6correct.py <input dir>`
   - input directory containing the tidied JSON chapter files: input_20220125_tidy
   - configuration file containing correction rules: CMIP6correct.conf
   - output directory containing corrected JSON chapter files, a list of remaining 23016 CMIP6 datasets (including doublets) and a list of 88 non-correctable datasets: input_20220125_tidy_correct
   - log file: log/CMIP6correct_2022-07-11.log

**3. Merge JSON chapter lists into single list and separate MPI-GE datasets from CMIP6 datasets:**

   The correction was an iterative process. The final version of the corrected and merged CMIP6 input dataset list was created on 2022-07-11. It contains 18909 CMIP6 input datasets.
   - usage `./compileList.py <input dir> <cmip6|cordex|cmip5>`
   - input directory with corrected JSON chapter files: input_20220125_tidy_correct
   - output directory for merged file:  output
   - log file: log/compileList_2022-07-11.log

**4. Check data availability in ESGF:**

The DRS specified in the JSON is used to check data availability. In a second data availability step the DRS is used to get the tracking_id from the NetCDF data headers, which contains the Handle ID of the file:
   - usage Jupyter Notebook `cmip6_lta-tsu_never-in-esgf.ipynb`
   - input file: cmip6_list_2022-07-11.json
   - output file: cmip6_list_data_ref_syntax_wrong-drs-by-pids_2022-08-17.txt, 860 data sets found, which have never been published.

**5. Add and correct versions for CMIP6 datasets without version information:**

For datasets with wrong or missing version information, ESGF and DKRZ data pool are checked for available versions, which are exchanged in or added to the CMIP6 input dataset list:
   - usage Jupyter Notebook `cmip6_lta-tsu_sanitize.ipynb`
   - input file: cmip6_list_data_ref_syntax_wrong-drs-by-pids_2022-08-17.txt
   - output files:  cmip6_list_data_ref_syntax_drs-candidates-by-version_2022-08-17.json providing 808 data sets for replacement in the dataset list and cmip6_list_data_ref_syntax_sortout-notfound_2022-08-17.txt listing 52 data sets, which are unavailable;  

**6. Update of CMIP6 input dataset list and replicate missing data sets into data pool:**

The corrected CMIP6 input dataset list cmip6_list_2022-07-11.json is updated with the results from 4. and 5. If more than one version for a dataset without specified version exist, all versions are included. Information on dublicates are merged:
   - usage Jupyter Notebook `cmip6_lta-tsu_finalize.ipynb`
   - input files: cmip6_list_2022-07-11.json and cmip6_list_data_ref_syntax_drs-candidates-by-version_2022-08-17.json
   - output files:  cmip6_list_2022-08-17.json; 855 datasets were identified, after merging dublicates 680 datasets were updated/added to the CMIP6 input dataset list (all are available)

The result contains 18956 corrected and available CMIP6 input datasets. 52 dataset duplicates caused by version changes require special treatment. 

An overview oover the changes applied in steps 4. and 5. to the input dataset list cmip6_list_2022-07-11.json to create the resulting cmip6_list_2022-08-17.json is provided in: `DDC_cmip6_overview.csv`. The CMIP6 input dataset list in column 'DDC_AR6_Archive' is used for merging with the WGI-requested variable list resulting in a total number of 65,118 archived CMIP6 datasets.

**7. Add data usage information to the metadata:**

The CMIP6 input data set lists provided by the TSU WGI contain abbreviated information on figure usage of the the data sets. This information was used to add references/links to the figure/final data sets in the CEDA catalogue (https://catalogue.ceda.ac.uk/) and to the figure pages of the IPCC WGI AR6 (https://www.ipcc.ch/report/ar6/wg1/figures).

## Repository Structure

   - [Metadata_Conformance](/Metadata_Conformance): containing scripts for steps 1 to 3
   - [Data_Verification](/Data_Verification): containing scripts for steps 4 to 6

## Variable usage analysis: Metadata_Conformance/varlist4dreq.py

For CMIP7 planning, the CMIP6 variable usage by IPCC WGI authors was analyzed based on the corrected CMIP6 input dataset list. The results were shared through the google drive folder: https://drive.google.com/drive/u/0/folders/14YSgIype4fFtnXb4DNMmgXxYQiLLC0wy

## Installation

The Preparation package requires python2.7. The Validation package was done using Python 3.7 including Python packages: json, pandas, tqdm, uuid, intake, pyhandle.handleclient (PyHandleClient).

## License

The software is released under the [MIT License](LICENSE).
