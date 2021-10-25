def check_password(password): return False if (password.islower() or password.isupper() or len(password) < 8) else True

def main(): print("Good password") if check_password(input("Enter your password: ")) else print("Isnt a good password")

if __name__ == "__main__": main()