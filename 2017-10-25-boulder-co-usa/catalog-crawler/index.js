const async = require("async");
const axios = require("axios");

const [catalogURL] = process.argv.slice(2);

if (catalogURL == null) {
  console.warn("Usage: catalog-crawler <catalog URL>");
  process.exit(1);
}

const catalogsChecked = new Set();

const catalogQueue = async.queue(async ({ uri }, callback) => {
  try {
    return callback(null, await processCatalog(uri));
  } catch (err) {
    return callback(err);
  }
});

const featureQueue = async.queue(async ({ uri, inherited }, callback) => {
  try {
    return callback(null, await processFeature(uri, inherited));
  } catch (err) {
    return callback(err);
  }
});

const processCatalog = async (uri, inherited = {}) => {
  if (catalogsChecked.has(uri)) {
    // we've already indexed this catalog
    return;
  }

  catalogsChecked.add(uri);

  const {
    data: {
      contact,
      description,
      endDate,
      features,
      geometry,
      homepage,
      keywords,
      links,
      name,
      provider,
      startDate
    }
  } = await axios.get(uri);

  // allow catalog properties to be overridden
  const properties = {
    ...inherited,
    contact,
    description,
    endDate,
    geometry,
    homepage,
    keywords,
    provider,
    name,
    startDate
  };

  console.log(uri);
  console.log(name);
  console.log(description);

  links.forEach(x =>
    catalogQueue.push({
      uri: x.uri,
      properties
    })
  );

  features.forEach(x => {
    // check if the feature needs to be fetched (if it's not fully present)

    // emit GeoJSON feature(collections) for each feature
    console.log(x.uri);
    console.log(x);

    if (x.uri) {
      featureQueue.push({
        uri: x.uri
      });
    }
  });
};

const processFeature = async uri => {
  const { data } = await axios.get(uri);

  // emit GeoJSON feature(collections) for each feature
  console.log(uri);
  console.log(data);
};

processCatalog(catalogURL);
