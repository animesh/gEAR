#!/opt/bin/python3

"""
Adds a layout via the '+' button in the dataset_manager

Requires:
1) Session id - which contains user_id
2) Layout name to be added
"""

import cgi
import json
import os
import sys
lib_path = os.path.abspath(os.path.join('..', '..', 'lib'))
sys.path.append(lib_path)
import geardb

def main():
    print('Content-Type: application/json\n\n')
    
    form = cgi.FieldStorage()
    session_id = form.getvalue('session_id')
    layout_name = form.getvalue('layout_name')

    user = geardb.get_user_from_session_id(session_id)
    
    if user is None:
        result = {'error':[]}
        error = "Not able to add layout. User must be logged in."
        result['error'] = error
    else:
        layout = geardb.Layout(user_id=user.id, label=layout_name,
                               is_current=0, members=None)
        layout.save()
        result = {'layout_id': layout.id, 'layout_label': layout.label}

    print(json.dumps(result))

if __name__ == '__main__':
    main()
