import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("C:\\Users\\Asus\OneDrive\Desktop\\Pulkit_AIML\\Machine learning Train\\Facial Recognition\\face-recog-attendance-6c441-firebase-adminsdk-q505x-43239c714b.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://face-recog-attendance-6c441-default-rtdb.firebaseio.com/"
})
ref = db.reference('Students')
data = {
    "321654":
        {
            "Name":"123456",
            "class":"4",
            "Major":"AI/ML",
            "Attendnace":"4",
            "Current":"2023-18-05 00:54:00"  
        },
    "452996":
        {
            "Name":"Pulkit",
            "class":"1",
            "Major":"AIML",
            "Attendnace":"10",
            "Current":"2023-18-05 00:54:00"  
        },
    "452997":
        {
            "Name":"Elon Musk",
            "class":"1",
            "Major":"AIML",
            "Attendnace":"5",
            "Current":"2023-18-05 00:54:00"  
        },
    "452998":
        {
            "Name":"amithabh",
            "class":"1",
            "Major":"Acting",
            "Attendnace":"9",
            "Current":"2023-18-05 00:54:00"  
        },
    "452999":
        {
            "Name":"Prashansa",
            "class":"1",
            "Major":"Padhi Likhi Gawar",
            "Attendnace":"4",
            "Current":"2023-18-05 00:54:00"  
        },
    "852741":
        {
            "Name":"cdes",
            "class":"4",
            "Major":"Pata nai",
            "Attendnace":"4",
            "Current":"2023-18-05 00:54:00"  
        }
}
for key,value in data.items():
    ref.child(key).set(value)