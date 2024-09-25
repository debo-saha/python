books = [
    {
        "title": "python ",
        "author": "Breat lee",
        "year": 1960
    },
    {
        "title": "cricket",
        "author": "MSD",
        "year": 1949
    },
    {
        "title": "Finished",
        "author": "Debo",
        "year": 1813
    },
    {
        "title": "Show",
        "author": "Franklin",
        "year": 1925
    },
    {
        "title": "Rocking",
        "author": "salaman",
        "year": 1999
    }
]
year=[]
for book in books:
    if book["year"]>1950:
        year.append(book["title"])
print(year)