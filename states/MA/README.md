# Massachusetts FOIA Campaign

FOIA requests targeting ALPR surveillance and fusion center data sharing 
across all 351 Massachusetts municipalities.

## Files

- `contacts.pdf` — official Mass.gov contact list for all 351 cities and towns
- `parse_contacts.py` — parses contacts.pdf and merges with town websites into targets.json
- `targets.json` — master target list with name, website, and email for each town
- `sender.py` — sends FOIA request emails to targets with dry run mode

## Workflow
```
contacts.pdf → parse_contacts.py → targets.json → sender.py
```

## Usage
```bash
# Parse contacts and build target list
python3 parse_contacts.py

# Dry run - preview without sending
python3 sender.py

# To send for real, change dry_run=False in sender.py
```

## Known Issues

8 towns are missing emails from the Mass.gov PDF and need to be filled 
in manually in targets.json:

- Chesterfield
- Easthampton
- Lynnfield
- Manchester-by-the-Sea
- Mount Washington
- Newburyport
- Wareham
- Westhampton

## Status

- Targets built: 343/351
- Requests sent: 0
- Responses received: 0
