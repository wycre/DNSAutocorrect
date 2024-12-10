# Writing a new DNS provider module

1. Make a copy of the [moduleTemplate](..%2F..%2FmoduleTemplate) folder
2. Move through each file in the folder, reading each comment that contains "MODIFY" in it, following the instructions written in them.
   - Read the[Unified Provider API](..%2FUnified%20Provider%20API.md) document when implementing the UPA functions
3. Open [dns_providers/__init__.py](..%2F..%2Fdns_providers%2F__init__.py) and follow the instructions of the MODIFY comment there.
4. Open [urls.py](..%2F..%2FDNSAutocorrect%2Furls.py) and add the include statement for the new module
