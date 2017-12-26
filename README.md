# esther-crawler
Web crawler for Esther that automates registering for courses at Rice.

## Current Features
- Automates logging into Esther, when given credentials (see Usage section below)
- Displays whether the given course is closed or not (or if you've already
registered for that course)

## Usage
You need to create a config.json file. Use the config-example.json as a template,
and rename it to config.json when you've entered the data you want.

Note that currently the script only performs one search, so entering multiple
course numbers isn't allowed. I plan to expand this functionality in the future
(see Todo section below).

Also note that the config.json file stores your ID and password in plaintext,
which is ~~arguably~~ a bad idea. This is another todo item.

### Todo:
- Add tests to ensure that everything is working
- Actually register for the course if it's open
- Multiple queries
- Encrypt the config.json file
- Schedule to run regularly or at a specific time (e.g. run daily if looking for
an opening in a closed course, or run at 7am on add/drop day instead of waking
up early)
- Report waitlist sizes
- Deliver email notifications (when a course opens up or when waitlist is
below/above a certain length)
