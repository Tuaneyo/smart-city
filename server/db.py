import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import uuid
from datetime import datetime
import math
import services

cred = credentials.Certificate('/home/pi/smart-city/smart-city/server/firebaseServiceKey.json')

firebase_admin.initialize_app(cred)

db = firestore.client()

def save_pk_spaces(space, parked):
    data = {
        u'occupied': parked
    }
    db.collection(u'spaces').document(u'{0}'.format(space)).set(data, merge=True)


def get_free_space():
    spaces_ref = db.collection(u'spaces').where(u'occupied', u'==', False).limit(3).stream()
    spaces_text = ''
    for space in spaces_ref:
        space_id = space.id
        # space_data = space.to_dict()
        spaces_text = spaces_text + str(space_id) + ', '

    if spaces_text == '':
        return
    return spaces_text.rstrip(', ')


def register_car():
    t = services.get_today()
    cars_ref = db.collection(u'parking').document(u'{}'.format(t)).get()
    cars_count = 0
    if cars_ref.exists:
        cars_count = cars_ref.to_dict()['count']
        print('car_count', cars_count)
        if cars_count >= services.PARKING_SIZE:
            print('Garage is vol')
            return
    data = {
        u'count': cars_count + 1
    }
    db.collection(u'parking').document(u'{}'.format(t)).set(data, merge=True)
    return True


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



