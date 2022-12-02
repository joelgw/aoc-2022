$rps = Get-Content C:\Users\\Documents\rps.txt
$running_score = 0

$rps | ForEach-Object -Process {
    $game = [string]$_.Split()

    # Convert to ASCII decimal representation and subtract, 21/24 Win, 23 Tie, Else Loss
    # Running total subtract 87 from int to get to 1/2/3 then add 3 or 6 for Draw/Win
    $outcome = [int]([char]$game[2]) - [int]([char]$game[0])

    if ($outcome -eq 21 -Or $outcome -eq 24) 
    # Win
    {$running_score += ([int]([char]$game[2])) - 81
    } 
    # Draw
    elseif ($outcome -eq 23) 
    {$running_score += ([int]([char]$game[2])) - 84}
    # Loss
    else 
    {$running_score += ([int]([char]$game[2])) - 87}
}

# Part 1 Answer
$running_score

# Hand-jammed the math. Wish I had found the mathematical way to determine win/tie/loss score
#   A B C
# X 3 1 2
# Y 4 5 6
# Z 8 9 7

$poss_score = (3, 4, 8), (1, 5, 9), (2, 6, 7)
$running_score = 0

$rps | ForEach-Object -Process {
    $game = [string]$_.Split()
    $running_score += $poss_score[[int]([char]$game[0]) - 65][[int]([char]$game[2]) - 88]
}

#Part 2 Answer
$running_score