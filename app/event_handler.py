from app.db import db
import time
import threading
from app.db.event import Event
import os.path 
import os
import pickle


def check_events():
    lock = 'event.lock'
    if os.path.isfile(lock):
        # someone else is handling events
        return
    else:
        event_id = 0
        with open(lock,"w") as l:
            l.write("Event id lock") 
        
        event_id = read_event_id()
        event_id = handle_event(event_id)
        write_event_id(event_id)
        os.remove(lock)



def write_event_id(event_id):
    filename = 'event_id'
    outfile = open(filename,'wb')
    pickle.dump(event_id,outfile)
    outfile.close()

def read_event_id():
    filename = 'event_id'    
    try:
        with open(filename, 'rb') as f:
            event_id = pickle.load(f)
    except (OSError, IOError) as e:
        event_id = 0
        with open(filename, 'wb') as f:
            pickle.dump(event_id, f)
    return event_id


def handle_event(event_id):

    
    e = Event.query.filter(Event.event_id > event_id).first()
    while(e != None):
        
        if e.event_type == 'NEW COMMENT':
            comment = e.getComment()
            db.insertComment(comment)

        elif e.event_type == 'UPDATE COMMENT':
            print("updating object ....")
            comment = e.getComment()
            db.updateComment(comment)
            
        elif e.event_type == 'DELETE COMMENT':
            db.deleteComment(e.getComment())
        else:
            print("invalid event type")

        event_id = e.event_id
        e = Event.query.filter(Event.event_id > event_id).first()


    return event_id
