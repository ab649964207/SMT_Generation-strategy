(define (domain Subtraction_game-1-2-3-6)
	(:objects ?v1)
	(:tercondition (and (>= ?v1 0) (= ?v1 0) ))
	(:constraint (>= ?v1 0))
	(:action take
		:parameters (?k)
		:precondition (and (>= ?v1 ?k) (or (= ?k 1) (= ?k 2) (= ?k 3) (= ?k 6)))
		:effect (assign ?v1 (- ?v1 ?k)))
)