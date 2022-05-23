from marc import MarkovChain

player_throws = "RRRSRSRRPRPSPPRPSSSPRSPSPRRRPSSPRRPRSRPRPSSSPRPRPSSRPSRPRSSPRP"
sequence = [throw for throw in player_throws]
# ['R', 'R', 'R', 'S', 'R', 'S', 'R', ...]

chain = MarkovChain(sequence)
chain.update("R", "S")

chain["R"]
# {'P': 0.5, 'R': 0.25, 'S': 0.25}

player_last_throw = "R"
player_predicted_next_throw = chain.next(player_last_throw)
# 'P'

counters = {"R": "P", "P": "S", "S": "R"}
counter_throw = counters[player_predicted_next_throw]
# 'S'
