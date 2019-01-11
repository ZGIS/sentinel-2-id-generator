
# Sentinel 2 id generator

## Problem

There is no unique universal identifier (uuid) for Sentinel data, which is valid across all data hubs and is unique for the distinct images. Even within a data hub (e.g. the Copernicus Open Data Hub) the same image might have different uuids.

To have a clean database in the EO-Compass and the data cubes, we need an id generator which generates reliably identical ids for identical images and distinct ids for distinct images. In this way, a UNIQUE constraint in the metadata table is able to prevent duplicate entries. The semantics of what identical images are is not the job of the database.

## Identical images 

When are two images identical?

When they have:

- the same acquisition time
- the same footprint
- ... tbd

## Image sub-sets and partially identical images

It should be reflected that an image is a sub-set or partially identical with another image.

## Image footprints

It should be reflected in the id that two images have the same footprint, but were acquired at different times.

## Image versions

Images might be re-processed by ESA using a different software version. The version should be reflected in the id.


## Example / general pattern

> {instrument}-{platform}-{processinglevel}-{...?}
>
> MSI-A-1C-...?
