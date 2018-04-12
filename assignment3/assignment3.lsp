(setf x  nil)
(loop for num from 0 to 20
     do (setf x (cons (random 100) x)))
(print x)

(setf x  nil)
(loop for num from 0 to 20
     do (setf x (cons (random 80.0) x)))
(print x)

(defun single (item)
  (setf s "")
  (cond ( (> (car item) 0 )
    (setf s "+")) )
  (format nil "~A~Ax^~A" s (car item) (car (cdr item))) 
)

(defun write-poly (listSet)
   (setf full "")
   (loop for item in listSet
	do (setf full (format nil "~A ~A" full (single item))))
   (print full)
   )
(write-poly nil)
(write-poly (list (list 2 1) (list 1 0)) )
(write-poly (list (list 3 2) (list -1 0)) )
(write-poly (list (list 5 2) (list -4 1) (list 1 0)) )
(write-poly (list (list 7 14) (list 11 13) (list -3 2) (list 7 1) (list -5 0)) )
(write-poly (list (list 1 0) (list 2 1) (list -5 3) (list -3 1) (list 7 0)) )
