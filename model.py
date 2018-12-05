import json
from datetime import datetime

GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
next_id = 0


##just read entriesf from the disk
def init():
    global entries, next_id
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        f.close()

    except:
        entries = []

    if len(entries) >0:
        for item in entries:
            if int(item['id']) > int(next_id):
                next_id = item['id']
        next_id = str(int(next_id) + 1)

##just returns the list of entries to send to the view
def get_entries():
    global entries
    return entries

##get a timestamp for when the entry was created
##controller gets data that user posted in form and sends it here
##here it gets turned into a dictionary and entered into the top of the json file
def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE, next_id
    now = datetime.now()
    time_string = now.strftime("%b %d, %Y %-I:%M %p")
    # if you have an error using this format, just use
    # time_string = str(now)
    entry = {"author": name, "text": text, "timestamp": time_string, "id": str(next_id)}
    next_id = int(next_id) + 1
    entries.insert(0, entry) ## add to front of list
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")


def delete_entry(id):
    global entries
    count = 0
    remove = -1
    for entry in entries:
        if int(entry["id"]) == int(id):
            remove = count
        count += 1

    del entries[remove]

    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")
