
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore


class DjangoFirebaseAdmin:

    def __init__(self, pathtojson):
        self.cred = credentials.Certificate(pathtojson + "creative-hire-firebase-adminsdk-zhrqv-5de1422d8c.json")
        
        # Initialize the app with a service account, granting admin privileges
        firebase_admin.initialize_app(self.cred, {
        'databaseURL': 'https://creative-hire.firebaseio.com'
        })

        # As an admin, the app has access to read and write all data, regradless of Security Rule
        self.db = firestore.client()

        self.doc_ref = self.db.collection(u'keywords').document(u'jobdescripts')


    def select

    # A function to check the health of connection
    def checkStatus(self):
        if self.doc_ref is None:
            return 'Connection error.'
        else:
            return 'All ok - Doc Ref: ' + str(self.doc_ref)

    # A function to insert data 
    def InsertInto(self):
        pass
