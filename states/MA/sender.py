import smtplib
import json
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv("../../.env")

GMAIL = os.getenv("GMAIL_ADDRESS")
PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
REPLY_TO = os.getenv("REPLY_TO")

print(f"Sending from: {GMAIL}")
print(f"Reply-to: {REPLY_TO}")
print(f"Password loaded: {bool(PASSWORD)}")

def send_email(to_address, town_name):
    subject = f"Public Records Request - ALPR and Surveillance Technology - {town_name}"

    body = f"""To the Records Access Officer,
{town_name} Town Hall

Re: Public Records Request — ALPR/License Plate Reader Program

Dear Records Access Officer,

Pursuant to M.G.L. c. 66, § 10, I am requesting the following records related to your agency's use of Automated License Plate Recognition (ALPR) technology:

1. All contracts or agreements with ALPR vendors including Flock Safety, Motorola Solutions (LEARN), and Rekor Systems.

2. Current data retention policies governing ALPR data, including how long plate reads are stored and who may access them.

3. Any data sharing agreements with other law enforcement agencies, federal agencies, fusion centers, or private entities.

4. The total number of ALPR cameras currently deployed and their general locations.

I request a fee waiver on the grounds that this request serves the public interest.

If any portion of this request is denied, please specify the exemption claimed.

Thank you,
FOIA Campaign Research
{REPLY_TO}"""

    msg = MIMEMultipart()
    msg["From"] = GMAIL
    msg["To"] = to_address
    msg["Reply-To"] = REPLY_TO
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    return msg

# Test it - just print the email, don't send yet
test_msg = send_email("test@example.com", "North Reading")
print(test_msg["Subject"])
print(test_msg["Reply-To"])
print("Email built successfully")
