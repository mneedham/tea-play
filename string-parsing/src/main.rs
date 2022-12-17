use std::io;

fn main() {
    let mut user_input = String::new();
    let _result = io::stdin().read_line(&mut user_input);
    let vec: Vec<&str> = user_input
        .trim_end()
        .split(".")
        .collect();

    println!("Major:{:?}, Minor:{:?}, Patch: {:?}", vec[0], vec[1], vec[2]);
}
