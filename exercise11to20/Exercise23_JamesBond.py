movies = {"Sean Connery": F"rom Russia With Love;", "Roger Moore": "Live and Let Die", "Pierce Brosnan": "Die Another Day;", "Daniel Graig": "Skyfall"}

print(movies)

score = 0
count = 1
while count <= 4:

    answer = input("Attempt %d name and actor " %(count))
    if answer in movies:
        score += 1
        print("Well done %s is bond in %s" %(answer, movies[answer]))
    else:
        print("incorrect answer")
    count += 1
print("You got %d out of 4" %(score))