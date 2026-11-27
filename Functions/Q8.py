def make_profile(**info):
    for key, value in info.items():
        print(key, ":", value)

    return len(info)


count = make_profile(name="Sara", city="Multan", course="Python")
print("Total details:", count)