from service import browse_by_times, browse_by_infinity

if __name__ == "__main__":
    mode = input("choose mode 1: infinity mode 2: times mode: ")
    if mode not in ("1", "2"):
        print("wrong mode!")
        exit()
    elif mode == "2":
        times = input("times: ")
    url = input("URL: ")
    if not url:
        print("empty url!")
        exit()
    if mode == "1":
        browse_by_infinity(url)
    elif mode == "2":
        browse_by_times(int(times), url)
