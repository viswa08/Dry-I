
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#fetch the service account key json from local
cred = credentials.Certificate('F:/projects/python/fire connect/trial-f8dca-firebase-adminsdk-bg8pg-0361afbaa0.json')

#initialize the app with a service account
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://trial-f8dca.firebaseio.com/'
    })

#As an admin, the app has access to read and write regardless of security rules
ref = db.reference()
new_user = ref.child('users').push({
    'name' : 'Mary Anning',
    'since' : 1800
    })

new_user.update({'since' : 1800})

# Obtain a new reference to the user, and retrieve child data.
# Result will be made available as a Python dict.
mary = db.reference('users/{0}'.format(new_user.key)).get()
print ('Name:', mary['name'])
print ('Since:', mary['since'])
