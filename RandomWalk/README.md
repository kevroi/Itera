# Random Walks
Random walks are an example of a mathematical concept called stochastic processes. 'Stochastic' is a fancy word for random.

Consider a person on an infinitely long street. Each minute, they must take one step, with a probability $p$ of moving forward, and $1-p$ of moving backwards. Thats a random walk!

In this directory we simulate a random walk along a finite street of length `street_length` with walls at either end where the walker bounces back to where the same place they were if they try to go further. This is formally known as a random walk with partially reflecting boundaries. You can run this on your terminal by running `main.py` above as follows:
```
python main.py
```

Note that other types of boundaries can exist. Random walks with absorbing boundaries trap the user at the first wall they reach (think of really sticky walls), ending the stochastic process. Random walks with fully refelcting boundaries mean the walker will always take a step away from the wall if they reach the end of a street. These are yet to be implemented here.