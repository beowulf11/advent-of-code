player_num = 419
marbles = 72164 * 100

class Marble:
    def __init__(self, value):
        self.value = value
        self.left = self
        self.right = self

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other.value


def unchain(m):
    '''Remove m from chain'''
    leftMarble = m.left
    rightMarble = m.right
    leftMarble.right = rightMarble
    rightMarble.left = leftMarble

def chain(m1, m2, m3):
    '''Create m1-m2-m3'''
    m1.right = m2
    m2.left = m1

    m3.left = m2
    m2.right = m3

def get_next(marble, next_by, reverse=False):
    next_marble = marble
    for x in range(next_by):
        if not reverse:
            next_marble = next_marble.right
        else:
            next_marble = next_marble.left
    return next_marble

def by_two(m1, m2):
    if get_next(m1, 2) == m2 or get_next(m1, 2, True) == m2:
        return True
    return False

def addMarble(value, currM, player):
    if value % 23 == 0:
         pop = get_next(currM, 7, True)
         players[player] = players.get(player, 0) + value + pop.value
         next_marble = pop.right
         unchain(pop)
         return next_marble
    else:
        m = get_next(currM, 1)
        newMarble = Marble(value)
        chain(m, newMarble, m.right)
        return newMarble


players = dict(zip([x + 1 for x in range(player_num)], [0 for x in range(player_num)]))
chanLen = 1
currentMarble = Marble(0)

player_index = 1
for x in range(1, marbles + 1):
    if x == marbles:
        x *= 100
    currentMarble = addMarble(x, currentMarble, player_index)
    player_index = (player_index + 1) % (player_num + 1)
    if player_index == 0:
        player_index += 1

m = 0
for x in players:
    print(x, players[x])
    if players[x] > m:
        m = players[x]

print(m)
print(max(players, key=lambda x: players[x]))
