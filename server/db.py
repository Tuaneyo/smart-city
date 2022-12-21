import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('/home/pi/smart-city/smart-city/server/firebaseServiceKey.json')

firebase_admin.initialize_app(cred)

db = firestore.client()


def save_pk_spaces(space, parked):
    print('hi')
    data = {
        u'occupied': parked
    }
    db.collection(u'spaces').document(u'{}'.format(space)).set(data, merge=True)


def get_free_space():
    print('here')
    spaces_ref = db.collection(u'spaces').where(u'occupied', u'==', False).limit(3).stream()
    spaces_text = ''
    for space in spaces_ref:
        space_id = space.id
        space_data = space.to_dict()
        spaces_text = spaces_text + str(space_id) + ', '

    return spaces_text.rstrip(', ')

get_free_space()