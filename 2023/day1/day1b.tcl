proc first_digit {s} {
    set len [string length $s]
    set i 0

    while { $i < $len } {
        set c [string index $s $i]

        if { [string is digit $c] } {
            return $c
        }

        incr i
    }
}

proc last_digit {s} {
    set len [string length $s]
    set i [expr $len - 1]

    while { $i >= 0 } {
        set c [string index $s $i]

        if { [string is digit $c] } {
            return $c
        }

        incr i -1
    }
}

set infile [open [lindex $argv 0] r]
set total 0

while { [gets $infile line] >= 0 } {
    set line [string map {one 1 two 2 three 3 four 4 five 5 six 6 seven 7 eight 8 nine 9} $line]
    set cal [string cat [first_digit $line] [last_digit $line]]
    set total [expr $total + $cal]
}

puts $total
