import doctest

def FirstStep(pr_k_x0, pr_k_x1):
    """Return Avr for massives 1, 0
    >>> FirstStep([0, 0], [1, 1])
    [0.0, 1.0]
    >>> FirstStep([0.5, 0.5], [0.5, 0.5])
    [0.5, 0.5]
    """
    pr_k = []
    sum0 = 0
    sum1 = 0
    for i in range(len(pr_k_x0)):
        sum0 = sum0 + pr_k_x0[i]
        sum1 = sum1 + pr_k_x1[i]
    pr_k.append(sum0/(sum0+sum1))
    pr_k.append(sum1/(sum0+sum1)) 
    return pr_k

def SecondStep(pr_k_x0, pr_k_x1, NormTrainX, N, pi0, pi1, Size):
    """
    >>> SecondStep([0.6, 0.4], [0.4, 0.6], [[[1, 0], [0, 1]], [[1, 1], [0, 0]]], 2, [[0, 0], [0, 0]], [[0, 0], [0, 0]], 2)
    ([[1.0, 0.4], [0.0, 0.6]], [[1.0, 0.6], [0.0, 0.4]])
    """
    for i in range(Size):
        for j in range(Size):
            sum0 = 0
            sumtemp0 = 0
            sum1 = 0
            sumtemp1 = 0
            for k in range(N):
                sum0 = sum0 + pr_k_x0[k] * NormTrainX[k][i][j]
                sumtemp0 = sumtemp0 + pr_k_x0[k]
                sum1 = sum1 + pr_k_x1[k] * NormTrainX[k][i][j]
                sumtemp1 = sumtemp1 + pr_k_x1[k]
            pi0[i][j] = sum0/sumtemp0
            pi1[i][j] = sum1/sumtemp1
    return pi0, pi1


def ThirdStep(pi0, pi1, N, pr_k, NormTrainX, Size):
    """
    >>> ThirdStep([[0.5, 0.5], [0.5, 0.5]], [[0.5, 0.5], [0.5, 0.5]], 1, [0.6, 0.4], [[[1, 0], [0, 0]]], 2)
    ([0.6], [0.4])
    """
    pr_k_x0 = []
    pr_k_x1 = []
    for m in range(N):
        Multiplication = 1
        for i in range(Size):
            for j in range(Size):
                if (pi0[i][j] == 0 and pi1[i][j] != 1):
                    Multiplication = Multiplication * (((1 - pi1[i][j])/(1 - pi0[i][j]))**(1 - NormTrainX[m][i][j]))
                if (pi0[i][j] == 1 and pi1[i][j] != 0):
                    Multiplication = Multiplication * ((pi1[i][j]/pi0[i][j])**(NormTrainX[m][i][j]))
                if ((pi0[i][j]) != 0 and (pi0[i][j]) != 1):
                    Multiplication = Multiplication * (((1 - pi1[i][j])/(1 - pi0[i][j]))**(1 - NormTrainX[m][i][j])) * ((pi1[i][j]/pi0[i][j])**(NormTrainX[m][i][j]))
        pr_k_x0.append(1/(1 + (Multiplication)*(pr_k[1]/pr_k[0])))
        pr_k_x1.append(1 - (1/(1 + (Multiplication)*(pr_k[1]/pr_k[0]))))
    return pr_k_x0, pr_k_x1


if __name__ == "__main__":
    doctest.testmod()
