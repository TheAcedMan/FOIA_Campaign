# FOIA Campaign

A Python-based automation project for filing Freedom of Information Act (FOIA) 
requests to municipalities across the United States, targeting:

- Automated License Plate Recognition (ALPR) surveillance infrastructure
- Fusion center data sharing agreements

Findings are published publicly on this repository and contributed to the 
[Deflock](https://deflock.me) network.

## Why

Local governments are deploying mass surveillance infrastructure — Flock Safety 
cameras, ALPR networks, and fusion center data sharing — with little public 
awareness or oversight. This project uses public records law to document what 
exists, where, and who has access to the data.

## Workflow

1. Build target list — scrape town names, parse contact PDFs, merge into targets.json
2. Send requests — automated email sender with dry run mode
3. Track responses — log replies by town
4. Process findings — extract key data and export to Deflock format
5. Publish — all findings committed to this public repo

## Setup
```bash
git clone https://github.com/TheAcedMan/FOIA_Campaign
cd FOIA_Campaign
python3 -m venv venv
source venv/bin/activate
pip install requests beautifulsoup4 pdfplumber python-dotenv
cp .env.example .env
# Fill in your credentials in .env
```

## Privacy

This project is designed to be operated with reasonable privacy practices:
- Use a VPN when sending requests
- Use a throwaway email address as the sender
- Use ProtonMail or similar as the reply-to address
- Never commit your .env file

## Status

| State | Targets | Sent | Responses |
|-------|---------|------|-----------|
|  MA   |   351   |  0   |     0     |

## Legal

Filing public records requests is constitutionally protected activity. 
This project operates entirely within the bounds of state and federal law.
