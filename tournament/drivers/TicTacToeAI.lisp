(defun parse-board (input)
  (coerce (string-trim '(#\Newline #\Return) input) 'list))

(defun main-loop ()
  (loop while (not (streamp *standard-input*))
        do (let ((input (read-line)))
             (let ((board (parse-board input)))
               ;; Implement AI logic here.
               ;; Choose an index (0-8) to replace.
               (let ((move 0)) ;; Replace with AI's move.
                 (format t "~a~%" move))))))

(main-loop)