set infile [open [lindex $argv 0] r]
set totalPoints 0

while { [gets $infile line] >= 0 } {
    regexp {Card\s+([0-9]+): (.*)} $line match cardNo numbers
    set numbers [split $numbers "|"]
    set winningNumbers [split [lindex $numbers 0] " "]
    set yourNumbers [split [lindex $numbers 1] " "]

    # https://stackoverflow.com/questions/5259294/how-to-remove-emty-elements-from-tcl-list
    set winningNumbers [lsearch -all -inline -not -exact $winningNumbers {}]
    set yourNumbers [lsearch -all -inline -not -exact $yourNumbers {}]
    set points -1

    foreach num $yourNumbers {
        if {[lsearch -exact $winningNumbers $num] >= 0} {
            incr points
        }
    }

    if {$points >= 0} {
        set points [expr 2 ** $points]
    } else {
        set points 0
    }

    set totalPoints [expr $totalPoints + $points]
}

puts $totalPoints
