import datetime
from random import randint


class BirthdayParadox:
    MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

    def __init__(self, n_people: int):
        self.n_people = n_people
        self.birthdays = self.simulation(n_people)

    def simulation(self, n):
        return [self.gen_bd() for _ in range(n)]

    def gen_bd(self):

        start_of_year = datetime.date(2001, 1, 1)
        rand_no_of_days = datetime.timedelta(randint(0, 364))
        birthday = start_of_year + rand_no_of_days

        return birthday

    def __repr__(self):
        return f"BirthdayParadox(n_people: {self.n_people})"

    def readable(self, bd):
        return '{} {}'.format(self.MONTHS[bd.month - 1], bd.day)

    def show_birthdays(self):
        return [self.readable(bd) for bd in self.birthdays]

    def get_match(self, birthdays=None):

        birthdays = self.birthdays if birthdays is None else birthdays

        if len(birthdays) == len(set(birthdays)):

            return None

        for a, birthday_a in enumerate(birthdays):

            if birthday_a in birthdays[a + 1:]:
                return birthday_a

    def get_desc(self):
        return """
            The Birthday Paradox is a counterintuitive probability puzzle that shows how quickly the likelihood of at least two people sharing the same birthday increases as you add more individuals to a group. With just 23 people, there's approximately a 50% chance of a shared birthday, and with 50 people, it's about 97%. This paradox challenges our intuition about probability and has practical applications in various fields, highlighting the importance of understanding the surprising ways in which probabilities work in large groups.
            """
