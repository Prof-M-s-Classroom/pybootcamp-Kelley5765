class CrewMember:
    """
    Represents a crew member with a name, role, and experience.
    """

    def __init__(self, name, role, experience):
        """
        Initializes CrewMember

        Arguments:
            name (str): Name of crew member.
            role (str): Role of crew member.
            experience (int): Years of experience.
        """
        self.name = name
        self.role = role
        self.experience = experience  # Years of experience


    def __str__(self):
        """
        Returns a string representation of CrewMember

        Returns:
            str: String representation of CrewMember with name, role, and experience.
        """
        return f"{self.name} - {self.role} ({self.experience} yrs exp)"


class CrewRoster:
    """
    Manages roster of crew members.
    """

    def __init__(self):
        """
        Initializes CrewRoster with an empty list
        """
        self.crew = []  # List of CrewMember objects


    def add_member(self, name, role, experience):
        """
        Adds a new crew member to the roster.

        Arguments:
            name (str): Name of crew member.
            role (str): Role of crew member.
            experience (int): Years of experience.
        """
        new_member = CrewMember(name, role, experience)
        self.crew.append(new_member)

    def remove_member(self, name):
        """
        Removes a crew member by name.

        Arguments:
            name (str): Name of crew member.
        """
        self.crew = [member for member in self.crew if member.name != name]

    def list_crew(self):
        """Prints all crew members."""
        for member in self.crew:
            print(member)

# === TEST CODE ===

roster=CrewRoster() #Empty Crew roster created

    # TODO: Uncomment and implement methods
roster.add_member("Alice", "Engineer", 5)
roster.add_member("Bob", "Pilot", 10)
roster.list_crew()

roster.remove_member("Alice")
roster.list_crew()