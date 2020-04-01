from app.db import db
import time
import threading
from app.db.event import Event
import os.path 
import os
import pickle
from app.logging import log



def check_events():
    lock = 'event.lock'
    if os.path.isfile(lock):
        # someone else is handling events
        log.info("event.lock exists!")
        return
    else:
        
        event_id = 0
        log.info("Open event.lock ")
        with open(lock,"w") as l:
            l.write("Event id lock") 
    
        event_id = read_event_id()
        event_id = handle_event(event_id)
        write_event_id(event_id)

        os.remove(lock)
        log.info("Close event.lock ")



def write_event_id(event_id , filename='event_id'):
    log.info("Write event_id to file ")
    outfile = open(filename,'wb')
    pickle.dump(event_id,outfile)
    outfile.close()

def read_event_id( filename='event_id'):
    log.info("Read event_id from file ")  
    try:
        with open(filename, 'rb') as f:
            event_id = pickle.load(f)
    except (OSError, IOError) as e:
        event_id = 0
        with open(filename, 'wb') as f:
            pickle.dump(event_id, f)
    return event_id


def handle_event(event_id):

    log.info("Handling events - event_id %s", event_id) 
    e = Event.query.filter(Event.event_id > event_id).first()
    while(e != None):
        
        if e.event_type == 'NEW COMMENT':
            comment = e.getComment()
            log.info("Insert Comment Event") 
            db.insertComment(comment)

        elif e.event_type == 'UPDATE COMMENT':
            log.info("Update Comment Event") 
            comment = e.getComment()
            db.updateComment(comment)
            
        elif e.event_type == 'DELETE COMMENT':
            log.info("Delete Comment Event") 
            db.deleteComment(e.getComment())
        else:
            log.error("Invalid event type %s", e.event_type) 

        event_id = e.event_id
        e = Event.query.filter(Event.event_id > event_id).first()


    return event_id
