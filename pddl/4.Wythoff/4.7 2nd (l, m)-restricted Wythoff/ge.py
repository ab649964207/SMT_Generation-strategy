import os

def generate(l,m,v2):
    l=str(l)
    m=str(m)
    v2=str(v2)

    filename = os.path.dirname(__file__)+'\(l,m)-2nd-wythoff(l-%s,m-%s)v2-%s.pddl'%(l,m,v2)
    # filename = os.path.dirname(__file__)+'\st(lm)wythoff(l-1,m-1)v2-1.pddl'

    print(filename)
    content='''(define (domain Wythoff_game)
    (:objects ?v1 ?v2)
    (:tercondition (and (= ?v1 0) (= ?v2 0)))
    (:constraint (and (>= ?v1 0) (>= ?v2 0) (<= ?v2 %s)))
    (:action take1
        :parameters (?k ?l)
        :precondition (and (>= ?v1 ?k) (>= ?k 0)  (>= ?v2 ?l) (>= ?l 0)  (> (+ ?k ?l) 0) (or (and (< (- ?k ?l) %s) (> ?k ?l)) (and (< (- ?l ?k) %s) (> ?l ?k))  (> %s ?k)  (> %s ?l) ))
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?l))))
)
    '''%(v2,m,m,l,l)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return

for v2 in range (0,6):
    for l in range (1,6):
        for m in range (1,6):
            generate(l,m,v2)
# generate(1,1,1)