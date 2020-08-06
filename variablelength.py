def func(name, *fav_subjects):
    print("\n", name, "likes to read ")
    for subject in fav_subjects:
        print(subject)

func("Goransh", "Mathematics", "Android Programming")

func("Richa", "C", "Data Structures", "Design and Analysis of algorithms")
