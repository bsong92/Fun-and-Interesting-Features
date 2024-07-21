import os


def extract_place(filename):
    return filename.split("_")[1]

def make_place_directories(places):
    for place in places:
        os.mkdir(place)
        #print(f"Created directory: {place}")

def organize_photos(directory):
    os.chdir(directory)
    originals = os.listdir()
    places = []
    for filename in originals:
        place = extract_place(filename)
        if place not in places:
            places.append(place)

    make_place_directories(places)

    for filename in originals:
        place = extract_place(filename)
        os.rename(filename, os.path.join(place, filename))

print(os.listdir())  # this is not necessarily needed. Just for sanity check 

#def extract_place(filename):
#    first = filename.find("_")
 #   partial = filename[first+1:]
  #  second = partial.find("_")
   # return(partial[:second])
