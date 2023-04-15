freezing_temp = 0
boilingTemp = 100


def water_state(temperature):
    state = 'Liquid'
    if temperature <= freezing_temp:
        state = 'Solid'
    elif temperature >= boilingTemp:
        state = "Gas"
    return state
