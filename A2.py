import numpy as np
import matplotlib.pyplot as plt


# ----------------Part A---------------------------------------
def run_simulation(no_of_samples):
    x, y = np.random.uniform(-1, 1, no_of_samples), np.random.uniform(-1, 1, no_of_samples)
    z = x * x + y * y
    positive = np.sum(z < 1)
    ans = 4 * positive / float(no_of_samples)
    plt.scatter(x[z < 1], y[z < 1], c='b')
    plt.scatter(x[z > 1], y[z > 1], c='r')
    plt.title("Estimated pi Value: " + str(ans))
    plt.savefig("circle_sample_no_" + str(no_of_samples) + ".png", bbox_inches='tight')
    plt.close()
    return ans


estimates = []
i = 10
while i <= 10000000:
    estimate = run_simulation(i)

    estimates.append(estimate)
    print("For Circle.", i, "samples taken. Estimated pi value:", run_simulation(i))
    i = i * 10
plt.plot(np.arange(7) + 1, estimates, label='Circle Estimate')
plt.axhline(y=np.pi, xmin=0, xmax=1, label='True Value', c='r', alpha=0.2)
plt.xlabel("No Of Samples")
plt.ylabel("Estimate")
plt.legend()


# ---------------Part B-----------------------------------------
def run_simulation(no_of_samples):
    x, y, z = np.random.uniform(-1, 1, no_of_samples), np.random.uniform(-1, 1, no_of_samples), \
              np.random.uniform(-1, 1, no_of_samples)
    r = x * x + y * y + z * z
    positive = np.sum(r < 1)
    ans = 6 * positive / float(no_of_samples)
    return ans


estimates = []
i = 10
while i <= 10000000:
    estimate = run_simulation(i * 10)
    estimates.append(estimate)
    print("For Sphere ", i, "samples taken. Estimated pi value:", run_simulation(i))
    i = i * 10
plt.plot(np.arange(7) + 1, estimates, label="Sphere Estimate")
# plt.axhline(y=np.pi, xmin=0, xmax=1, label="True Value",alpha=0.2)
plt.xlabel("No Of Samples")
plt.ylabel("Estimate")
plt.legend()
plt.savefig("sphere_circle_estimate.png")
