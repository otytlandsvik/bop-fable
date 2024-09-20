// Excercise 1
let a = 3
printfn $"%i{a}"

// Excercise 2
let getAbs (f: float) : float = if f < 0. then f * -1.0 else f

printfn $"Absolute value of %f{3.}: %f{3. |> getAbs}"
printfn $"Absolute value of %f{-9.}: %f{-9. |> getAbs}"

// Exercise 3
let busTicketPrice (age: int) : unit =
    let price =
        match age with
        | a when a < 18 -> 20
        | a when a < 76 -> 40
        | _ -> 30

    printfn $"Person of age %i{age} must pay %i{price}kr"

[ 4; 17; 18; 69; 76; 99 ] |> List.iter busTicketPrice

// Exercise 4
let euclidean (p1: float * float) (p2: float * float) : float =
    let x1, y1 = p1
    let x2, y2 = p2

    (x2 - x1) ** 2 + (y2 - y1) ** 2 |> sqrt

let distance = ((2., 2.), (-3., -1.)) ||> euclidean
printfn $"Eclidean distance between (2, 2) and (-3, -1) is %f{distance}"

// Exercise 5
let getVelocity (v0: float) (a: float) (t: float) : float = v0 + a * t

let velocityAtTime = getVelocity 5 2

[ 0.; 4.; 9.5 ]
|> List.iter (fun t -> printfn $"Velocity at %.2f{t} was %.2f{t |> velocityAtTime}")
