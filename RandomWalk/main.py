from walker import Walker

def main():
    random_walker = Walker()
    random_walker.makeStreet()
    print(random_walker.output)
    random_walker.walk()

if __name__ == "__main__":
    main()