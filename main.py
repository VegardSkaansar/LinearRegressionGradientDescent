import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from linear_regression import LinearRegression


def main():
    cars = pd.read_csv(r'cars.csv', usecols=["mpg", "horsepower"])
    horsepower = cars.drop("mpg", axis=1)
    mpg = cars.drop("horsepower", axis=1)
    horsepower_train, horsepower_test, mpg_train, mpg_test = train_test_split(np.array(horsepower), np.array(mpg),
                                                                              test_size=0.1)
    print(mpg_test)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
