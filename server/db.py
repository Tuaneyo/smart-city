import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('./firebaseServiceKey.json')

firebase_admin.initialize_app(cred)

db = firestore.client()


def save_car_enter():
    print('ho')
    data = {
        u'name': u'Los Angeles',
        u'state': u'CA',
        u'country': u'USA'
    }
    db.collection(u'parking').document(u'LA').set(data)