library = {'AI and ML related books':'shelf no. 2','engineering mathematics':'shelf no. 4','engineering physics':'shelf no. 1','engineering chemistry':'shelf no. 5','python books':'shelf no. 1','HTML/CSS books':'shelf no. 10','javascript books':'shelf no. 7','java books': 'shelf no. 13','SQL books':'shelf no. 11','data science books':'shelf no. 9','magazines':'shelf no. 20','newspaper':'shelf no.19','novels':'shelf no. 12','civil engineering books':'shelf no. 15','mechanical engineering books':'shelf no. 17','electronic and electrical engineering books':'shelf no. 16','aerospace engineering books':'shelf no. 18','CSE fundamental books':'shelf no. 14'}

#1.Get input and normalize letters casing to avoid case-sensitivity issues
book_name = input("Enter the name of the book: ").strip().lower()

#2.search using lower keys found = false
found = False
for key, value in library.items():
  if key.lower()==book_name:
    print(f"Location:{value}")
    found = True
    break

#3.Handel missing entries
if not found:
  print("Sorry the book category was not found in the library")
  # The line below is redundant if the above print statement is sufficient,
  # but if you want to use library.get, it should be like this:
  # shelf=library.get(book_name,"book not found in library.")
  # print(shelf)
