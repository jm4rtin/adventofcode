set infile [open [lindex $argv 0] r]

set maxRed 12
set maxGreen 13
set maxBlue 14

set totalPower 0

while { [gets $infile line] >= 0 } {
    regexp {Game ([0-9]+): (.*)} $line match gameNum values

    set red 0
    set green 0
    set blue 0

    foreach game [split $values ";"] {
        foreach value [split $game ","] {
            regexp {\s*([0-9]+)\s*(red|green|blue)\s*} $value match count color


            if { [string equal $color "red"]} {
                set red [expr max($red,$count)]
            } elseif { [string equal $color "green"]} {
                set green [expr max($green,$count)]
            } elseif { [string equal $color "blue"]} {
                set blue [expr max($blue,$count)]
            }
        }
    }

    set power [expr $red * $green * $blue]
    set totalPower [expr $totalPower + $power]
}

puts $totalPower
