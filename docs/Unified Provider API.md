# Unified Provider API (UPA)

This is the design document for the internal Unified Provider API. The purpose is to create a consistent interface that 
the views and background tasks can interact with in lieu of disparate implementations for each supported provider.


## API Data Exchange
This area is a reference to the structure of data utilized by, and returned by UPA methods.

### Service Data
JSON string holding different values depending on intended provider. This string is stored in the `DNSService` database 
table. It includes the redundant data `provider_id` and `auth_token` to make UPA method calls simpler. UPA method
implementation should parse the JSON and utilize the necessary elements.

Example Service Data object:
```json lines
{
	"provider_id": 1,
	"auth_token": "secret", // Redundant, but they simplify method calls
	// Custom Values Here
	"zone_id": "zzebf"
}
```

### Record
When records are passed into and returned by UPA methods, they should follow this standard format.
Data values that do not exist for specific providers can be filled with `None`.
This structure is not final, and new data may be added later, but the ordering of existing elements cannot be changed.

Record structure:
```python
record = (record_name, record_type, record_data, record_id)
```

## API Methods
These are the face of the UPA, all methods must have identical signatures 

### `get_records`
Obtains all records known to the DNS service

Parameters:
- Service Data

Returns:
- List of Records

### `update_record`
Updates records with the DNS Provider

Parameters:
- Service Data
- Original Record
- Updated Record

Returns:
- boolean indicating success or failure

### `upa_sovler`
This method returns a tuple containing references to the other UPA records.

Parameters:
- ID of DNS provider, intended to be provided by the model object

Returns:
- Tuple of the format `(get_records, update_record)`. Method names are references, not calls.

## Interaction
This is an example for interacting with the UPA.

```python
(get_records, update_record) = api_determinator("""Provider ID from DB""")

retrieved_records = get_records(provider_data)
for record in retrieved_records:
    # Check record validity
    if record[2] != source_of_truth:
        """Record fixing logic"""
        success = update_record(provider_data, record, fixed_record)
    
    
```