(defun disc (a b c)
 (/ (sqrt (- (* b b) (* 4 a c ))) (* 2 a)) 
)

(defun top (a b)
 (/ (* -1 b) (* 2 a))
)

(defun quadratic (a b c)
  (cond ((= a 0)
    (return-from quadratic (/ (* -1 c) b)))
  )

  (list (+ (top a b) (disc a b c)) (- (top a b) (disc a b c)))

)

(print (quadratic 2 -1 -1))
(print (quadratic 1 4 4))
(print (quadratic 3 11 0))
(print (quadratic 4 0 8))
(print (quadratic 0 4 4))
