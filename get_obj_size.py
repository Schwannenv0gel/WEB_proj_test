def get_size_params(json_response):
    org_borders = json_response["features"][0]["properties"]["boundedBy"]
    adress_ll = list(map(str, json_response["features"][0]["geometry"]["coordinates"]))
    size = list(map(str, [abs(org_borders[1][0] - org_borders[0][0]), abs(org_borders[1][1] - org_borders[0][1])]))
    return [adress_ll, size]
