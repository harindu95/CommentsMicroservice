from app.db import db
import time
import threading

event_buffer = []
flag = threading.Condition()


class Thread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.running = True

    def run(self):
        print("thread started running")
        while self.running:
            self.handle_event() 
            with flag:
                print("thread on wait")
                flag.wait(2)
    
    def stop(self):
        self.running = False

    def handle_event(self):
        print("handler started")
        length = 0
        with flag:
            length = len(event_buffer)
        while(length > 0):
            e = None
            with flag:
                e = event_buffer.pop()
            
            if e.type == 'NEW COMMENT':
                db.insertComment(e.comment)
            elif e.type == 'UPDATE COMMENT':
                db.updateComment(e.comment)
            elif e.type == 'DELETE COMMENT':
                db.deleteComment(e.comment)
            else:
                print("invalid event type")

            with flag:
               length = len(event_buffer)
 

def add_event(event):
    with flag:
        print("add event - notify")
        # event_buffer.append(event)
        flag.notify()
        

