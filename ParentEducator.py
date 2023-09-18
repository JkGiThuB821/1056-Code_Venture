'''
The definition for the ParentEducator class is below.
'''
# Import statements
from user import User
from learner import Learner

# ParentEducator class definition
class ParentEducator():
    """
    - parentEducatorName: string
    - student: Learner
    - learnerProgress: ProgressTracker

    """

    def __init__(self, User, Learner, learner_progress):
        """
        Constructor of ParentEducator self
        """
        self.User = User
        self.parentEducatorName = User.getUsername()
        self.Learner = Learner
        self.learnerProgress = learner_progress

    def get_learner_progress(self):
        return self.learner_progress
    def get_learner(self):
        return self.learner

    def give_feedback(self):
        feedback_input = input("Please give your feedback about CodeVenture: ")
        print("Thank you very much for your feedback.")
        return feedback_input


    


if __name__ == "__main__":
    # Test cases
    # Create a User object
    pass
