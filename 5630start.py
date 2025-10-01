import sys
import numpy as np

def main():
    # Check if the user provided the correct number of arguments
    if len(sys.argv) != 6:
        print(f"Usage: {sys.argv[0]} <int1> <int2> <double> <double> <double>")
        sys.exit(1)  # Exit with error code

    # Parse the command-line arguments
    try:
        d = int(sys.argv[1])         # First integer
        N = int(sys.argv[2])         # Second integer
        r1 = float(sys.argv[3])      # First double
        r2 = float(sys.argv[4])      # Second double
        a = float(sys.argv[5])       # Third double
    except ValueError:
        print("Error: Please provide valid integers and doubles as arguments.")
        sys.exit(1)  # Exit with error code

    # ******* Add your code here

    lenght = max(r1, r2)
    z = max(r1, r2+a)
    box_dim = np.append(np.ones(d-1)*lenght, z)

    points = np.random.uniform(-box_dim, box_dim, (N, d))

    dist1 = np.linalg.norm(points, axis=1)
    dist2 = np.linalg.norm(points+np.append(np.zeros(d-1), a), axis=1)


    inside = np.dot(np.where(dist1<=r1, 1, 0), np.where(dist2<=r2, 1, 0))


    dev = np.sqrt((inside-inside**2/N)/(N-1))

    
    volume = np.prod(2*box_dim)*inside/N
    stdev = dev/np.sqrt(N)


    
    # *******

    # Do not change the format below
    print(f"(r1,r2): {r1} {r2}")
    print(f"(d,N,a): {d} {N} {a}")
    print(f"volume: {volume}")
    print(f"stat uncertainty: {stdev}")

if __name__ == "__main__":
    main()
