#### clean_line_breaks.py
#### November 8, 2019
#### PP275 -- Lab 7
#### Contact email: jsayre@berkeley.edu


def clean_line_breaks(df):
    '''clean_line_breaks cleans up noncontiguous polylines in ZAF railroads
    Inputs: geopandas dataframe of ZAF railroad shapefile
    Outputs: cleaned railroad gpd dataframe, with the endpoints rounded to ~10m accuracy'''
    from shapely.geometry import LineString
    import numpy as np
    for i in range(len(df)):
        try:
            line_lats, line_lons = df['geometry'][i].xy
            line_lats[0] = np.round(line_lats[0],4)
            line_lats[-1] = np.round(line_lats[-1],4)
            line_lons[0] = np.round(line_lons[0],4)
            line_lons[-1] = np.round(line_lons[-1],4)
            df.loc[i,'geometry'] = LineString(list(zip(line_lats,line_lons)))
        except:
            if i == 481: ### for whatever reason this one has a different structure
                line_lats, line_lons = df['geometry'][i].geoms[0].xy
                line_lats[0] = np.round(line_lats[0],4)
                line_lats[-1] = np.round(line_lats[-1],4)
                line_lons[0] = np.round(line_lons[0],4)
                line_lons[-1] = np.round(line_lons[-1],4)
                df.loc[i,'geometry'] = LineString(list(zip(line_lats,line_lons)))
            else:
                full_lats, full_lons = [], []
                for geom in df['geometry'][i].geoms:
                    line_lats, line_lons = geom.xy
                    full_lats.extend(line_lats)
                    full_lons.extend(line_lons)
                full_lats[0] = np.round(full_lats[0],4)
                full_lats[-1] = np.round(full_lats[-1],4)
                full_lons[0] = np.round(full_lons[0],4)
                full_lons[-1] = np.round(full_lons[-1],4)
                df.loc[i,'geometry'] = LineString(list(zip(full_lats,full_lons)))
    return df

