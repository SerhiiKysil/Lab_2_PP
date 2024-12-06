class User:

    def __init__(self, name, email, telegram, password, is_verified=False):
        self._password = password
        self.name = name
        self.email = email
        self.telegram = telegram
        self.is_verified = is_verified

    def verify(self):
        self.is_verified = True
        print(f"User {self.name} is now verified.")


    def change_password(self, new_password):
        self._password = new_password
        print(f"Password for user {self.name} has been updated.")



    @staticmethod
    def get_user_type():
        return "Regular User"




class Organization:


    def __init__(self, name, description, contact_email, is_verified=False):
        self.name = name
        self.description = description
        self.contact_email = contact_email
        self.is_verified = is_verified


    def verify(self):
        self.is_verified = True
        print(f"Organization {self.name} is now verified.")


class Event:

    def __init__(self, title, description, start_time, end_time, organization):
        self.title = title
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
        self.organization = organization
        self.participants = []


    def add_participant(self, user):
        if user not in self.participants:
            self.participants.append(user)
            print(f"User {user.name} has been added to the event '{self.title}'.")
        else:
            print(f"User {user.name} is already a participant in the event '{self.title}'.")


    def list_participants(self):
        print(f"Participants in event '{self.title}':")
        for participant in self.participants:
            print(f"- {participant.name}")

    def __str__(self):
        return f"Event: {self.title}, Organization: {self.organization.name}, Start: {self.start_time}, End: {self.end_time}"


class OrganizationUser(User, Organization):
    def __init__(self, user_name, user_email, telegram, password, org_name, org_description, contact_email):
        User.__init__(self, user_name, user_email, telegram, password)
        Organization.__init__(self, org_name, org_description, contact_email)

    def assign_to_organization(self):
        print(f"User {self.name} has been assigned to the organization {self.name}.")


class AdminUser(User):
    def __init__(self, name, email, telegram, password, permissions):
        super().__init__(name, email, telegram, password)
        self.permissions = permissions

    def grant_permission(self, permission):
        self.permissions.append(permission)
        print(f"Permission '{permission}' has been granted to {self.name}.")

    def list_permissions(self):
        print(f"Admin {self.name} has the following permissions: {', '.join(self.permissions)}.")

    @staticmethod
    def get_user_type():
        return "Admin User"


if __name__ == "__main__":
    user1 = User("John Doe", "john@example.com", "@johndoe", "password123")
    user2 = User("Jane Smith", "jane@example.com", "@janesmith", "password456")
    user3 = User("Emily Davis", "emily@example.com", "@emilyd", "emilypass")
    user4 = User("Michael Brown", "michael@example.com", "@michaelb", "mikepass")
    admin1 = AdminUser("Alice Smith", "alice@example.com", "@alicesmith", "adminpass", ["manage_users", "delete_data"])
    admin2 = AdminUser("Charles Wilson", "charles@example.com", "@charlesw", "charlespass", ["create_events", "edit_events"])
    org_user = OrganizationUser("Bob Marley", "bob@example.com", "@bobmarley", "bobpass", "Music Org", "An org for music lovers", "contact@music.org")

    music_org = Organization("Music Org", "An org for music lovers", "contact@music.org")
    tech_org = Organization("Tech Innovators", "Technology and innovation hub", "contact@tech.org")
    music_org.verify()

    event1 = Event("Music Festival", "A grand music event", "2024-12-01 18:00", "2024-12-01 23:00", music_org)
    event2 = Event("Guitar Workshop", "Learn guitar from experts", "2024-12-05 10:00", "2024-12-05 15:00", music_org)
    event3 = Event("Tech Summit", "A conference for tech enthusiasts", "2024-11-30 09:00", "2024-11-30 17:00", tech_org)

    event1.add_participant(user1)
    event1.add_participant(admin1)
    event1.add_participant(org_user)
    event2.add_participant(user2)
    event3.add_participant(user3)
    event3.add_participant(admin2)
    event1.add_participant(user1)

    event1.list_participants()
    event2.list_participants()
    event3.list_participants()

    user1.verify()
    user1.change_password("newpassword123")

    admin1.list_permissions()
    admin1.grant_permission("edit_users")
    admin2.list_permissions()

    org_user.assign_to_organization()

    print(event1)
    print(event2)
    print(event3)

    users = [user1, user2, user3, user4, admin1, admin2, org_user]
    for user in users:
        print(f"User {user.name} is a {user.get_user_type()}.")
