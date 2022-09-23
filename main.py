from service import browse_by_times, browse_by_infinity, browse_by_close_open

if __name__ == "__main__":
    mode = input("choose mode 1: infinity mode 2: times mode 3: close-open node :")
    if mode not in ("1", "2", "3"):
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
    elif mode == "3":
        browse_by_close_open(url)
