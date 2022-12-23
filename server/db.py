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


def register_car(count_type = 'increment'):
    t = services.get_today()
    cars_ref = db.collection(u'parking').document(u'cars').get()
    cars_count = 0
    full = False

    if t in cars_ref.to_dict():
        cars_count = cars_ref.to_dict()[t]
        print('car_count', cars_count)
        if cars_count >= services.PARKING_SIZE:
            print('Garage is vol')
            full = True

    if count_type == 'increment' and full == False:
        cars_count = cars_count + 1
    elif count_type == 'decrement':
        cars_count = cars_count - 1

    data = {
        u'{}'.format(t): cars_count
    }
    db.collection(u'parking').document('cars').set(data, merge=True)
    return full

def save_car_parked(begin_time, end_time, space):
    delta = end_time - begin_time
    data = {
        u'space_id': space,
        u'start': begin_time,
        u'end': end_time,
        u'total': math.floor(delta.total_seconds())
    }
    db.collection(u'parked').document(u'{}'.format(uuid.uuid4())).set(data, merge=True)



