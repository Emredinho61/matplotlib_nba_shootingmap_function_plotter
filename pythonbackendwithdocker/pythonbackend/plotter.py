import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.patches import Circle, Rectangle, Arc
import seaborn as sns

"""
plotter.py: Script that holds the classes of each Plotter used in the frontend. This document contains the classes for
plotting:
- Simple Plots
- Bar Plots
- Pie Plots
- Trigonometric Plots
- NBA Shooting Plots per Player
"""


class SimplePlot:
    """
    Used to plot simple plots with equations that are inputed into the frontend.
    """

    def __init__(self, fun, start, stop, xlabel, ylabel, title):
        self.fun = fun
        self.start = start
        self.stop = stop
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.title = title

    def plotSimplePlot(self):
        plt.style.use('default')
        # evenly spaced numbers in the interval of start and stop
        x = np.linspace(self.start, self.stop, 100)

        # inputed equation is of type string and must be changed to a equation
        y = eval(self.fun)

        fig, ax = plt.subplots(figsize=(5, 5))

        # plot the graph
        ax.plot(
            x, y, label=self.fun, color="blue", markersize=3
        )

        # set the labels and the title
        ax.set(
            xlabel=self.xlabel,
            ylabel=self.ylabel,
            title=self.title,
        )

        # staticly set a grid
        ax.grid(True, linestyle="--", alpha=0.7)

        # display the legend
        ax.legend()

        ax.set_facecolor("#f0f0f0")

        # we save the file relatively -> subfolder plots
        save_path = os.path.join("pythonbackend/plots", "simplePlot.png")
        fig.savefig(save_path, bbox_inches="tight")


class BarPlot:
    """
    Used to plot bar charts with values that are inputed into the frontend.
    """

    def __init__(self, names, vals, colors, xlabel, ylabel, title):
        self.names = names
        self.vals = vals
        self.colors = colors
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.title = title

    def plotBarPlot(self):
        plt.style.use('default')
        fig, ax = plt.subplots(figsize=(5, 5))
        bars = ax.bar(self.names, self.vals, color=self.colors, width=0.5)

        # the labels of the plots are generated and put over the bars such that the labels are centered to the width
        # of the bars
        for bar in bars:
            height = bar.get_height()
            ax.annotate(
                f"{height}",
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
            )

        # set the title and labels
        ax.set(
            xlabel=self.xlabel,
            ylabel=self.ylabel,
            title=self.title,
        )

        # set a grid for better comparison of the heights of the bars
        ax.grid(True, linestyle="--", alpha=0.7)
        ax.set_axisbelow(True)
        # set a fancy (cuz rotated) label for each bar with the names set
        ax.tick_params(axis="x", rotation=45, labelrotation=45)

        # we save the file relatively -> subfolder plots
        save_path = os.path.join("pythonbackend/plots", "barPlot.png")
        fig.savefig(save_path, bbox_inches="tight")


class PiePlot:
    """
    Used to plot pie charts with values that are inputed into the frontend.
    """

    def __init__(self, names, vals, colors, title):
        self.names = names
        self.vals = vals
        self.colors = colors
        self.title = title

    def plotPieChart(self):
        # use a style sheet according to: https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
        plt.style.use("_mpl-gallery-nogrid")

        labels = self.names

        fig, ax = plt.subplots(figsize=(5, 5))

        # plot pie chart with labels, some spacing, colors...
        ax.pie(
            self.vals,
            labels=labels,
            colors=self.colors,
            autopct="%1.1f%%",
            startangle=90,
            wedgeprops={"linewidth": 1, "edgecolor": "white"},
        )

        ax.legend(labels, loc="upper left", bbox_to_anchor=(1, 1))

        # Set aspect ratio to be equal, so the pie is circular
        ax.axis("equal")

        ax.set(title=self.title)

        # we save the file relatively -> subfolder plots
        save_path = os.path.join("pythonbackend/plots", "piePlot.png")
        fig.savefig(save_path, bbox_inches="tight")


class TrigPlot:
    """
    Used to plot trigonmetric Plots.
    """

    def __init__(self, mode, start, stop, numOfSamples, a, b, c, d, title):
        self.mode = mode
        self.start = start
        self.stop = stop
        self.numOfSamples = numOfSamples
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.title = title

    def plotTrigPlot(self):
        # use a style sheet according to: https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
        plt.style.use("_mpl-gallery")

        # need to distinguish between 3 cases -> sin, cos, tan
        if self.mode == "sin":
            x = np.linspace(self.start, self.stop, 100)
            y = self.d + self.a * np.sin(self.b * x + self.c)

            fig, ax = plt.subplots(figsize=(5, 5))

            ax.plot(x, y, linewidth=2.0)

            ax.set(title=self.title)

            # we save the file relatively -> subfolder plots
            save_path = os.path.join(
                "pythonbackend/plots", "trigPlot.png"
            )

            fig.savefig(save_path, bbox_inches="tight")
        elif self.mode == "cos":
            x = np.linspace(self.start, self.stop, 100)
            y = self.d + self.a * np.cos(self.b * x + self.c)

            fig, ax = plt.subplots(figsize=(5, 5))

            ax.plot(x, y, linewidth=2.0)

            ax.set(title=self.title)

            # we save the file relatively -> subfolder plots
            save_path = os.path.join(
                "pythonbackend/plots", "trigPlot.png"
            )
            fig.savefig(save_path, bbox_inches="tight")
        else:
            x = np.linspace(self.start, self.stop, 100)
            y = self.d + self.a * np.tan(self.b * x + self.c)

            fig, ax = plt.subplots(figsize=(5, 5))

            ax.plot(x, y, linewidth=2.0)

            ax.set(title=self.title)

            # we save the file relatively -> subfolder plots
            save_path = os.path.join(
                "pythonbackend/plots", "trigPlot.png"
            )
            fig.savefig(save_path, bbox_inches="tight")


class NbaShootingMapPlotter:
    """
    Plot a shooting "Heat Map" out of the Stats from stat.nba.com. Plots are generated per season and per player,
    distinguished between made and missed shots.
    """

    def __init__(self, loc_x, loc_y, missed, playername, season, heatmap):
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.missed = missed
        self.playername = playername
        self.season = season
        self.heatmap = heatmap

        # range of shot data
        self.original_x_min = -30
        self.original_x_max = 30
        self.original_y_min = 0
        self.original_y_max = 40

        # range of basketball court dimensions
        self.new_x_min = -300
        self.new_x_max = 300
        self.new_y_min = -47.5
        self.new_y_max = 350

    def scale_coordinate(self, coord, orig_min, orig_max, new_min, new_max):
        # the shot coordinates are for a court of x range: 30 : -30 and y range 0 : 40 so we need to scale
        return ((coord - orig_min) / (orig_max - orig_min)) * (new_max - new_min) + new_min

    def scale_x(self):
        # scale every x-coordinate
        scaled_x = []
        for oneX in self.loc_x:
            scaled_x.append(self.scale_coordinate(oneX, self.original_x_min, self.original_x_max, self.new_x_min,
                                                  self.new_x_max))
        return scaled_x

    def scale_y(self):
        # scale every y-coordinate
        scaled_y = []
        for oneY in self.loc_y:
            scaled_y.append(self.scale_coordinate(oneY, self.original_y_min, self.original_y_max, self.new_y_min,
                                                  self.new_y_max))
        return scaled_y

    def draw_court(self, ax=None, color="black", lw=2, outer_lines=False):
        plt.style.use('default')
        # Shoutout to: http://savvastjortjoglou.com/nba-shot-sharts.html for creating an easy tutorial on how to draw
        # an basketball court

        # If an axes object isn't provided to plot onto, just get current one
        if ax is None:
            ax = plt.gca()

        # basketball hoop
        hoop = Circle((0, 0), radius=7.5, linewidth=lw, color=color, fill=False)

        # backboard
        backboard = Rectangle((-30, -7.5), 60, -1, linewidth=lw, color=color)

        # outer box 0f the paint
        outer_box = Rectangle(
            (-80, -47.5), 160, 190, linewidth=lw, color=color, fill=False
        )

        # inner box of the paint
        inner_box = Rectangle(
            (-60, -47.5), 120, 190, linewidth=lw, color=color, fill=False
        )

        # free throw top arc
        top_free_throw = Arc(
            (0, 142.5),
            120,
            120,
            theta1=0,
            theta2=180,
            linewidth=lw,
            color=color,
            fill=False,
        )

        # free throw bottom arc
        bottom_free_throw = Arc(
            (0, 142.5),
            120,
            120,
            theta1=180,
            theta2=0,
            linewidth=lw,
            color=color,
            linestyle="dashed",
        )

        # Restricted Arc
        restricted = Arc(
            (0, 0), 80, 80, theta1=0, theta2=180, linewidth=lw, color=color
        )

        # Three point line
        corner_three_a = Rectangle((-220, -47.5), 0, 140, linewidth=lw, color=color)
        corner_three_b = Rectangle((220, -47.5), 0, 140, linewidth=lw, color=color)

        # 3pt arc
        three_arc = Arc(
            (0, 0), 475, 475, theta1=22, theta2=158, linewidth=lw, color=color
        )

        # Center Court
        center_outer_arc = Arc(
            (0, 422.5), 120, 120, theta1=180, theta2=0, linewidth=lw, color=color
        )
        center_inner_arc = Arc(
            (0, 422.5), 40, 40, theta1=180, theta2=0, linewidth=lw, color=color
        )

        # List of the court elements to be plotted onto the axes
        court_elements = [
            hoop,
            backboard,
            outer_box,
            inner_box,
            top_free_throw,
            bottom_free_throw,
            restricted,
            corner_three_a,
            corner_three_b,
            three_arc,
            center_outer_arc,
            center_inner_arc,
        ]

        if outer_lines:
            # Draw the half court line, baseline and side out bound lines
            outer_lines = Rectangle(
                (-250, -47.5), 500, 470, linewidth=lw, color=color, fill=False
            )
            court_elements.append(outer_lines)

        # Add the court elements onto the axes
        for element in court_elements:
            ax.add_patch(element)

        return ax

    def drawPointsOnCourt(self):
        if self.heatmap == "False":
            plt.style.use('default')
            fig, ax = plt.subplots(figsize=(12, 11))

            # distinguish between to cases: missed and made shots
            if self.missed == "False":
                # made shot is marked with green dot
                plt.scatter(self.scale_x(), self.scale_y(), marker='o', c="green")
                ax.set_title(label=f"{self.playername} Made Shots in Season {self.season}", fontsize=18)

                # data source
                ax.text(-250, 480, 'Data Source: stats.nba.com', fontsize=12)
            else:
                # missed shot is marked with red cross
                plt.scatter(self.scale_x(), self.scale_y(), marker='x', c="red")
                ax.set_title(label=f"{self.playername} Missed Shots in Season {self.season}", fontsize=18)

                # data source
                ax.text(-250, 480, 'Data Source: stats.nba.com', fontsize=12)
            self.draw_court(outer_lines=True)

            # x-y ranges
            plt.xlim(-250, 250)
            plt.ylim(-47.5, 422.5)

            # we save the file relatively -> subfolder plots
            save_path = os.path.join("pythonbackend/plots",
                                     "nbaPlot.png"
                                     )
            fig.savefig(save_path)
        else:
            plt.style.use('default')
            fig, ax = plt.subplots(figsize=(12, 11))
            # plot a heatmap
            sns.kdeplot(x=self.scale_x(), y=self.scale_y(), cmap="YlOrRd_r", fill=True)

            # draw court
            self.draw_court(ax)
            plt.xlim(-250, 250)
            plt.ylim(-47.5, 422.5)
            if self.missed == "False":
                ax.set_title(label=f"{self.playername} Heatmap of Made Shots in Season {self.season}", fontsize=18)
                ax.text(-250, 480, 'Data Source: stats.nba.com', fontsize=12)
            else:
                ax.set_title(label=f"{self.playername} Heatmap of Missed Shots in Season {self.season}", fontsize=18)
                ax.text(-250, 480, 'Data Source: stats.nba.com', fontsize=12)
            save_path = os.path.join("pythonbackend/plots",
                                     "nbaPlot.png"
                                     )
            fig.savefig(save_path)
