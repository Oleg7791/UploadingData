def data_earthquake(d):
    """функция создает списки с данными о землетрясении"""
    mags, lons, lats, hover_texts = [], [], [], []
    mag = d['properties']['mag']
    lon = d['geometry']['coordinates'][0]
    lat = d['geometry']['coordinates'][1]
    title = d['properties']['title']

    return mag, lon, lat, title
