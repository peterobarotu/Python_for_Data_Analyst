
def greet(user_name):
    print(f"Nice to me you {user_name.title()}")

if __name__=='__main__':
    import sys
    user_name = sys.argv[1]
    greet(user_name)
    sys.exit()
