print("=" * 50)
print("AI Course Recommendation System")
print("=" * 50)

name = input("Enter your name: ")

print("\nChoose Your Interest:")
print("1. Artificial Intelligence")
print("2. Data Science")
print("3. Web Development")
print("4. Cyber Security")
print("5. Mobile App Development")

choice = input("\nEnter your choice (1-5): ")

print("\n" + "=" * 50)
print("Hello", name)
print("Recommended Courses For You:")
print("=" * 50)

if choice == "1":
    print("1. Python for AI")
    print("2. Machine Learning Basics")
    print("3. Deep Learning Fundamentals")
    print("4. Natural Language Processing")
    print("5. Computer Vision")

elif choice == "2":
    print("1. Python for Data Science")
    print("2. Statistics for Data Analysis")
    print("3. Data Visualization")
    print("4. Pandas and NumPy")
    print("5. Data Analytics")

elif choice == "3":
    print("1. HTML & CSS")
    print("2. JavaScript")
    print("3. React JS")
    print("4. Node JS")
    print("5. Full Stack Development")

elif choice == "4":
    print("1. Ethical Hacking")
    print("2. Network Security")
    print("3. Penetration Testing")
    print("4. Cyber Threat Analysis")
    print("5. Security Operations")

elif choice == "5":
    print("1. Java Programming")
    print("2. Kotlin Development")
    print("3. Flutter")
    print("4. Android Studio")
    print("5. Mobile UI Design")

else:
    print("Invalid Choice!")

print("\nThank You For Using The Recommendation System!")
