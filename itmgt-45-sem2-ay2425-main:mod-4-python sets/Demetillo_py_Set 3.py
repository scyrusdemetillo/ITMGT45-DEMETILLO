def relationship_status(from_member, to_member, social_graph):
 
    from_member_follows = False
    if from_member in social_graph and "following" in social_graph[from_member]:
        if to_member in social_graph[from_member]["following"]:
            from_member_follows = True
    
    to_member_follows = False
    if to_member in social_graph and "following" in social_graph[to_member]:
        if from_member in social_graph[to_member]["following"]:
            to_member_follows = True
    
    if from_member_follows and to_member_follows:
        return "friends"
    elif from_member_follows:
        return "follower"
    elif to_member_follows:
        return "followed by"
    else:
        return "no relationship"


def tic_tac_toe(board):
   
    n = len(board)
    
    for row in board:
        if len(set(row)) == 1 and row[0] != '':
            return row[0]
    
    for col in range(n):
        column = [board[row][col] for row in range(n)]
        if len(set(column)) == 1 and column[0] != '':
            return column[0]
    
    main_diag = [board[i][i] for i in range(n)]
    if len(set(main_diag)) == 1 and main_diag[0] != '':
        return main_diag[0]
    
    anti_diag = [board[i][n-1-i] for i in range(n)]
    if len(set(anti_diag)) == 1 and anti_diag[0] != '':
        return anti_diag[0]
    
    return "NO WINNER"


def eta(first_stop, second_stop, route_map):

    if first_stop == second_stop:
        time_total = 0
        for leg in route_map:
            time_total += route_map[leg]['travel_time_mins']
        return total_time
    
    current_stop = first_stop
    time_total = 0
    
    next_stops = {}
    for leg in route_map:
        start, end = leg
        next_stops[start] = {
            'next': end, 
            'time': route_map[leg]['travel_time_mins']
        }
        
    while current_stop != second_stop:
        leg_info = next_stops[current_stop]        
        time_total += leg_info['time']       
        current_stop = leg_info['next']
    
    return time_total










