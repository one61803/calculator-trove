(load-file "DEBUG.el")

(defun common-letter-count (string1$ string2$)
  "Count (and return) the quantity of letters in common between string1$ and string2$, considering both of them as multisets of letters. (I.e., find the multiset intersection between them, then return the cardinality of said intersection.)"
  (setq string1$ (downcase string1$))
  (setq string2$ (downcase string2$))
  (let (char$ (count 0) position (BUC! nil))
    (while (> (length string1$) 0)
      (setq char$ (substring string1$ 0 1))
      (DEBUG_%s BUC! t "char$ = %s" char$)
      (setq string1$ (substring string1$ 1))
      (DEBUG_%s BUC! t "string1$ = %s" string1$)
      (when (string-match char$ string2$)
        (setq count (1+ count))
        (setq position (string-match char$ string2$))
        (setq string2$ (concat (substring string2$ 0 position) (substring string2$ (1+ position))))))
    count))
					; (describe-function 'common-letter-count)

(defun harmonic-mean (natural1 natural2)
  "Returns the harmonic mean of natural numbers natural1 and natural2."
  (/ (* 2.0 natural1 natural2) (+ natural1 natural2)))
					; (describe-function 'harmonic-mean)

					;(defun are-litterally-communal (string1$ string2$)
(defun are-litterally-related (string1$ string2$)
  "Returns a Boolean indicating whether string1$ and string2$ are /littera/-lly related."
  (let (threshold count)
    (setq threshold (/ (harmonic-mean (length string1$) (length string2$)) 2))
    (setq count (common-letter-count string1$ string2$))
    (>= count threshold)))
; (describe-function 'are-litterally-related)
					;; (describe-function 'are-litterally-communal)

(defun litteral-relatedness (string1$ string2$)
  "Returns a score of litteral relatedness between words in string1$ and string2$."
  (let (upperbound count)
    (setq upperbound (harmonic-mean (length string1$) (length string2$)))
    (setq count (common-letter-count string1$ string2$))
    (/ (* 1.0 count) upperbound)))
; (describe-function 'litteral-relatedness)
