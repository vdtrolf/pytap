from utilities.util import *

class Log:

    def __init__(self):
        self.key = get_next_key()
        self.entries = []

    def append_event_to_log(self,event):
        """Appends an event to the event log"""
        self.entries.append(event)

    def get_event_log(self,cntlog):
        """Gets the n-1 event log"""
        # print(f'{self.events_log}')
        if cntlog <= len(self.entries):
            return self.entries[cntlog * -1] + '                                 '
        else:
            return '                           '

