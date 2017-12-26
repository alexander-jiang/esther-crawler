# esther-crawler
Web crawler for Esther that automates registering for courses at Rice.

## Current Features
- Automates logging into Esther, when given credentials (see Usage section below)

## Usage
You need to create a config.json file. Use the config-example.json as a template, and rename it to config.json when 
you've entered the data you want.

Note that currently the script only performs one search, so entering multiple course numbers isn't allowed (however,
specifying multiple subject codes with the same course number is allowed e.g. crosslisted courses like PSYC 362 and NEUR 362).
I plan to expand this functionality in the future (see Todo section below).

Also note that the config.json file stores your ID and password in plaintext, which is arguably a bad idea. This is another todo item.

### Todo:
- Actually registering for the course if it's open
- Multiple queries
- Encrypting the config.json file
- Schedule to run regularly or at a specific time (e.g. daily if looking for opening, or at 7am on add/drop day)
- Able to register for courses and check waitlist sizes
- Email notifications
