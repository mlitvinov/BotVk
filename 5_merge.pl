% merge 2 sorted lists L1 and L2
% checking for list emptiness
mrg(L1, [], L1).
mrg([], L2, L2).
mrg([],[],[]).

% main rule: less element goes first in a result list
% we're getting head elements from both of lists when compare them
% if head element of L1 smaller than L2 head element - we put it to the output
% after we do recursive call where put tail of L1 and whole L2 
% also we use cut here instead of additional condition below (can replace by checking H1 > H2)
mrg([H1|T1], [H2|T2], [H1|T]):-
	H1 =< H2, !, 
	mrg(T1, [H2|T2], T).

% if current element of L2 is bigger than element of L1
% we put L2 head element into the T(output) head
mrg([H1|T1], [H2|T2], [H2|T]):-
	mrg([H1|T1], T2, T).

% ?- mrg([2,4,7,7,8],[1,2,3,7],Result).
% Result = [1, 2, 2, 3, 4, 7, 7, 7, 8] 
