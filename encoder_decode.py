def decode(prev_clk, prev_dt, clk, dt) -> int:
    """
        clk vs dt:
        - is two inputs spaced so you know directions 
        - turn it one way -> clk triggers first, then dt 
        - vice versa 
    """

    prev = (prev_clk, prev_dt)
    curr = (clk, dt)

    #(1,1) mean that we "click" the encoder resting postion
    if curr == (1,1): 
        #cw 
        if prev == (1,0): 
            return 1
        #ccw
        elif prev == (0,1):
            return -1
        else:
            return 0
    else:
        return 0 
