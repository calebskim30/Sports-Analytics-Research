import requests
import pandas as pd
import numpy as np

data = {
    "Date": [
        "Nov 15, 2023", "Nov 16, 2023", "Nov 17, 2023", "Nov 18, 2023", "Nov 28, 2023", "Nov 30, 2023",
        "Dec 2, 2023", "Dec 5, 2023", "Dec 8, 2023", "Dec 11, 2023", "Dec 14, 2023", "Dec 15, 2023",
        "Dec 16, 2023", "Dec 22, 2023", "Dec 27, 2023", "Dec 28, 2023", "Dec 29, 2023", "Dec 30, 2023",
        "Jan. 3, 2024", "Jan. 5, 2024", "Jan. 9, 2024", "Jan. 12, 2024", "Jan. 16, 2024",
        "Jan. 19, 2024", "Jan. 23, 2024", "Jan. 26, 2024", "Jan. 30, 2024", "Feb. 1, 2024"
    ],
    "Opponent": [
        "Kingman High School", "Verdugo Hills", "Trabuco Hills", "Portola", "Magnolia Science Academy",
        "Legacy College Prep", "Hueneme High School", "Sherman Indian", "Eastside Christian",
        "Verbum Dei", "Anaheim High", "Huntington Beach", "Yorba Linda", "Avalon", "Desert Hot Springs", "Palo Verde Valley",
        "Xavier Prep High", "Royal High School",
        "Katella Knights", "Godinez High", "Segerstrom High", "Garden Grove High", "Westminster High",
        "Katella Knights", "Godinez High", "Segerstrom High", "Garden Grove High", "Westminster High"
    ],
    "Home/Away": [
        "Home", "Home", "Home", "Home", "Away", "Home", "Home", "Away", "Away", "Home", "Neutral",
        "Neutral", "Neutral", "Away", "Neutral", "Neutral", "Neutral", "Neutral",
        "Home", "Away", "Away", "Home", "Home", "Away", "Home", "Home", "Away", "Away"
    ],
    "Points OVHS": [73, 42, 19, 53, 84, 65, 65, 66, 86, 47, 69, 32, 30, 72, 55, 49, 54, 45, 65, 44, 46, 66, 64, 52, 54, 52, 58, 57],
    "Points Opponent": [38, 65, 71, 75, 25, 19, 29, 33, 10, 68, 52, 55, 69, 31, 27, 44, 41, 62, 61, 57, 52, 58, 72, 61, 62, 61, 61, 87],
    "Rebounds OVHS": [31, 31, 24, 31, 46, 30, 42, 42, 44, 30, 43, 32, 26, 45, 42, 32, 26, 29, 45, 36, 34, 31, 31, 39, 28, 29, 35, 31],
    "Rebounds Opponent": [39, 31, 36, 37, 38, 25, 30, 36, 19, 35, 26, 32, 48, 25, 30, 38, 31, 32, 31, 32, 22, 17, 26, 39, 36, 23, 32, 37],
    "Assists OVHS": [15, 5, 4, 14, 17, 15, 11, 21, 15, 9, 18, 3, 6, 16, 12, 15, 19, 14, 16, 11, 10, 21, 16, 12, 15, 16, 9, 10],
    "Assists Opponent": [9, 14, 20, 18, 0, 3, 7, 7, 1, 9, 15, 8, 13, 8, 4, 11, 7, 11, 21, 12, 10, 16, 14, 9, 16, 18, 9, 18],
    "Steals OVHS": [15, 3, 3, 7, 24, 23, 12, 21, 22, 6, 11, 3, 1, 11, 10, 8, 9, 8, 15, 2, 5, 6, 4, 3, 6, 5, 5, 2],
    "Steals Opponent": [7, 16, 11, 15, 7, 3, 5, 12, 3, 17, 6, 15, 10, 6, 7, 8, 7, 7, 12, 7, 16, 5, 10, 12, 10, 8, 6, 11],
    "Blocks OVHS": [0, 1, 0, 1, 0, 1, 2, 0, 0, 0, 1, 2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 8, 3, 1, 1, 0, 2, 1],
    "Blocks Opponent": [2, 4, 2, 3, 2, 1, 0, 5, 0, 2, 2, 1, 3, 3, 3, 7, 0, 1, 2, 4, 1, 1, 5, 2, 6, 0, 3, 4],
    "FG% OVHS": [44, 39, 9, 36, 46, 47, 43, 40, 54, 33, 43, 31, 23, 42, 34, 35, 43, 36, 43, 33, 39, 50, 50, 29, 38, 42, 45, 41],
    "FG% Opponent": [35, 44, 58, 46, 20, 26, 22, 24, 11, 47, 40, 38, 42, 29, 26, 37, 36, 45, 35, 37, 43, 48, 43, 38, 45, 43, 37, 50],
    "3PT% OVHS": [39, 19, 0, 31, 24, 23, 25, 24, 32, 22, 31, 0, 15, 21, 30, 23, 35, 29, 20, 11, 17, 42, 33, 24, 28, 18, 19, 25],
    "3PT% Opponent": [11, 32, 25, 23, 22, 0, 20, 15, 5, 35, 41, 6, 19, 22, 6, 33, 32, 30, 33, 29, 31, 59, 35, 47, 38, 39, 38, 36],
    "FT% OVHS": [62, 27, 69, 40, 43, 30, 88, 67, 67, 69, 52, 62, 46, 45, 67, 55, 56, 83, 46, 50, 39, 65, 46, 57, 65, 65, 54, 54],
    "FT% Opponent": [50, 100, 67, 73, 75, 50, 50, 71, 33, 60, 43, 100, 80, 75, 20, 50, 45, 75, 78, 82, 58, 40, 82, 50, 30, 80, 71, 50]
}

df = pd.DataFrame(data)

#Win/Loss Indicator (in terms of OVHS)
df['Win/Loss'] = df.apply(lambda row: 'Win' if row['Points OVHS'] > row['Points Opponent'] else 'Loss', axis=1)
column_order = df.columns.tolist()
column_order.insert(3, column_order.pop(column_order.index('Win/Loss')))
df['Win_Loss_Numeric'] = df['Win/Loss'].apply(lambda x: 1 if x == 'Win' else 0)
df = df[column_order]

df