derivate(const(_), const(0)).
derivate(var(x), const(1)).
derivate(F + G, F_prime + G_prime) :-
    derivate(F, F_prime),
    derivate(G, G_prime)
.
derivate(F * G, F_prime * G + F * G_prime) :-
    derivate(F, F_prime),
    derivate(G, G_prime)
.

derivate(call(F, G), call(F_prime, G) * G_prime) :-
    derivate(F, F_prime),
    derivate(G, G_prime)
.

simplify(const(0) * _, const(0)) :- !.
simplify(_ * const(0), const(0)) :- !.
simplify(const(1) * F, F_s) :- simplify(F, F_s), !.
simplify(F * const(1), F_s) :- simplify(F, F_s), !.
simplify(F + const(0), F_s) :- simplify(F, F_s), !.
simplify(const(0) + F, F_s) :- simplify(F, F_s), !.
simplify(F, F).

derivate_simplify(F, F_simplified) :- 
    derivate(F, F_prime), 
    simplify(F_prime, F_simplified)
.

test(H, H_prime) :-
    F = const(2)*var(x)+const(10),
    G = var(x) * var(x),
    H = call(F, G),
    derivate_simplify(H, H_prime)
.

