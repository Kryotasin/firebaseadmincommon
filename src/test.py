from firebaseadmin import FirebaseAdmin

t = FirebaseAdmin('')

print(t.check_status())

print(t.get_contents(t.collection('jobposts')))