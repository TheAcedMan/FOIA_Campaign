import smtplib
import json
import os
import time
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# LOAD CREDENTIALS-------------------------------------------------------------------------------------
load_dotenv("../../.env")
GMAIL = os.getenv("GMAIL_ADDRESS")
PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
REPLY_TO = os.getenv("REPLY_TO")

# CONFIG------------------------------------------------------------------------------------------------
DRY_RUN = True
DELAY_SECONDS = 10
LOG_FILE = "sent_log.txt"

def load_sent():
    if not os.path.exists(LOG_FILE):
        return set()
    with open(LOG_FILE) as f:
        return set(line.strip() for line in f.readlines())

def log_sent(town_name):
    with open(LOG_FILE, "a") as f:
        f.write(f"{town_name}\n")

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

def send_foia(to_address, town_name):
    msg = send_email(to_address, town_name)
    if DRY_RUN:
        print(f"[DRY RUN] Would send to: {town_name} <{to_address}>")
        return True
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(GMAIL, PASSWORD)
            server.sendmail(GMAIL, to_address, msg.as_string())
            print(f"[SENT] {town_name} <{to_address}>")
            return True
    except Exception as e:
        print(f"[FAILED] {town_name}: {e}")
        return False

def main():
    with open("targets.json") as f:
        targets = json.load(f)

    sent = load_sent()
    skipped_no_email = []
    skipped_already_sent = []
    failed = []
    success = 0

    print(f"Loaded {len(targets)} towns")
    print(f"Already sent: {len(sent)}")
    print(f"DRY RUN: {DRY_RUN}")
    print("="*50)

    for town in targets:
        name = town["name"]
        email = town.get("email", "")

        if not email:
            skipped_no_email.append(name)
            continue

        if name in sent:
            skipped_already_sent.append(name)
            continue

        result = send_foia(email, name)

        if result:
            if not DRY_RUN:
                log_sent(name)
                time.sleep(DELAY_SECONDS)
            success += 1
        else:
            failed.append(name)

    print("\n" + "="*50)
    print(f"Sent/previewed:  {success}")
    print(f"Already sent:    {len(skipped_already_sent)}")
    print(f"No email:        {len(skipped_no_email)} {skipped_no_email}")
    print(f"Failed:          {len(failed)}")

if __name__ == "__main__":
    main()
