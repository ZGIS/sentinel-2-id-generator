# sentinel-2-id-generator

## Problem

There is no unique universal identifier (uuid) for Sentinel data, which is valid across all data hubs and unique for the individual images. Even within a data hub (e.g. the Copernicus Open Data Hube) the same image might have different uuids.

To have a clean database in the EO-Compass and the data cubes, we need an id generator which generates reliably identical ids for identical images and distinct ids for distinct images.

## Identical images 

When are two images identical?

When they have:

- the same acquisition time
- the same footprint
- ... tbd

## Image versions

Images might be re-processed by ESA using a different software version. The version should be reflected in the id.
