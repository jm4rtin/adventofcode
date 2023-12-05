set line1 ""
set line2 ""

set sumGearRatios 0
set gears [list]

proc append_to_gears {lineNo start stop value} {
    global gears

    set i 0
    set len [llength $gears]

    while {$i < $len} {
        set gear [lindex $gears $i]
        set gearLine [lindex $gear 0]
        set gearIdx [lindex $gear 1]

        if {$lineNo == $gearLine && $gearIdx >= $start && $gearIdx <= $stop} {
            lappend gear $value
            lset gears $i $gear
        }

        incr i
    }
}

proc process_line {before current after lineNo} {
    global gears

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

            append_to_gears $lineNo $matchStart $matchStart $matchValue
        }

        if {$matchEnd < $len_m1} {
            incr matchEnd

            append_to_gears $lineNo $matchEnd $matchEnd $matchValue
        }

        append_to_gears [expr $lineNo - 1] $matchStart $matchEnd $matchValue
        append_to_gears [expr $lineNo + 1] $matchStart $matchEnd $matchValue

        set start [expr $matchEnd + 1]
    }
}

set infile [open [lindex $argv 0] r]

set lineNo 0

while { [gets $infile line] >= 0 } {
    set len [string length $line]
    set start 0

    while {$start < $len} {
        set idx [string first {*} $line $start]

        if {$idx < 0} {
            break
        }

        lappend gears [list $lineNo $idx]

        set start [expr $idx + 1]
    }

    incr lineNo
}

close $infile

set infile [open [lindex $argv 0] r]

set lineNo -1

while { [gets $infile line3] >= 0 } {
    process_line $line1 $line2 $line3 $lineNo
    incr lineNo
    set line1 $line2
    set line2 $line3
}

process_line $line1 $line2 "" $lineNo

foreach gear $gears {
    if {[llength $gear] >= 4} {
        set a [lindex $gear 2]
        set b [lindex $gear 3]
        set ratio [expr $a * $b]
        set sumGearRatios [expr $sumGearRatios + $ratio]
    }
}

puts $sumGearRatios
