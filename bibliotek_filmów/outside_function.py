

def outside_function(title,library,get_series):
    series = get_series(library)
    count = 0
    for item in series:
        if item.title == title:
            count +=1
    print(f"Liczba odcinków serialu {title} - {count}")