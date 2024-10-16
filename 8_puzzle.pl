/*
[
 [1,3,empty],
 [8,2,4],
 [7,6,5]
]

-- board_from -->

board_row(1,[1,3,empty]).
board_row(2,[8,2,4]).
board_row(3,[7,6,5]).

*/

/*
[1,2,3] [a, b, c] -> [[1,a], [2,b], [3, c]] zip
*/

%%%%%%%%%%%%%%%%%%%% UTILS %%%%%%%%%%%%%
zip(L, M, Z) :- maplist( [X, Y, [X, Y]] >> true, L, M, Z)
.
enumerate(L, EL) :-
    length(L, N),  numlist(1, N, LN), zip(LN, L, EL)
.
index_of(V, L, P) :- nth1(P, L, V).

new_id(B, I) :- gensym(B, I).

list_split(L, A, X, B) :-  append(A, [X | B], L).


list_set_value(L, I, V, LS) :-
   list_split(L, A, _, B),
   I1 is I - 1, I1 >= 0,
   length(A, I1),
   append(A, [V | B], LS)
.

list_at(L, I, V) :-
	nth1(I, L, V)
.
list_swap(L, I, J, LS):-
   list_at(L, I, VI), list_at(L, J, VJ),
   list_set_value(L, I, VJ, LJ),
   list_set_value(LJ, J, VI, LS)
.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
:- dynamic visited/1.
visited_clear :-
	retractall(visited(_))
.

set_visited(I) :-
	assert(visited(I))
.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

board_from(L, Id) :-
    board_new_id(Id),
    board_clear(Id),
    enumerate(L, EL),
    forall(member(R, EL), board_add(Id, R))
.

:- dynamic board_row/3.
:- dynamic board_empty/3.

board_new_id(I) :- new_id('board_', I).

board_clear_all :-
   retractall(board_row(_, _)),
   retractall(board_empty(_,_))
.
   
board_clear(Id) :-
   retractall(board_row(Id, _)),
   retractall(board_empty(Id,_))
.

board_clone(Id, IdC):-
   findall([RId, R], board_row(Id, RId, R), EL),
   board_new_id(IdC),
   forall(member(RC, EL), board_add(IdC, RC))
.

board_add(Id, [I, R]) :-
    assert(board_row(Id, I, R)),
    ( index_of(empty, R, J) -> board_add_empty(Id, I, J) ; true )
.
board_update(Id, I, RS) :-
    writeln(['***', Id, I, RS]),
    retract(board_row(Id, I, _)),
	board_add(Id, [I, RS])
.
board_add_empty(Id, I, J) :-
    retractall(board_empty(Id, _,_)),
    assert(board_empty(Id, I, J))
.

board_show(Id) :- 
   writeln('Board rows:'),
   findall([IR, Row], board_row(Id, IR, Row), LR),
   sort(LR, LRS),
   forall( member([I, R], LRS), writeln([I, R]) ),
   writeln('Empty at:'),
   board_empty(Id, EI, EJ),
   write([EI, EJ])
.

board_get_valid_move(Id, P, D) :-
    board_empty(Id, I, J),
    ( (I > 1, I1 is I - 1, P=[I1, J], D = up);
      (I < 3, I1 is I + 1, P=[I1, J], D = down);
      (J > 1, J1 is J - 1, P=[I, J1], D = left);
      (J < 3, J1 is J + 1, P=[I, J1], D = right))
.

board_apply_move(Id,D) :-
   board_get_valid_move(Id, [I, J1], D), 
   member(D, [left, right]),
   board_row(Id, I, R),
   board_empty(Id, I, J),
   list_swap(R, J, J1, RS),
   board_update(Id, I, RS)
.
board_child(Id, IdChild) :-
   board_clone(Id, IdChild), 
   board_apply_move(IdChild, _D)
.

board_is_visited(I) :-
  visited(I)
.
board_set_visited(I) :-
	assert(visited(I))
.

board_play_dfs(Id, Depth):-
   \+ board_is_visited(Id),
   board_set_visited(Id),
   findall(IdChild, board_child(Id, IdChild), ChildList),
   Depth > 0, 
   Depth1 is Depth - 1,
   forall(member(IdC, ChildList), board_play_dfs(IdC, Depth1))
.
test(Id) :-
  L = [
        [1,3,empty],
        [8,2,4],
        [7,6,5]],
   
  board_from(L, Id),
  board_show(Id)
.