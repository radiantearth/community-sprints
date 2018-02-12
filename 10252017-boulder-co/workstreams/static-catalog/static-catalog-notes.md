#Flat File Catalog


## **GOALS**

Proposed Value

   * Data tha can be quickly ingested to access subsets of the imagery
   * Standardized format for crawlers to create federated indexes
   * Crawler interface standard

   * Define a minimal set of metadata properties to be included in the metadata file(not including properties that can be generated)
       * URI
       * No listing necessary
   * Definition of a set of linked JSON files that specify the network (subresource delegation)
       * What are different levels of metadata possible/necessary
   * Define what this is not
       * The most up to date, there might be some lag
   * Define Extensions to core metadata
       *  Statement around path description 
       * extensions that are readable - z/x/y

Non-core goals

   * Minimal set of guidelines to make this imagery more useful
   * Minimal set of open source tooling to be released with the standard
   * Guidelines for running such a network
       * Size restrictions
   * SEO
       * description
       * tagging/keywords

What we are not

   * Something that sepcifies authentication 

## PRIOR ART


   * Open Data
       * Open Imagery Network
         * JSON sidecar files, main registry pointing to folder of imagery
       * Landsat on AWS <https://landsatonaws.com/L8/154/118/LC08_L1GT_154118_20171023_20171023_01_RT/>
           * lambda code responds to S3 events and generates HTML
       * Mapzen terrain dataset
           *  GeoJSON catalog will be available for the next version
       * Climate NEX
           * hard to use
       * SRTM File Grabber (\url{http://dwtkns.com/srtm/)}
           * UI to browse around the globe and translate to SRTM file names
       * NAIP (state/year/bands/filename\_including\_APFO\_id\_and\_acq\_date)
           * Informative file path that is human readable
           * Key value naming scheme for something at a national level
       * Don't need to have a DB
   * Software systems
       * Entwine for Point cloud (software to index flat files of point cloud)
           * indexing point clouds
       * COGs
           * file level optimization
           * been doing this for years, being smarter about file format
       * GeoTrellis
           * Indexing raster data

## **QUESTIONS TO DISCUSS**

   * Should the flat file catalog include searchability or should it facilitate discoverability + indexing
   * Predictability of filenames (Landsat, SRTM) and extents
   * What's the minimal set of metadata necessarily for making a dataset usable
   * Ideal set of metadata properties
   * Determine granularity recommendations / redirects
       * Dataset-wide vs. delegation 
       * What does the update mechanism look like?
Current unanswered questions:
     - Asset types?


## **NOTES**

   * Where do we store metadata information
       * There are file level metadata properties that you can get from the file itself
       * Or, if that's generated once, you can consume it
           * 5K files for NAIP, had to consume that
   * What's an appropriate level of granularity for flat file catalogs
       * per year per state
       * amount of metadtat that can be tracked that can be recalculated
       * what is a derived product that should already be there
       * Athena on top of S3. Instead of having text, if they were json, dump into s3 bucket, query with Athena
   * Is in our scope to recommend json or other raw material?
       * metadata that is human readable
   * What goes into this?
       * core metadata. JSON
       * thinking about replacements for stuff in 
       * Can run GDAL and upload JSON
       * file level informaiton available via GDAL tools, what about things that are not in the GeoTiff?
   * NAIP data as an example
       * just use JSON
       * then you can keep the structure of it as opposed to a text file
       * Mark experience: when you have sidecar, you have errors.
       * What goes into the metadata of a GeoTiff
   * Sidecar vs derivative sidecar
       * Sidecar: Information from the source not contained in the file
       * Derivitave sidecar: Description of the file
       * Stuff that can fall out of date vs not falling out of date
   * Things the file can't support - collection level metadata
       * reason vendors supply sidecars is because the file can't handle the 
   * Goals - Value proposition
       * goal here - flat file registry, to be ingested by catalog api
       * static storage doing 2 jobs
           * providing underlying storage
           * exposing through crawlers
       * set of rules to allow crawlers to understand on network
       * some federated catalogs you don't need a specific catlaog to participate in the search
       * the data is stages so it can be automatically consumed
       * there will be a proliferation of datatypes and sidecar files
       * important to remember that in order for data to be useable, you have to open source the catalog tooling right next to it
   * GOAL - minimal set of core properties
       * need URI
   * GOAL - set of granularity
       * need metadata for each bucket, or each of the states, each of the years
       * Aggregation mechanisms
       * Intermediate heiracrchical metadata
           * JSON representation of the top level file listing
           * get a list of collections, with a URI to the metadata for a collection
           * smaller units that need to update
           * multi-petabyte dataset
           * different systems
   * Is JSON a part of this, file format?
       * If you want to make counts, make it readable
       * sidecar files turns into a mess
       * NAIP follows some profile - kept separate from the tiffs
       * doesn't follow standard rest
       * seth - yes it is, different resource with a matching link
       * files/whatever.tif
       * meta/whater.json
       * Not sub resources, symbiant resources
       * If you just want the imagery, you don't have to filter downstream
       * easier to eyeball if something is missing w/ sidecar files
   * Question: If you don't have control over your side of the bucket, you don't have ability to sidecar
   * Why aren't we using URIs to point
   * What is the interface for the crawler?
       * Needs one entrypoint
       * nominating the endpoint to crawl
       * OIN register
       * root json doc
       * what's in that? - not everything
       * has to be some way from that root document to discover the network
       * we should do the linking, not point to a directory
       * we are replacing listing
   * *No list access necessary*
   * Federated nodes
       * points to image and sidecar
       * Registry points to nodes, nodes can point to other nodes
   * What about 1.5, 1.6 million files a day
       * having index at root, that works if it's not a lot of data
       * if that bucket gets hit
   * Two fixes for OIN
       * json listing
       * DNS - Not one server that serves it out
       * You can create SOA record for hostname that can say anything under this host as a DNS server
   * NEXRAD - one of the root
       * temporal partitioning of JSON files
   * Do we need a max size for JSON files?
   * Discoverable pattern in naming
   * z/x/y is a type of discoverable pattern
   * push back on z/x/y
   * statement of "this is a predictable dataset, make a guess and see if the data is there"
   * Root metadata
       * Licensing
       * Licensing is implied that it has access to bucket
       * This style of license key or API key
       * mechanics of the associated metadata
       * put in root node part
   * Harris interface says, I have the worlds data. 
       * is a service that crawls through multiple interface, and crawls for what they have access to
       * including online APIs
       * "federations" is set of API calls
   * Authentication
       * However you authenticate against the URI, that's your business
   * Restriction of objects is a key point
   * the more things we can box into "this is actualy metadata associated with leaf nodes"
   * licensing is handled at another level
   * URIs can be a view - authenticated
   * Dynamic rendering vs static rendering
   * HTML?
       * HTML is presentation to human eyes
       * Now it is so much mixed up with presentation issues
       * Doesn't make a great way to serialize data for machine access
       * HTML makes me feel queasy
   * SEO - is there a future we can't see where this data through SEO 
   * What if google cared enough for 
   * SEO - description and tags (keywords)
   * RDF similar thing
   * Image level metadata vs a list of metadata
       * this license applies to everything in this document
       * properties can be progressed through the network
       * other stuff
           * contact info
           * data updated
           * license
   * Sidecar are one to one with asset
   * derived asset vs core asset
   * Sidecare
       * Has URI, follow it. Maybe fall back
       * No URI, same file path with sidecar
**First stab at the JSON specification**

Let there **Nodes** and **Sidecars**

```
{ // http://schema.org/Thing
  name: "foobar",
  description: "imagery for Foobar, Inc.",
  properties: {
    license: "CC-BY-SA 3.0", // SPDX license identifier
    contact: { // http://schema.org/Person
      name: "Pat Exampleperson",
      email: "pat@example.com",
      phone: "555-555-5555",
      url: "https://example.com/people/pate"
    },
  asset_types: [ "geotiff" ], // ??? Optional
  keywords: ["raster", "drone"], // optional
  homepage: "http://wherever"
  assets: [ // leaves; TODO rename
    {
      uri: "https://example.com/foo", 
      properties: { // externally declared properties/metadata for this asset; this is a copy of the sidecar with the addition of uri
            // core metadata properties
            uri: "" // actual data file
      }
    },
    {
     uri: "https://example.com/bar", // metadata sidecar URI (optional)
    }
  ],
 resources: [ // other indexes TODO rename
    {
      name: "",
      uri: "https://host/path/to/list.json"
    }
 ]
}
```

assets - list of objects that describe the assest held by node. 
  - Object pointing to the sidecare
  - AND/OR  the sidecar metadata object itself
  
  resources - list of objects that describe the downstream nodes linked to by this node
  - If there are no resources, this is a leaf node
  
  properties - object of resource and asset properties that apply to everything in this node and also forwardly linked nodes 
  - linked nodes can override parent metadata



*
