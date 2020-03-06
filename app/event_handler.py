from app.db import db
import time
import threading

event_buffer = []
flag = threading.Condition()


class Thread(threading.Thread):

    def __init__(self, app):
        threading.Thread.__init__(self)
        self.running = True
        self.app = app

    def run(self):
        print("thread started running")
        while self.running:
            self.handle_event() 
            with flag:
                print("thread on wait")
                flag.wait()
    
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
                with self.app.app_context():
                    db.insertComment(e.comment)
            elif e.type == 'UPDATE COMMENT':
                with self.app.app_context():
                    db.updateComment(e.comment)
            elif e.type == 'DELETE COMMENT':
                with self.app.app_context():
                    db.deleteComment(e.comment)
            else:
                print("invalid event type")

            with flag:
               length = len(event_buffer)
 

def add_event(event):
    with flag:
        print("add event - notify")
        event_buffer.append(event)
        flag.notify()
        

