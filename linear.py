import numpy as np
import matplotlib.pyplot as plt

def estimate(x,y):
    n=np.size(x)
    mean_x,mean_y = np.mean(x) , np.mean(y)
    ss_xy = np.sum(y * x - n * mean_y * mean_x )
    ss_xx = np.sum(x * x - n * mean_x * mean_x )
    b_1 = ss_xy /ss_xx
    b_0 = mean_y - b_1*mean_x
    return (b_0,b_1)

def plot_line(x,y,b):
    plt.scatter(x, y, s=10)
    ypred = b[0] + b[1] * x
    plt.plot(x, ypred, color="g")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def main():
    np.random.seed(0)
    x = np.random.rand(100,1)
    y = x * 5 + np.random.rand(100,1)
    print("{}\n{}".format(x,y))
    b=estimate(x,y)
    print("{}\n{}".format(b[0],b[1]))
    plot_line(x,y,b)

if __name__=="__main__":
    main()