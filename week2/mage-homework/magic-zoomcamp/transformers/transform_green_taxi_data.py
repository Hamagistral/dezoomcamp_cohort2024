if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import re

def camel_to_snake(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

@transformer
def transform(data, *args, **kwargs):
    # Remove rows where passenger count or trip distance is equal to zero
    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]

    # Create a new column lpep_pickup_date by converting lpep_pickup_datetime to a date
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    # Rename columns in Camel Case to Snake Case
    data.columns = [camel_to_snake(col) for col in data.columns]

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert set(output['vendor_id']).issubset([1, 2]), "Vendor Id not existing value"
    assert (output['passenger_count'] > 0).all(), "Passenger count is under 0"
    assert (output['trip_distance'] > 0).all(), "Trip distance is under 0"