def validStartingCity(distances, fuel, mpg):
    city_with_min_gas = 0
    min_gas = 0
    current_gas = 0
    for index in range(1, len(distances)):
        current_gas += fuel[index - 1] * mpg
        current_gas -= distances[index - 1]
        if current_gas < min_gas:
            city_with_min_gas = index
            min_gas = current_gas
    return city_with_min_gas
        
