# API Documentation

## Authorization
You will not be allowed to access the API unless you provide the following key:  
`ArtOfDataKEY123`

## Requests
**Base URL:** `https://hm-cs.herokuapp.com`  
**Endpoint:** `/socks`

### Parameters

|**Parameter**|**Required**|**Description**|
|:--|:--|:--|
|`key`|Yes|API key|
|`idx`|Yes|Retrieve the row with index `idx` of the dataset

### Error Codes
|**HTTP Code**|**Error Code**|**Description**|
|:--|:--|:--|
|`400`|`1001`|Did not provide `idx`|
|`400`|`1002`|Provided `idx` parameter specifies invalid row of dataset|
|`401`|`1003`|Did not provide API key|
|`401`|`1004`|Provided incorrect API key|
|`404`|`1003`|Reached incorrect endpoint|

