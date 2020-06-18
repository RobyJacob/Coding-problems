import time


def main():
    test_cases = int(input())


    for _ in range(test_cases):
        n = int(input())
        team = list(map(int, input().split()))
        opponent = list(map(int, input().split()))

        team_vs_opponent = []
        for item in zip(team, opponent):
            team_vs_opponent.append(item)

        # max_fights = []
        # for team, opponent in team_vs_opponent:
        #     if team > opponent:
        #         max_fights.append((team, opponent))
        #         team_vs_opponent.remove((team, opponent))

        count = 0
        # for team, opponent in team_vs_opponent:
        #     for team_fight, opponent_fight in max_fights:
        #         if team_fight > opponent and team > opponent_fight:
        #             # team_vs_opponent.remove((team, opponent))
        #             max_fights.append((team, opponent))
        #             count += 1

            # print(max_fights)
            # print(team_vs_opponent)

        for i in range(1, len(team_vs_opponent)):
            for j in range(i):
                if team_vs_opponent[j][0] > team_vs_opponent[i][1] and \
                        team_vs_opponent[j][1] < team_vs_opponent[i][0]:
                    # tmp = team_vs_opponent[i][0]
                    # team_vs_opponent[i][0] = team_vs_opponent[j][0]
                    # team_vs_opponent[j][0] = tmp
                    count += 1
                    break

        print(count)


main()
