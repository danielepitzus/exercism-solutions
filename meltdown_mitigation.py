# criticality 
# if rector_state < criticality = it can become damaged
# if reactor_state > criicality = it can overload and result in a meltdown

# Check for criticality:
    # check if the reactor is balanced in criticality: 
        # temperature < 800 K
        # neutrons_emitted > 500
        # temperature * neutrons_emitted < 500000

# Determine the power output range
    # 1. green -> efficiency >= 0.80
    # 2. orange -> 0.60 <= efficiency < 0.80
    # 3. red -> 0.30 <= efficiency < 0.60
    # 4. black -> efficiency < 0.30

# Fails safe Mechanism
    # temperature * neutron_produced_per_second < 0.90 of threshold= LOW
    # temperature * neutron_produced_per_second +/- 0.10 of threshold = NORMAL
    # temperature * neutron_produced_per_second is not in the above-stated ranges = DANGER 

"""Functions to prevent a nuclear meltdown."""

def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be balanced in criticality if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    return temperature < 800 and neutrons_emitted > 500 and (temperature * neutrons_emitted) < 500000

def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    generated_power = voltage * current
    efficiency = (generated_power/theoretical_max_power) * 100

    if efficiency >= 80:
        return "green"
    elif efficiency >= 60:
        return "orange"
    elif efficiency >= 30:
        return "red"
    else:
        return "black"
    
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """
    efficiency = temperature * neutrons_produced_per_second
    lower_bound = 0.90 * threshold
    upper_bound = 1.1 * threshold

    if efficiency < lower_bound:
        return "LOW"
    elif lower_bound <= efficiency <= upper_bound:
        return "NORMAL"
    else:
        return "DANGER"







print(is_criticality_balanced(800, 500.01))
