set line1 ""
set line2 ""

set partSum 0

proc have_non_dot_digit {s} {
    set len [string length $s]
    set i 0

    while {$i < $len} {
        set c [string index $s $i]

        if {!([string is digit $c]) && !([string equal "." $c])} {
            return 1
        }

        incr i
    }

    return 0
}

proc process_line {before current after} {
    global gears
    global partSum

    set len [string length $current]
    set len_m1 [expr $len - 1]
    set start 0

    while {$start < $len} {
        set match [list -1 -1]

        regexp -indices -start $start -- {[0-9]+} $current match

        set matchStart [lindex $match 0]
        set matchEnd [lindex $match 1]

        if {$matchStart < 0} {
            break
        }

        set matchValue [string range $current $matchStart $matchEnd]
        set haveSymbol 0

        if {$matchStart > 0} {
            incr matchStart -1

            if {[have_non_dot_digit [string index $current $matchStart]]} {
                set haveSymbol 1
            }
        }

        if {$matchEnd < $len_m1} {
            incr matchEnd

            if {[have_non_dot_digit [string index $current $matchEnd]]} {
                set haveSymbol 1
            }
        }

        if {[string length $before] > 0 && [have_non_dot_digit [string range $before $matchStart $matchEnd]]} {
            set haveSymbol 1
        }

        if {[string length $after] > 0 && [have_non_dot_digit [string range $after $matchStart $matchEnd]]} {
            set haveSymbol 1
        }

        if {$haveSymbol} {
            set partSum [expr $partSum + $matchValue]
        }

        set start [expr $matchEnd + 1]
    }
}

set infile [open [lindex $argv 0] r]

while { [gets $infile line3] >= 0 } {
    process_line $line1 $line2 $line3
    set line1 $line2
    set line2 $line3
}

process_line $line1 $line2 ""

puts $partSum
