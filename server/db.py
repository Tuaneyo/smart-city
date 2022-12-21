import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import uuid
from datetime import datetime
import math

print('db init')
cred = credentials.Certificate('/home/pi/smart-city/smart-city/server/firebaseServiceKey.json')

firebase_admin.initialize_app(cred)

db = firestore.client()

def save_pk_spaces(space, parked):
    data = {
        u'occupied': parked
    }
    print(data)
    db.collection(u'spaces').document(u'{0}'.format(space)).set(data, merge=True)


def get_free_space():
    print('here')
    spaces_ref = db.collection(u'spaces').where(u'occupied', u'==', False).limit(3).stream()
    spaces_text = ''
    for space in spaces_ref:
        print('space ', space)
        space_id = space.id
        space_data = space.to_dict()
        spaces_text = spaces_text + str(space_id) + ', '
    return spaces_text.rstrip(', ')

get_free_space()

def register_car():
    cars_ref = db.collection(u'parking').document(u'cars').get()
    print('hi', cars_ref)
    cars_count = cars_ref.to_dict()['count']
    print(cars_count)
    data = {
        u'count': cars_count + 1
    }
    db.collection(u'parking').document(u'cars').set(data, merge=True)

# def unregister_car():
#     cars_ref = db.collection(u'parking').document('cars').get()
#     cars_count = cars_ref.to_dict()['count']
#     print(cars_count)
#     data = {
#         u'count': cars_count - 1
#     }
#     db.collection(u'parking').document(u'cars').set(data, merge=True)

def save_car_parked(begin_time, end_time):
    delta = end_time - begin_time
    data = {
        u'space_id': 1,
        u'start': begin_time,
        u'end': end_time,
        u'total': math.floor(delta.total_seconds())
    }
    db.collection(u'parked').document(u'{}'.format(uuid.uuid4())).set(data, merge=True)



