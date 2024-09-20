// Exercise 1
let oddAndMod7 (n: int) : string =
    let evenStr = if n % 2 = 0 then "even" else "odd"
    let mod7Str = if n % 7 = 0 then "" else "not "
    $"%i{n} is %s{evenStr} and %s{mod7Str}divisible with 7"

printfn "Enter any integer:"
let userInput = System.Console.ReadLine()

let output =
    try
        userInput |> int |> oddAndMod7
    with _e ->
        "Given invalid input. Please input an integer!"

printfn $"%s{output}"

// Exercise 2
let absoluteDiff (a: int) (b: int) : int = if a < b then b - a else a - b

[ (2, 4); (4, 2); (69, 0) ]
|> List.iter (fun (a, b) ->
    let diff = absoluteDiff a b
    printfn $"Absolute difference between %i{a} and %i{b} is %i{diff}")

// Exercise 3
let findMax (a: int) (b: int) (c: int) : int =
    if a < b then
        if b < c then c else b
    else if a < c then
        c
    else
        a

let findMin (a: int) (b: int) (c: int) : int =
    if a < b then
        if c < a then c else a
    else if c < b then
        c
    else
        b

let printLargest (a: int) (b: int) (c: int) : unit =
    printfn $"Amongst %i{a}, %i{b} and %i{c}, %i{findMax a b c} is the largest"

let printSwapped (a: int) (b: int) (c: int) : unit =
    let min = findMin a b c
    let max = findMax a b c

    let swapped =
        [ a; b; c ]
        |> List.map (fun n ->
            match n with
            | n' when n' = min -> max
            | n' when n' = max -> min
            | n' -> n')

    printfn $"%i{a}, %i{b} and %i{c} swapped -> %i{swapped[0]}, %i{swapped[1]} and %i{swapped[2]}"

let printAscending (a: int) (b: int) (c: int) : unit =
    let min = findMin a b c
    let max = findMax a b c
    let mid = [ a; b; c ] |> List.find (fun n -> n <> max && n <> min)
    printfn $"%i{a}, %i{b} and %i{c} ascending -> %i{min}, %i{mid} and %i{max}"

[ (2, 4, 5); (5, 2, 4); (4, 5, 2); (5, 4, 2) ]
|> List.iter (fun (a, b, c) ->
    printLargest a b c
    printSwapped a b c
    printAscending a b c)

// Exercise 4

// Functional
[ 0..50 ] |> List.iter (fun n -> printfn $"%s{n |> oddAndMod7}")

// With loop
for i in [ 0..50 ] do
    printfn $"With for loop: %s{i |> oddAndMod7}"

// Exercise 5

// Functional
[ 1..40 ]
|> List.map float
|> List.iter (fun k -> printfn $"%.2f{(cos k) / (sin k)}")

// With for loop
for i in [ 1..40 ] do
    let k = i |> float
    printfn $"With for loop: %.2f{(cos k) / (sin k)}"

// With while loop
let mutable i = 1

while i >= 40 do
    let k = i |> float
    printfn $"With while loop: %.2f{(cos k) / (sin k)}"
    i <- i + 1
