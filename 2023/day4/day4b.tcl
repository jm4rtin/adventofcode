set infile [open [lindex $argv 0] r]
set totalCards 0

while { [gets $infile line] >= 0 } {
    regexp {Card\s+([0-9]+): (.*)} $line match cardNo numbers
    set numbers [split $numbers "|"]
    set winningNumbers [split [lindex $numbers 0] " "]
    set yourNumbers [split [lindex $numbers 1] " "]

    # https://stackoverflow.com/questions/5259294/how-to-remove-emty-elements-from-tcl-list
    set winningNumbers [lsearch -all -inline -not -exact $winningNumbers {}]
    set yourNumbers [lsearch -all -inline -not -exact $yourNumbers {}]
    set points 0

    foreach num $yourNumbers {
        if {[lsearch -exact $winningNumbers $num] >= 0} {
            incr points
        }
    }

    if {!([info exists cardCount($cardNo)])} {
        set cardCount($cardNo) 1
    }

    set i 1

    while {$i <= $points} {
        set bonusNo [expr $i + $cardNo]

        if {[info exists cardCount($bonusNo)]} {
            set cardCount($bonusNo) [expr $cardCount($bonusNo) + $cardCount($cardNo)]
        } else {
            set cardCount($bonusNo) [expr 1 + $cardCount($cardNo)]
        }

        incr i
    }

    set totalCards [expr $totalCards + $cardCount($cardNo)]
}

puts $totalCards
