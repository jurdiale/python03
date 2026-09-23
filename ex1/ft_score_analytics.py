import sys

if __name__ == '__main__':
    score = []
    print("=== Player Score Analytics ===")
    for i in range(1, len(sys.argv)):
        try:
            score.append(int(sys.argv[i]))
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")
    if not score:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py "
            "<score1> <score2> ...")
    else:
        print(f"Scores processed: {score}")
        print(f"Total players: {len(score)}")
        print(f"Total score: {sum(score)}")
        print(f"Average score: {float(sum(score) / len(score))}")
        print(f"High score: {max(score)}")
        print(f"Low score: {min(score)}")
        print(f"Score range: {max(score) - min(score)}")
