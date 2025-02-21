def user(f_name, l_name, age, country='nigeria', **user_info):
    "Returns a dictionary of user data"
    user_info['f_name'] = f_name
    user_info['l_name'] = l_name
    user_info['age'] = age
    user_info['country'] = country
    
    return(user_info)    


def greet_bday_user(dob, *users):
    """
    Send out birthday message to user 
    base on their date of birth(dob)
    """
    for user in users:
        if user.get('dob') == dob:       # use get() method to avoid error in case the dob key is missing for a user
            print(f"Hurray! it's {dob}")
            print(f"Happy birthday {user['f_name'].title()} {user['l_name'].title()}. We celebrate you on your day!\n")