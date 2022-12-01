$calories = Get-Content C:\Users\\Documents\calories.txt

$total_cals = @()
$running_sum = 0

For($i=0; $i -le $calories.Count; $i++) {
    if([string]::IsNullOrWhiteSpace($calories[$i])) { 
        $total_cals += $running_sum 
        $running_sum = 0
    } 
    else { 
        $running_sum += $calories[$i]
    }
}

# Part 1 Answer
($total_cals | measure -Maximum).Maximum

#Part 2

$sorted_cals = ($total_cals | Sort-Object -Descending) 

$sorted_cals[0] + $sorted_cals[1] + $sorted_cals[2]