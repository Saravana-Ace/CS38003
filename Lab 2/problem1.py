# Write a function called get_total_score(game_scores, team)
# that returns the total score of the given team.
#
# game_scores contains a list of lists where each sublist has the following form [[team1,team2],[score1,score2]]
# team1 plays against team2 with the result score1 for team1 and score2 for team2.
# No team can play against itself and so such an input is invalid.
#
# To get the total score of a given team you need to traverse the list and find all occurrences
# of this team and keep accumulating its scores.
#
# INPUT:
# game_scores: Game scores between teams. type: List of lists containing:
# [[team1,team2],[score1,score2]] where team1, team2: String, score1, score2: Integer
# team: The team for which we must calculate total score, type: String
#
# RETURNS:
# An error value of -1 if the input shows that a team is playing against itself.
# Otherwise: The total score of the given team: type: Integer
#
# SAMPLE INPUT/OUTPUT:
#
# get_total_score( [], 'Alabama' ) should return 0
#get_total_score( [[['Ohio','Arizona'],[22,15]], [['Winconsion','Michigan State'],[12,34]]], 'Georgia' ) should return 0
# get_total_score( [[['Ohio','Ohio'],[22,15]], [['Winconsion','Michigan State'],[12,34]]], 'Georgia' ) should return -1
# get_total_score( [[['Ohio','Arizona'],[22,15]], [['Winconsion','Winconsion'],[12,34]]], 'Georgia' ) should return -1
# get_total_score( [[['Ohio','Arizona'],[29,45]], [['Winconsion','Michigan State'],[38,27]]], 'Ohio' ) should return 29
# get_total_score( [[['Ohio','Florida'],[29,45]], [['Florida','Stanford'],[38,27]]], 'Florida' ) should return 83
# get_total_score( [[['Florida','Stanford'],[13,32]], [['Missouri','Massachusetts'],[28,16]], [['Massachusetts','Stanford'],[48,21]]], 'Massachusetts' ) should return 64
#
# Note: No score can be negative.
#

def main():
    value = get_total_score([], 'Alabama')

    print(value)

def get_total_score(game_scores, team):
    total_score = 0

    for game in game_scores:
        for teams in game:
            if teams[0] == teams[1]:
                return -1
            if(team in teams):
                index = teams.index(team)
                total_score += game[1][index]

    return total_score


if __name__ == '__main__':
    main()
