def swap_sum(A, B):
    A_i, B_i = 0, len(B) - 1
    
    while A_i < len(A) and B_i >= 0:
        A[A_i], B[B_i] = B[B_i], A[A_i]
        diff = sum(B) - sum(A)
        A[A_i], B[B_i] = B[B_i], A[A_i]

        if diff == 10:
            return (A_i, B_i)
                
        elif diff < 10:
            if (B_i >= 1):
                B_i-= 1
            else:
                A_i += 1
        else:
            if (A_i >= 1):
                B_i += 1
    return None
