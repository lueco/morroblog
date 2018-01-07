---
layout: post
title: python examples of Google maps api
date: '2017-05-10 10:17:21'
tags:
- python
- api
---

Last week, Sheena shouted at me that I just stand to see her suffering from apartment searching. I actually do not have any idea how to find an apartment oversea, more even I haven't gone abroad. It's a really tricky task.
The succeeding days, I will post several articles about how I build a bot to find a suitable apartment nearby specify university.
First thing.
Since I get an address of an apartment, how could I know the time it takes to the campus.
Use apps, such as Google Maps, do work, but it's hard to program. Fortunately, Google Maps provides lots of map-relation APIs.

##Here are some exampls 
`def coord_distance(uname, hla
t, hlon, model):
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=%s&destinations=%f,%f&mode=%s&key=%s" % (uname, hlat, hlon, model, DIST_KEY)
    googlerowdis = requests_get(url).text
    googledist = json.loads(googlerowdis)
    dura = googledist['rows'][0]['elements'][0]['duration']['value']
    duratext = googledist['rows'][0]['elements'][0]['duration']['text']
    dist = googledist['rows'][0]['elements'][0]['distance']['value']
    disttext = googledist['rows'][0]['elements'][0]['distance']['text']
    return dura, duratext, dist, disttext`
`def getGeocode(uname):
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (uname, GEOCODE_KEY)
    rowgeo= requests_get(url).text
    geocode= json.loads(rowgeo)
    zipcode = geocode['results'][0]['address_components'][-1]['short_name']
    lat = geocode['results'][0]['geometry']['location']['lat']
    lng = geocode['results'][0]['geometry']['location']['lng']
    placeId= geocode['results'][0]['place_id']
    placeType = geocode['results'][0]['types'][-1]
    geocode={'zipcode':zipcode, 'lat':lat, 'lng':lng, 'placeId':placeId, 'placeType':placeType}
    return geocode`