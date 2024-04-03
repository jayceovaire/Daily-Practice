
function foo(n: number): number {
    if (n === 0) {
        return 1;
    }
    console.log(n)
    return n + foo(n - 1)
}
foo(5);

// Maze solver

["#,#,#,#,#,E,#",
"#, , , , , , #",
"#,S,#,#,#,#,#"]

// Base Case
//1. it's a wall
//2. off the map
//3. it's the end
//4. if we have seen it
