import numpy as np
import matplotlib.pyplot as plt


def integrator(d, N, r1, r2, a):

    lenght = max(r1, r2)
    z = max(r1, r2+a)
    box_dim = np.append(np.ones(d-1)*lenght, z)

    points = np.random.uniform(-box_dim, box_dim, (N, d))

    dist1 = np.linalg.norm(points, axis=1)
    dist2 = np.linalg.norm(points+np.append(np.zeros(d-1), a), axis=1)


    inside = np.dot(np.where(dist1<=r1, 1, 0), np.where(dist2<=r2, 1, 0))


    dev = np.sqrt((inside-inside**2/N)/(N-1))

    
    volume = np.prod(2*box_dim)*inside/N
    stdev = dev/np.sqrt(N)*volume

    return volume, stdev


if __name__ == "__main__":

    n_array = np.logspace(6, 24, num=19, base=2.0, dtype=int)

    
    d10, u10, d5, u5, d3, u3 = [],[],[],[],[],[]


    for i in n_array:
        
        d, u = integrator(10, i, 5, 3, 2)
        d10.append(d)
        u10.append(u)

        d, u = integrator(5, i, 5, 3, 2)
        d5.append(d)
        u5.append(u)

        d, u = integrator(3, i, 5, 3, 2)
        d3.append(d)
        u3.append(u)





    fig, ax = plt.subplots(2, 3, figsize=[16,9])

    
    ax[0,0].errorbar(np.sqrt(n_array), d10, yerr=u10, fmt='o-')
    ax[0,0].set_title("10-D Vol (r1=5, r2=3,a=2)")
    ax[1,0].scatter(np.sqrt(n_array), u10)
    ax[1,0].set_title("10-D Uncert")
    ax[1,0].set_xlabel("Sqrt(N)")
    ax[0,1].errorbar(np.sqrt(n_array), d5, yerr=u5, fmt='o-')
    ax[0,1].set_title("5-D Vol (r1=5, r2=3,a=2)")
    ax[1,1].scatter(np.sqrt(n_array), u5)
    ax[1,1].set_title("5-D Uncert")
    ax[1,1].set_xlabel("Sqrt(N)")
    ax[0,2].errorbar(np.sqrt(n_array), d3, yerr=u3, fmt='o-')
    ax[0,2].set_title("3-D Vol (r1=5, r2=3,a=2)")
    ax[1,2].scatter(np.sqrt(n_array), u3)
    ax[1,2].set_title("3-D Uncert")
    ax[1,2].set_xlabel("Sqrt(N)")

    plt.savefig("convergence.png")
