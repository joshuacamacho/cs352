;Problem 4
(defun op-some (condition op a)
	(map 'list (lambda (x) 
					(cond 
						((funcall condition x) (funcall op x))
						(T x)
					)
				)
			a
	)
)

(op-some #'oddp #'(lambda (x) (* x x)) ())
(op-some #'oddp #'(lambda (x) (* x x)) `(2))
(op-some #'oddp #'(lambda (x) (* x x)) `(3))
(op-some #'oddp #'(lambda (x) (* x x)) `(3 6 4 5 2))

;output

; (op-some #'oddp #'(lambda (x) (* x x)) ())

; NIL
; >>(op-some #'oddp #'(lambda (x) (* x x)) `(2))

; (2)
; >>(op-some #'oddp #'(lambda (x) (* x x)) `(3))

; (9)
; >>(op-some #'oddp #'(lambda (x) (* x x)) `(3 6 4 5 2))

; (9 6 4 25 2)