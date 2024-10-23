# Models

## DNSService
DNS services represent one account with an API.
### User Provided Fields
- Name
  - CharField
- Provider
  - CharField w/ Choices
    - Choices from `dns_providers.ProviderChoices`
  - Forms render a dropdown
- Auth
  - TextField
  - Holds the API key
- [Service Data](Unified%20Provider%20API.md)

## MonitoredRecord
- Name
  - CharField
- Type
  - CharField w/ Choices
    - Choices are DNS record Types
- Source Of Truth
  - CharField
  - Optional
- Dynamic SOT
  - BooleanField
  - Form renders Checkbox
- Interval
  - CharField
  - Holds `cron` expression interpreted by `background.py`
- History
  - TextField
  - Holds recent valid record data
  - Not exposed to user (except in logs)
- Service
  - ForeignKey (DNSService)