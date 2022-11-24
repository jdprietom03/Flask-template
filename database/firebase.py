import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./database/rutan-2215a-firebase-adminsdk-1blnf-2a77638673.json")
firebase_admin.initialize_app(cred)

db = firestore.client()