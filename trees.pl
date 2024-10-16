% person(Name, Age, Gender)

get_age(person(_, Age, _), Age).

:-
    P = person('Juan', 29, gender('M')),
    get_age(P, Age).