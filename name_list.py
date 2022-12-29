

def get_words_from_file(file):
    words_str = ""
    words = []

    with open(file, "r") as f:
        words_str = f.read()

    words = words_str.split(" ")
    return words


if __name__ == "__main__":
    print(get_words_from_file("Words/adj_en"))
