def person(**details):
    print(details)

person(name="ram", age="12")

#do same as above adding more attribute

def person(**details):
    print(details['name'])

person(name="ram", age="12", Gender="male", address="lolang", ph_no=98213123, college="achs")