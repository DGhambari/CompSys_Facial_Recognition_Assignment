import presence_detector

def check_presence():
    occupants=[]
    print("Scanning the network for known users...\n")

    occupants = presence_detector.find_devices()

    if "Brian" in occupants:
        print("Brian is home")

    if "Darren" in occupants:
        print("Darren is home")

    return(occupants)