from sklearn.linear_model import LinearRegression
from DatabasePy import Database
from pandas import DataFrame
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np


class Graph:
    def __init__(self):
        self.D = Database('SQLite_Python.db', 'Database')
        self.data = {}

    def get_data_from_db(self):
        data = self.D.fetch()
        return data

    def sort_data(self):
        self.data = self.get_data_from_db()
        self.data = dict(sorted(self.data.items(), key=lambda kv: kv[1], reverse=True))
        first_ten_counties = dict(list(self.data.items())[:10])
        self.data = first_ten_counties
        return self.data

    def create_pie_chart(self):
        data = self.sort_data()
        keys = data.keys()
        values = [data[key] for key in keys]
        plt.pie(values, labels=keys, autopct = '%2.2f%%')
        plt.title('List of Countries by Carbon Dioxide Emissions')
        return plt

    def create_xy_plot(self):
        data = self.sort_data()
        keys = data.keys()
        values = [data[key] for key in keys]
        plt.plot(keys, values)

        plt.xlabel('Carbon Emission')
        plt.ylabel('Countries')
        plt.title('List of Countries by Carbon Dioxide Emissions')
        return plt

    def create_bar_chart(self):
        data = self.sort_data()
        keys = data.keys()
        values = [data[key] for key in keys]
        plt.bar(keys, values)

        plt.xlabel('Carbon Emission')
        plt.ylabel('Countries')
        plt.title('List of Countries by Carbon Dioxide Emissions')
        return plt

    def create_bar_chart1(self):
        data = self.sort_data()
        keys = data.keys()
        values = [data[key] for key in keys]

        y_pos = np.arange(len(keys))

        plt.bar(y_pos, values, align='center', alpha=0.5)
        plt.xticks(y_pos, keys)
        plt.xlabel('Carbon Emission')
        plt.ylabel('Countries')
        plt.title('List of Countries by Carbon Dioxide Emissions')
        return plt

    def create_linear_regression(self):
        data = self.sort_data()
        keys = data.keys()
        values = [data[key] for key in keys]

        X = DataFrame(keys).values.reshape(-1, 1)
        Y = DataFrame(values).values.reshape(-1, 1)

        linear_regressor = LinearRegression()  # create object for the class
        linear_regressor.fit(X, Y)  # perform linear regression
        Y_pred = linear_regressor.predict(X)  # make predictions
        plt.scatter(X, Y)
        plt.plot(X, Y_pred, color='red')
        plt.xlabel('Carbon Emission')
        plt.ylabel('Countries')
        plt.title('List of Countries by Carbon Dioxide Emissions')

        return plt


x = Graph()
# print(x.get_data_from_db())
# x.sort_data()
x.create_pie_chart()
# x.create_xy_plot()
# x.create_bar_chart()
# x.create_linear_regression()
plt.show()
