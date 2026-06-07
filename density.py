def density_status(count):

    if count < 30:
        return "Low"

    elif count < 60:
        return "Medium"

    elif count < 100:
        return "High"

    return "Critical"


if __name__ == "__main__":

    people = int(input("Enter Crowd Count: "))
    print(density_status(people))