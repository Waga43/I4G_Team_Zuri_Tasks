class Student:
    # [assignment] Skeleton class. Add your code here
    ''' Ceate the dunder init method for the Student
    class with additional parameters as stipulated in
    the question
    '''
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)

    def change_name(self, new_name):
        self.name = new_name


    def change_age(self, new_age):
        self.age = int(new_age)


    def add_track(self, add_track):
        self.tracks.append(add_track)


    def get_score(self):
        return float(self.score)


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
