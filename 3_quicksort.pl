% my implementation of qsort() using Prolog
% actually, it's often used algorithm and probably has similar implementations

qsort([],[]).
qsort([Head|Tail],Sorted) :-

	% we need to divide array on 2 parts using special "pivot" value
	% in our case pivot is just the first value
	partition(Head,Tail,Less,Greater),

	% then we use qsort() for left side that has elements less than pivot
	qsort(Less,SortedLess),

	% and for the right side, where elements are bigger than pivot
	qsort(Greater,SortedGreater),

	% we use append to get sorted parts together (pivot is included like head in greater part)
	append(SortedLess,[Head|SortedGreater],Sorted).

partition(_,[],[],[]).
% here we analyze and compare all elements with pivot
partition(Pivot,[Head|Tail], [Head|Less], Greater) :-
	
	% (oh, wonderful "=<" sign. I ve spent half an hour to fix bug of using "<=" instead)
	Head =< Pivot, partition(Pivot,Tail,Less,Greater).

partition(Pivot,[Head|Tail], Less, [Head|Greater]) :-
	% if element greater than pivot we put it into the less part
	partition(Pivot,Tail,Less,Greater).

%?- qsort([9,1,0,-1,-20,11,100,-22],Sorted).
%Sorted = [-22, -20, -1, 0, 1, 9, 11, 100] 
