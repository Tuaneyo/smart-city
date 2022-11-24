import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('./firebaseServiceKey.json')

firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collections(u'parking')

doc = doc_ref.get()
if doc.exists:
    print(f'Document data: {doc.to_dict()}')
else:
    print(u'No such file found')