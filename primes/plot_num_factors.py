import matplotlib.pyplot as plt
from num_factors import get_prime_factors


def main(MAX: int):
    MAX_N = 10
    X = list(range(2, MAX + 1))
    Y = [len(get_prime_factors(x)) for x in X]

    plt.figure(figsize=(12, 6))
    colors = plt.cm.tab10.colors if MAX_N <= 10 else plt.cm.tab20.colors
    for idx, n in enumerate(range(1, MAX_N + 1)):
        cumulative = []
        count = 0
        for i, y in enumerate(Y):
            if y == n:
                count += 1
            cumulative.append(count)
        color = colors[idx % len(colors)]
        plt.plot(X, cumulative, label=f"n = {n}", color=color)
        # Annotate at the end of the curve
        plt.annotate(
            f"n={n}",
            xy=(X[-1], cumulative[-1]),
            xytext=(5, 0),
            textcoords="offset points",
            color=color,
            fontsize=10,
            va="center",
            fontweight="bold",
        )
    plt.title(
        f"Cumulative Count of Numbers with n Prime Factors (n=1..{MAX_N}) up to {MAX}"
    )
    plt.xlabel("Number (x)")
    plt.ylabel("Count of numbers with n prime factors ≤ x")
    # plt.legend(title="n", loc="upper left", bbox_to_anchor=(1, 1))  # Legend removed
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout(rect=[0, 0, 0.85, 1])
    image_path = f"primes/num_factors_cumulative_plot_{MAX}.png"
    plt.savefig(image_path, dpi=150, bbox_inches="tight")
    print(f"Saved {image_path}")
    # plt.show()  # Uncomment to display interactively


if __name__ == "__main__":
    for MAX in [100, 1000, 10_000, 100_000, 200_000]:
        main(MAX)
