# Regional Data

The provision of selected CMIP6 input datasets for regions utilizes the [Climate Data Operators (cdo) package](https://code.mpimet.mpg.de/projects/cdo) and has three step process:

   1. jblob*.sh: Download of selected datasets
   2. cutRegions.py: cutting regions out of global datasets

    cdo -s sellonlatbox,lon1,lon2,lat1,lat2
    
   - Africa: ``cdo -s sellonlatbox,-35,72,-58,40``
   - South_Pole: ``cdo -s sellonlatbox,0,360,-90,-57``
   - Central_Pacific: ``cdo -s sellonlatbox,120,290,-20,20``
   - Asia: ``cdo -s sellonlatbox,26,-168,3,83``
   - Australia: ``cdo -s sellonlatbox,68,-115,-58,8``
   - Europe: ``cdo -s sellonlatbox,-60,60,30,75``
   - North America: ``cdo -s sellonlatbox,-170,-45,5,85``
   - North_Pole: ``cdo -s sellonlatbox,0,360,60,90``
   - South_America: ``cdo -s sellonlatbox,-120,-30,-58,15``

   3. mergeFiles.py: merge NetCDF files into single time series

    cdo -s mergetime

The applied cdo commands are documented in the history attribute of each NetCDF file header. The data subset is documented in [IPCC_AR6_RegionData.pdf](/IPCC_AR6_RegionData.pdf).
