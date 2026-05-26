"CART·AM·ARE : CAlculation of Reading Target for AMAzon REviews"
"This is for calculating (using a statistical formula) how many Amazon reviews one should read (for a given product sold on Amazon) before deciding whether to order it or not."

(defun rating-positivity (percentage-5-stars percentage-4-stars percentage-3-stars)
  "Returns a decimal number between 0 and 1 which indicates the portion of ratings which are 3½ stars or above. First argument is percentage of reviews which are 5-star. Second argument is percentage of reviews which are 4-star. Third argument is percentage of reviews which are 3-star."
  (/ (+ percentage-5-stars percentage-4-stars (/ percentage-3-stars 2.0)) 100.0))
					; (describe-function 'rating-positivity)

(defun CARTAMARE1 (rating-positivity)
  "CAlculation of Reading Target for AMAzon REviews 1. Parameter rating-positivity is a decimal number between 0 and 1 (closed interval) that indicates “rating positivity” (fraction of ratings that are above 3.5 stars)."
  (/ (* (expt 1.645 2) rating-positivity (- 1 rating-positivity)) (expt 0.05 2)))
; (describe-function 'CARTAMARE1)

(defun CARTAMARE2 (num-reviews prototarget)
  "CAlculation of Reading Target for AMAzon REviews 2. First argument should be the number of ratings. The second argument should be the result obtained from CARTAMARE1. The output is the (lower/minimum bound to the) quantity of Amazon reviews that one should aim to read."
  (/ prototarget (1+ (/ prototarget num-reviews))))
; (describe-function 'CARTAMARE2)

(defun CARTAMARE (percentage-of-5-star-ratings percentage-of-4-star-ratings percentage-of-3-star-ratings number-of-reviews)
  "CAlculation of Reading Target for AMAzon REviews. (There are four parameters, whose names should make them rather self-explanatory.)"
  (CARTAMARE2 number-of-reviews (CARTAMARE1 (rating-positivity percentage-of-5-star-ratings percentage-of-4-star-ratings percentage-of-3-star-ratings))))
; (describe-function 'CARTAMARE)
