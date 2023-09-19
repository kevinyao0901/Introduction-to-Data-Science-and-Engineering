def Move(state, cnt, Move_record, pre_move, Move_State):
    if state == final_state:
        print(Move_record)
        return
    elif state[0] == state[1] and state[3] == state[0]:
        n = [0, 1]
        if(cnt==0):
            n=[0]
        for i in n:
            if i == pre_move:
                continue
            new_state = state.copy()
            new_state[3] = not new_state[3]
            new_state[i] = not new_state[i]
            if new_state not in Move_State:
                Move_State.append(new_state)
                pre_move = i
                cnt += 1
                Move_record.append(str(d[i]) + " and " + str(d[3]) + " Cross to " + str(cnt % 2))
                Move(new_state, cnt, Move_record, pre_move, Move_State)
                Move_State.remove(new_state)
                Move_record.pop()
    elif state[0] == state[2] and state[3] == state[0]:
        n = [0, 2]
        if(cnt==0):
            n=[0]
        for i in n:
            if i == pre_move:
                continue
            new_state = state.copy()
            new_state[3] = not new_state[3]
            new_state[i] = not new_state[i]
            if new_state not in Move_State:
                Move_State.append(new_state)
                pre_move = i
                cnt += 1
                Move_record.append(str(d[i]) + " and " + str(d[3]) + " Cross to " + str(cnt % 2))
                Move(new_state, cnt, Move_record, pre_move, Move_State)
                Move_State.remove(new_state)
                Move_record.pop()
    else:
        cnt += 1
        for i in range(0, 3):
            if state[i] == state[3] and state[3] == False:
                if i == pre_move:
                    continue
                new_state = state.copy()
                new_state[i] = not new_state[i]
                new_state[3] = not new_state[3]
                if new_state not in Move_State:
                    Move_State.append(new_state)
                    pre_move = i
                    Move_record.append(str(d[i]) + " and " + str(d[3]) + " Cross to " + str(cnt % 2))
                    Move(new_state, cnt, Move_record, pre_move, Move_State)
                    Move_State.remove(new_state)
                    Move_record.pop()
        if state == final_state:
            return
        pre_move = -1
        new_state = state.copy()
        new_state[3] = not new_state[3]
        if new_state not in Move_State:
            Move_State.append(new_state)
            Move_record.append(str(d[3]) + " Cross to " + str(cnt % 2))
            Move(new_state, cnt, Move_record, pre_move, Move_State)
            Move_State.remove(new_state)
            Move_record.pop()


d = {0: "Goat", 1: "Wolf", 2: "Vegetable", 3: "Man"}
pre_move = -1
initial_state = [False, False, False, False]  # the left side of river = 0 [Goat, Wolf, Vegetable, Man]
final_state = [True, True, True, True]  # the right side of river = 1 [Goat, Wolf, Vegetable, Man]
Move_record = []
Move_State = []
cnt = 0
Move(initial_state, cnt, Move_record, pre_move, Move_State)
