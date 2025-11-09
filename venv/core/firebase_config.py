import os
import json
import firebase_admin 
from firebase_admin import credentials, firestore

def init_firebase():
  firebase_key_str = os.getenv("FIREBASE_KEY")
  
  if not firebase_key_str:
    raise ValueError("❌ FIREBASE_KEY no encontrada en variables de entorno.")
  
  firebase_key = json.loads(firebase_key_str)
  cred = credentials.Certificate(firebase_key)
  
  if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)
    
  return firestore.client()