
![](https://travis-ci.org/ZGIS/sentinel-2-id-generator.svg?branch=master) [![codecov](https://codecov.io/gh/ZGIS/sentinel-2-id-generator/branch/master/graph/badge.svg)](https://codecov.io/gh/ZGIS/sentinel-2-id-generator)

# Sentinel 2 id generator

## 1. Problem

There is no unique universal identifier (uuid) for Sentinel data, which is valid across all data hubs and is unique for the distinct images. Even within a data hub (e.g. the Copernicus Open Data Hub) the same image might have different uuids.

To have a clean database in the EO-Compass and the data cubes, we need an id generator which generates reliably identical ids for identical images and distinct ids for distinct images. In this way, a UNIQUE constraint in the metadata table is able to prevent duplicate entries. The semantics of what identical images are is not the job of the database.

## 2. Sentinel-2 metadata structure (relevant elements)

For the first version the granule id (according to the UTM grid) and the acquistion time will be used. The formatting is as follows according to the naming convention (https://sentinel.esa.int/web/sentinel/user-guides/sentinel-2-msi/naming-convention):


```python
#
# Tile/Granule id / Footprint / UTM grid id
#
# General pattern: Txxxxx
#
# Example:
#
granule_id = 'T33UVP'

#
# Acquisition time
#
# General pattern: YYYYMMDDHHMMSS
#
# Example:
#
acquisition_time = '20170105T013442'
```

## 3. Initial considerations

There will be a (simplified) version 1 of the Sentinel-2 id generator, which is scene-based. I.e., it takes a scene name according to the UTM grid and the acquisition time. The version 2 of the Sentinel-2 id generator will work on arbitrary geographic regions.

### 3.1 Identical images 

When are two images identical?

When they have:

- the same acquisition time
- the same footprint
- ... tbd

### 3.2 Image sub-sets and partially identical images

It should be reflected that an image is a sub-set or partially identical with another image.

### 3.3 Image footprints

It should be reflected in the id that two images have the same footprint, but were acquired at different times.

### 3.4 Acquisition time

It is reasonable to expect that there is a time tolerance of a few miniutes required. For example the temporal granularity might be 5 minutes (neglecting day/night changes for simplicity).

### 3.5 Image versions

Images might be re-processed by ESA using a different software version. The version should be reflected in the id.


## 4. Example / general pattern

Version 1:

> {granule-id}-{acquisitionyear}-{acquisitiondayofyear}-{acquisitionhour}-{acquisitiontime (minutes / 5)}
>
> t33uvp-2017-005-01-6

Version 2 might be something like this:
> {instrument}-{platform}-{processinglevel}-{...?}
>
> MSI-A-1C-...?

## 5. Usage

Use the package as follows


```python
#
# Import the package
#
from s2_idgen import s2_idgen

#
# Generate a new id
#
id = s2_idgen.Generator(granule_id = 'T33UVP', acquisition_time = '20170105T013442')

#
# Access the id
#
id.getID()
```




    't33uvp-2017-005-01-6'


