from firebaseadmin import FirebaseAdmin

t = FirebaseAdmin('')

print(t.check_status())

col = t.collection('jobposts').document('2')

print(t.get_contents(col))


test ={
    "one": "two",
    "three": "four"
}

print(t.write_document(col, test))