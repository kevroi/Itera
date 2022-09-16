from walker import Walker

def main():
    random_walker = Walker(street_length=10, timesteps=10, start_at=0, p=0.5)
    random_walker.walk()

if __name__ == "__main__":
    main()