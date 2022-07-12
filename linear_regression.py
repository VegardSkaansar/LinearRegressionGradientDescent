import numpy as np


class LinearRegression:

    def __init__(self, features, labels, learning_rate=0.1, iterations=1000):
        self.features = features
        self.labels = labels
        self.learning_rate = learning_rate
        self.iterations = iterations

        self.m = 0
        self.b = 0

    def train(self):
        for i in range(0, self.iterations):
            self.gradient_descent()

    def gradient_descent(self):
        self


