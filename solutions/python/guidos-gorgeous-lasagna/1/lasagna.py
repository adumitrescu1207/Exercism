"""Constants for lasagna"""
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 0

def bake_time_remaining(elapsed_bake_time):
    """Returns the bake_time_remaining"""
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Returns the preparation_time_in_minutes"""
    return number_of_layers * 2
    
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Returns the elapsed_time_in_minutes"""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
