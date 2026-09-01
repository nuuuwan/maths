N = 100000000


def mirror(n: int) -> int:
    return int(str(n)[::-1])


def main():

    for i in range(1, N):
        mirror_i = mirror(i)
        if mirror_i == i:
            continue
        if len(str(i)) != len(str(mirror_i)):
            continue

        i3 = i**3
        mirror_i3 = mirror(i3)

        if mirror_i3 == mirror_i**3:
            print(i, mirror_i, i3, mirror_i3)


if __name__ == "__main__":
    main()
