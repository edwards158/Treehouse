import csv
import os

# declare constants
NUMBER_OF_TEAMS = 3
DATES = [
    "5pm 1st Jan 2017.",
    "5pm 3rd Jan 2017.",
    "5pm 5th Jan 2017."
    ]
LETTER_TEXT = (
            "Dear {}, \nYour ward {} is in team {}. The date of first"
            " practice is {} \nRegards \nThe Soccer Coach"
        )


def process_players():
    ''' Generate and return a list of teams and players
    '''
    player_list = []
    with open('soccer_players.csv') as mycsvfile:
        the_data = csv.DictReader(mycsvfile)

        count1 = 0
        count2 = 1
        num_players = 0

        # put the players into alternate slots according to experience
        for row in the_data:
            if row['Soccer Experience'] == 'YES':
                player_list.insert(count1, row)
                count1 += 2
            else:
                player_list.insert(count2, row)
                count2 += 2
            num_players += 1

    players_per_team = int(num_players / NUMBER_OF_TEAMS)

    # create the teams - first 6, middle 6 and last 6 players
    teams = {
        'Sharks':   player_list[0:players_per_team],
        'Dragons':  player_list[players_per_team:2*players_per_team],
        'Raptors':  player_list[2*players_per_team:3*players_per_team]
        }

    return teams


def write_to_guardians(teams):
    ''' Write to the guardians using specified format
    '''
    s = '_'
    count1 = 0
    for team_name in teams:
        for key in teams[team_name]:
            name = (key['Name'].lower()).split()
            file_name = data_path + '/' + s.join(name) + '.txt'
            f = open(file_name, 'w+')
            f.write(LETTER_TEXT.format(key['Guardian Name(s)'], key['Name'],
                    team_name, DATES[count1]))
            f.close()
        count1 += 1
    

def write_teams(teams):
    ''' Write the team information using specified format
    '''
    with open(data_path + '/' + 'teams.txt', 'w+') as f:
        for team_name in teams:
            f.write(team_name + '\n')
            for k in teams[team_name]:
                f.write(k['Name'] + ', ')
                f.write(k['Soccer Experience'] + ', ')
                f.write(k['Guardian Name(s)'] + ' ')
                f.write('\n')
            f.write('\n')

if __name__ == "__main__":

    # create a folder to hold all the files
    data_path = os.getcwd()+'/data'
    
    if not os.path.isdir(data_path):
        os.makedirs(data_path)
    
    teams = process_players()
    write_teams(teams)
    write_to_guardians(teams)
