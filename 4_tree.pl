% In the code below we use qsort() function from lab3.
% We have to build balanced binary tree using balanced_tree(List,Tree) function
% "empty" for empty tree and instant(Root,Left,Right) for tree instance (node).

qsort([],[]).
qsort([Head|Tail],Sorted) :-
	partition(Head,Tail,Less,Greater),
	qsort(Less,SortedLess),
	qsort(Greater,SortedGreater),
	append(SortedLess,[Head|SortedGreater],Sorted).

partition(_,[],[],[]).
partition(Pivot,[Head|Tail], [Head|Less], Greater) :-
	Head =< Pivot, partition(Pivot,Tail,Less,Greater).

partition(Pivot,[Head|Tail], Less, [Head|Greater]) :-
	partition(Pivot,Tail,Less,Greater).

% if empty input list - empty output tree
balanced_tree([], empty).

% if we have sorted list as an input list2tree function
% it's pretty simple to build a balanced tree
% we can just choose middle element in the sorted list and use it as a root 
balanced_tree(List, Tree) :- 
	% we need to get sorted list
	qsort(List, SortedList),
	% convert sorted list to the balanced tree
	list2tree(SortedList, Tree).

% if input list empty then tree branch(tree) is empty too
list2tree([],empty).

% function that converts sorted list to tree instant 
% we always choose Root like head of the RightPart list
% then we recursive convert left part of list to the left branch of tree
% and right part - to the right branch, respectively (they are already sorted, so
% there is no problem to get root from them - tree will stay balanced)
list2tree(List, instant(Root, Left, Right)) :- 
	divide(List, LeftPart, [Root | RightPart]),
	list2tree(LeftPart, Left),
	list2tree(RightPart, Right).

% function that divides input list on two parts
divide(List, LeftPart, RightPart) :-
	% here we get 2 parts of income lists in that length of the left part 
	% equals length of the input list div 2 (we can't use '/' if we want to get integer value)
	% 'div' operator also helps us to process odd or even length of the input list
	append(LeftPart, RightPart, List),
	length(List, ListLength),
	Middle is ListLength div 2,
	% Middle is actually (ListLength/2 or ListLength/2-0.5)
	length(LeftPart, Middle).

%?- balanced_tree([8,1,0,11,7,-2,2,8],Tree).
%Tree = instant(7, 
%	  instant(1, 
%		  instant(0, 
%			instant(-2, empty, empty), empty),
%	          instant(2, empty, empty)),
%	   instant(8,
%	  	  instant(8, empty, empty),
%		  instant(11, empty, empty))) 
