
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore

from google.cloud import firestore_v1


class FirebaseAdmin:

    def __init__(self, pathtojson):
        self.cred = credentials.Certificate(pathtojson + "creative-hire-firebase-adminsdk-zhrqv-5de1422d8c.json")
        
        # Initialize the app with a service account, granting admin privileges
        firebase_admin.initialize_app(self.cred, {
        'databaseURL': 'https://creative-hire.firebaseio.com'
        })

        # As an admin, the app has access to read and write all data, regradless of Security Rule
        self.db = firestore.client()

        self.doc_ref = self.db.collection(u'keywords').document(u'jobdescripts')


    # A function to check the health of connection
    def check_status(self):
        if self.db is None:
            return 'Connection error.'
        else:
            return 'All ok - Doc Ref: ' + str(self.doc_ref)

    # A function to insert data 
    def insert_into(self):
        pass

    # Get the collection specified
    def collection(self, collection_name):
        return self.db.collection(collection_name)

    # Get the document specified
    def document(self, document_name):
        return self.db.document(document_name)

    # Return all contents inside specified Collection
    def collection_contents(self, collection):
        docs = collection.stream()
        output = ""

        for doc in docs:
            output += '{} => {}'.format(doc.id, doc.to_dict())
        return output

    # return all the contents inside Document    
    def document_contents(self, document):
        try:
            doc = document.get()
            return  'Document data: {}'.format(doc.to_dict())
        except google.cloud.exceptions.NotFound:
            return 'No such document!'

    # Get contents no matter what the object is
    def get_contents(self, object):
        if isinstance(object, firestore_v1.document.DocumentReference):
            return self.document_contents(object)
        elif isinstance(object, firestore_v1.collection.CollectionReference):
            return self.collection_contents(object)